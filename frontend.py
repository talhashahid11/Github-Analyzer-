import streamlit as st
import requests

st.set_page_config(page_title="GitHub Analyzer", layout="wide")

st.title("🚀 GitHub Analyzer AI")

tab1, tab2 = st.tabs(["🔍 Analyze Profile", "⚔️ Compare Profiles"])

# ========================
# ANALYZE
# ========================
with tab1:
    username = st.text_input("Enter GitHub Username")

    if st.button("Analyze"):
        if username:
            with st.spinner("Analyzing..."):
                res = requests.post(
                    "http://localhost:8000/analyze",
                    json={"username": username}
                )

                data = res.json()

                if "data" in data:
                    result = data["data"]

                    st.success("Analysis Complete ✅")

                    col1, col2 = st.columns(2)

                    col1.metric("⭐ Total Stars", result["stats"]["total_stars"])
                    if result["stats"]["top_languages"]:
                        col2.metric("💻 Top Language", result["stats"]["top_languages"][0][0])

                    st.divider()

                    st.markdown(result["analysis"])

                else:
                    st.error("Backend error")

# ========================
# COMPARE
# ========================
with tab2:
    users = st.text_input("Enter usernames (comma separated)")

    if st.button("Compare"):
        if users:
            usernames = [u.strip() for u in users.split(",")]

            if len(usernames) < 2:
                st.warning("Enter at least 2 users")
            else:
                with st.spinner("Comparing..."):
                    res = requests.post(
                        "http://localhost:8000/compare",
                        json={"usernames": usernames}
                    )

                    data = res.json()

                    st.success("Comparison Done ✅")
                    st.markdown(data["comparison"])
