import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)


def generate_response_with_groq(input_text):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": input_text}],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response from Groq: {e}")
        return f"Error: {e}"


def main():
    st.title("Groq Assistant")

    user_input = st.text_input("Enter your query:")
    if user_input:
        if st.button("Send"):
            response = generate_response_with_groq(user_input)
            st.subheader("Groq response:")
            st.write(response)


if __name__ == "__main__":
    main()
