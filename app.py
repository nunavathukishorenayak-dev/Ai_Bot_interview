import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(
    api_key=st.secrets("OPENAI_API_KEY")
)

# Page title
st.title("AI Interview Preparation Bot")

st.write("Practice interviews with AI")

# Select role
role = st.selectbox(
    "Select Job Role",
    [
        "Data Analyst",
        "Data Scientist",
        "Data Engineer",
        "Python Developer",
        "Machine Learning Engineer"
    ]
)

# Experience level
experience = st.selectbox(
    "Experience Level",
    [
        "Fresher",
        "1-3 Years",
        "3-5 Years"
    ]
)

# Generate questions button
if st.button("Generate Interview Questions"):

    prompt = f"""
    Generate 5 interview questions for a
    {experience} {role}.

    Include:
    - Technical questions
    - Scenario based questions
    - Problem solving questions
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    questions = response.choices[0].message.content

    st.subheader("Interview Questions")
    st.write(questions)

# User answer section
st.subheader("Answer a Question")

question = st.text_input("Paste Question Here")

answer = st.text_area("Write Your Answer")

# Evaluate answer
if st.button("Evaluate My Answer"):

    feedback_prompt = f"""
    You are an interview evaluator.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give:
    1. Score out of 10
    2. Technical Accuracy
    3. Communication
    4. Improvements
    5. Better Sample Answer
    """

    feedback_response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": feedback_prompt
            }
        ]
    )

    feedback = feedback_response.choices[0].message.content

    st.subheader("AI Feedback")
    st.write(feedback)
