import os
from dotenv import load_dotenv # Add this
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Load the environment variables from .env
load_dotenv()

class SentinelEngine:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found. Check your .env file.")

        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
        
        self.vectorstore = Chroma(
            collection_name="incident_memory",
            embedding_function=self.embeddings,
            persist_directory="./chroma_db"
        )

    def add_memory(self, text):
        """Adds historical logs to the vector store."""
        self.vectorstore.add_texts([text])

    def get_rca(self, error_msg):
        """Retrieves context and generates fix."""
        template = """
        Context from past incidents:
        {context}

        New Pipeline Error:
        {error_message}

        As an AI Product Engineer, provide:
        1. Root Cause Analysis (RCA)
        2. A code-based fix (SQL or Python)
        """
        prompt = ChatPromptTemplate.from_template(template)
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 2})

        chain = (
            {"context": retriever, "error_message": RunnablePassthrough()}
            | prompt
            | self.llm
        )
        return chain.invoke(error_msg).content