
  # News Summarizer App

  Note: Please install the necessary libraries to boot this app. You can visit the free website on <a href="https://globalnewz.streamlit.app">globalnewz</a>
to preview and run the project on your device:

  1) Open project folder in <a href="https://code.visualstudio.com/download">Visual Studio Code</a>
  2) In the terminal, run install `pip install requirements.txt` and create your .env file to store your token keys to use the openai API
  3) To run the app's 1st version vist <a href="https://platform.openai.com">link</a> with your account and create an API key to run the program and store it on your `.env` file.
  4) Run `streamlit run streamlit.py` to view the project in the browser
  
""""
# News Summarizer App:

This Streamlit application allows users to summarize news articles based on a keyword/topic.
Users can input a topic of interest, specify the number of articles to retrieve, and the
application will fetch the latest news articles from the web related to that topic. It then
summarizes the articles and provides the summarized information to the user.

The application also uses a chat interface to interact with users, providing them with a
conversational experience while summarizing the news.

Instructions:
- Enter a keyword/topic in the text input field.
- Specify the number of articles to retrieve using the number input field.
- Click on the "Summarize" button to initiate the summarization process.
- The application will display the retrieved news articles along with their summaries.
- It will also provide additional insights or instructions based on the summarized content.
"""
