import streamlit as st
import requests

st.title("AI-powered Adptive Learning")

page = st.sidebar.selectbox("GO to",["Dashboard","Content","Quiz","Feedback"])

if page == "Dashboard":
    st.subheader("Dashboard")
    user_id = st.text_input("Enter User ID")
    if st.button("Fetch Profile"):
        res = requests.get(f"http://localhost:8000/learner/profile/{user_id}")
        st.json(res.json())

elif page == "Content":
    st.subheader("Content Recommendation")
    user_id = st.text_input("User iD content")
    if st.button("Recommended"):
        res = requests.get(f"http://localhost:8000/content/recommended/{user_id}")
        st.json(res.json())


elif page == "Quiz":
    st.subheader("Adaptive Quiz")
    user_id = st.text_input("user ID for Quiz")
    topic = st.text_input("Topic")
    if st.button("Generate Quiz"):
        res = requests.get(f"http://localhost:8000/quiz/generate",json={"user_id":user_id,"topic": topic})
        st.json(res.json())

elif page == "Feedback":
    st.subheader("Feedback Analysis")
    user_id = st.text_input("User ID for feedback")
    text = st.text_area("Enter feedbak")
    if st.button("Analyze"):
        res = requests.get(f"http://localhost:8000/feedback/analyze",json={"user_id":user_id,"text":text})
        st.json(res.json())