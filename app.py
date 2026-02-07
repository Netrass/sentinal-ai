import streamlit as st
from engine import SentinelEngine

st.set_page_config(page_title="Sentinel-AI | Observability", page_icon="🛡️")

st.title("🛡️ Sentinel-AI")
st.subheader("Predictive Data Reliability for PostHog-scale Pipelines")

# Sidebar for Config
with st.sidebar:
    api_key = st.text_input("Enter Google API Key", type="password")
    st.info("This tool monitors BigQuery logs and uses RAG to suggest fixes.")

if api_key:
    engine = SentinelEngine(api_key)

    # Live Monitoring
    tab1, tab2 = st.tabs(["Monitor", "Inject Memory"])

    with tab1:
        error_input = st.text_area("Simulate a New Error Log:", 
                                  placeholder="e.g., BigQuery Job failed: Access Denied to table 'events'...")
        
        if st.button("Run AI Analysis"):
            with st.spinner("Analyzing historical patterns..."):
                analysis = engine.get_rca(error_input)
                st.markdown("### 🤖 AI Insight")
                st.write(analysis)

    with tab2:
        st.write("Train the AI by adding past incident reports.")
        past_log = st.text_area("Past Incident Log:")
        if st.button("Save to Memory"):
            engine.add_memory(past_log)
            st.success("Memory Updated!")
else:
    st.warning("Please enter your API Key in the sidebar to begin.")