import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(
    page_title="AI Interview Preparation Bot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Interview Preparation Bot")

st.write("Practice mock interviews with AI")

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

# Role Selection
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

# Experience Selection
experience = st.selectbox(
    "Experience Level",
    [
        "Fresher",
        "1-3 Years",
        "3-5 Years"
    ]
)

# Generate Questions
if st.button("Generate Interview Questions"):

    with st.spinner("Generating questions..."):

        prompt = f"""
        Generate 5 interview questions for a
        {experience} {role} candidate.

        Include:
        - Technical questions
        - Scenario-based questions
        - Problem-solving questions

        Keep questions beginner friendly.
        """

        try:

            response = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct",
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

        except Exception as e:

            st.error(f"Error: {e}")

# Answer Evaluation Section
st.subheader("Answer Evaluation")

question = st.text_input("Paste Interview Question")

answer = st.text_area("Write Your Answer")

# Evaluate Button
if st.button("Evaluate My Answer"):

    with st.spinner("Evaluating answer..."):

        feedback_prompt = f"""
        You are an interview evaluator.

        Interview Question:
        {question}

        Candidate Answer:
        {answer}

        Evaluate the answer.

        Give:
        1. Score out of 10
        2. Strengths
        3. Improvements
        4. Better Sample Answer

        Keep feedback simple and beginner friendly.
        """

        try:

            feedback_response = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct",
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

        except Exception as e:

            st.error(f"Error: {e}")
