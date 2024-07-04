Groq Assistant

A Streamlit app that generates responses using the Groq AI model.
Description

This project is a simple web application that uses the Streamlit framework to allow users to interact with the Groq AI model. Users can input their query, and the app will generate a response using the Groq API.
Features

    User input: A text input field where users can enter their query.
    Response generation: Uses the Groq API to generate a response to the user's query.
    Error handling: Handles any errors that occur during the response generation process and displays an error message to the user.

Requirements

    Python 3.8 or later
    Streamlit
    Groq API key (stored in a .env file)

Running the app

    Clone the repository and navigate to the project directory.
    Install the required dependencies by running pip install -r requirements.txt.
    Run the app by executing streamlit run groq_assistant.py.

Configuration

To use this app, you'll need to store your Groq API key in a .env file in the project directory. This file should contain the following line:

GROQ_API_KEY=your_api_key_here

Replace your_api_key_here with your actual Groq API key.
