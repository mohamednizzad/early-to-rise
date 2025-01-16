import streamlit as st
import openai
from datetime import datetime, timedelta
import io
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Prompt function for habits
def generate_habits(time_period, context, physical_condition):
    prompt = f"""
    Suggest one daily habit for improving productivity. Each habit should be aligned with the principle: 
    "Early to bed and early to rise makes a man healthy, wealthy, and wise." 
    Provide one habit for a {time_period} period considering the context of {context} and physical condition {physical_condition}.
    """
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
    )
    habits = response.choices[0].text.strip().split("\n")
    return [habit.strip() for habit in habits if habit.strip()]

# Streamlit App
def main():
    # Set page config
    st.set_page_config(
        page_title="New Beginnings: Daily Productivity Habits",
        page_icon="🌅",
        layout="centered",
        initial_sidebar_state="auto",
    )

    # Bootstrap CSS for styling
    st.markdown(
        """
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            font-family: 'Arial', sans-serif;
            color: #2c3e50;
            text-align: center;
        }
        .subheader {
            font-family: 'Arial', sans-serif;
            color: #34495e;
        }
        .markdown-text {
            font-family: 'Arial', sans-serif;
            color: #7f8c8d;
        }
        .download-button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main container">', unsafe_allow_html=True)

    # Add logo image
    st.image("logo.png", width=700)

    st.markdown('<h1 class="title">New Beginnings: Daily Productivity Habits</h1>', unsafe_allow_html=True)
    st.markdown('<p class="markdown-text">**Start your day with purposeful habits to boost productivity and well-being.**</p>', unsafe_allow_html=True)
    st.markdown('<p class="markdown-text">*Inspired by: "Early to bed and early to rise makes a man healthy, wealthy, and wise."*</p>', unsafe_allow_html=True)

    # Dropdown for selecting time period
    time_period = st.selectbox(
        "Select the time period for habit suggestions:",
        ["5 Minutes", "15 Minutes", "30 Minutes", "1 Hour"]
    )

    # Dropdown for selecting context
    context = st.selectbox(
        "Select the context for habit suggestions:",
        ["General", "Religious", "Cultural"]
    )

    # Dropdown for selecting physical condition
    physical_condition = st.selectbox(
        "Select your physical condition:",
        ["Strong", "Moderate", "Weak"]
    )

    # Habit generation
    if "habits" not in st.session_state or st.button("Generate New Habits"):
        st.session_state.habits = generate_habits(time_period, context, physical_condition)
        st.session_state.date = datetime.now().date()

    st.markdown(f'<h2 class="subheader">Habits for {st.session_state.date.strftime("%B %d, %Y")} ({time_period}, {context}, {physical_condition})</h2>', unsafe_allow_html=True)
    habits = st.session_state.habits

    # Display habits
    for idx, habit in enumerate(habits, 1):
        st.markdown(f'<p class="markdown-text">**{idx}.** {habit}</p>', unsafe_allow_html=True)

    # Feature to download the habits as a .txt file and PNG file in the same row
    st.markdown('<div class="row">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        habits_text = "\n".join([f"{idx}. {habit}" for idx, habit in enumerate(habits, 1)])
        st.download_button(
            label="Download Habits as .txt",
            data=habits_text,
            file_name=f"habits_{st.session_state.date.strftime('%Y%m%d')}.txt",
            mime="text/plain",
            key="txt_download",
            help="Download the habits as a text file",
            on_click=None,
            args=None,
            kwargs=None,
            disabled=False,
            use_container_width=False,
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Encouragement section
    st.markdown("---")
    st.markdown('<h2 class="subheader">Why these habits matter:</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="markdown-text">
            <li><strong>5-minute habit:</strong> A quick activity to jump-start your momentum.</li>
            <li><strong>15-minute habit:</strong> Focused time for meaningful progress.</li>
            <li><strong>30-minute habit:</strong> A substantial period to engage in productive activities.</li>
            <li><strong>1-hour habit:</strong> Deep work session for significant achievements.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
