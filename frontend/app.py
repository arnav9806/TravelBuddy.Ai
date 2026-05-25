import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)


import streamlit as st
from langchain_core.messages import HumanMessage
from main import app

# PAGE CONFIG
st.set_page_config(
    page_title="TravelBuddy AI",
    page_icon="✈️",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.hero {
    text-align: center;
    padding: 2rem;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: white;
}

.hero-subtitle {
    color: #cbd5e1;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
    border: 1px solid #334155;
    padding: 15px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#3b82f6,#8b5cf6);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg,#2563eb,#7c3aed);
}

.result-card {
    background: #1e293b;
    padding: 25px;
    border-radius: 16px;
    margin-top: 20px;
    border: 1px solid #334155;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
}

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 15px;
    color: #60a5fa;
}

.footer {
    text-align: center;
    padding: 2rem;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero">
    <div class="hero-title">✈️ TravelBuddy AI</div>
    <div class="hero-subtitle">
        Your AI Powered Travel Planner using LangGraph + Multi Agents
    </div>
</div>
""", unsafe_allow_html=True)

# INPUT
user_query = st.text_input(
    "Enter your travel plan",
    placeholder="Example: Plan a 5 day Dubai trip with flights and hotels"
)

# BUTTON
if st.button("Generate Travel Plan"):

    if user_query:

        with st.spinner("TravelBuddy AI is planning your trip..."):

            config = {
                "configurable": {
                    "thread_id": "streamlit_user"
                }
            }

            result = app.invoke(
                {
                    "messages": [
                        HumanMessage(content=user_query)
                    ],
                    "user_query": user_query,
                    "flight_results": "",
                    "hotel_results": "",
                    "itinerary": "",
                    "llm_calls": 0
                },
                config=config
            )

            final_response = result["messages"][-1].content

        # RESULT CARD
        st.markdown(f"""
        <div class="result-card">
            <div class="section-title">🌍 Your AI Travel Plan</div>
            <div style="line-height:1.8;">
                {final_response}
            </div>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    Built with LangGraph • Groq • Tavily • Streamlit
</div>
""", unsafe_allow_html=True)