import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI News Assistant",
    page_icon="📰",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("📰 AI News Assistant")
st.write(
    "Get AI-powered summaries for news, IPL, weather, politics, business, and technology."
)

st.divider()

# ---------------- USER INPUT ----------------
query = st.text_input(
    "Enter your query",
    placeholder="Example: IPL news, weather in Hyderabad, AI updates..."
)

# ---------------- SEARCH BUTTON ----------------
if st.button("🔍 Search", use_container_width=True):

    if query.strip() == "":
        st.warning("⚠️ Please enter a query")

    else:
        try:
            with st.spinner("Fetching latest updates..."):

                # n8n webhook URL
                url = "https://mukeshsai.app.n8n.cloud/webhook/chat"

                payload = {
                    "query": query
                }

                response = requests.post(url, json=payload)

            # ---------------- SUCCESS ----------------
            if response.status_code == 200:

                result = response.text

                st.success("✅ Result")
                st.markdown(result.replace("\\n", "\n"))

            # ---------------- ERROR ----------------
            else:
                st.error(f"❌ Error: {response.status_code}")

        except Exception as e:
            st.error(f"🚨 Something went wrong: {e}")

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header("📌 Example Queries")

    st.markdown("""
    - IPL latest news  
    - Weather in Hyderabad  
    - AI technology updates  
    - Business news today  
    - Politics headlines  
    - Stock market updates  
    """)

    st.divider()

    st.info("Powered by n8n + Gemini AI + Streamlit")