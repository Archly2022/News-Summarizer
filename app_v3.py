"""
News Summarizer App Version 3:

This Streamlit application allows users to summarize news articles based on a keyword/topic.
Users can input a topic of interest, specify the number of articles to retrieve, and the
application will fetch the latest news articles from the web related to that topic. It then
summarizes the articles and provides the summarized information to the user.


Instructions:
- Enter a keyword/topic in the text input field.
- Specify the number of articles to retrieve using the number input field.
- Click on the "Summarize" button to initiate the summarization process.
- The application will display the retrieved news articles along with their summaries.
- It will also provide additional insights or instructions based on the summarized content.
"""

import streamlit as st
import time  
from newz import NewsSummarizer  
from dotenv import load_dotenv
from sorter import get_news 

# Load environment variables from .env file
load_dotenv()

st.title('News Summarizer')

def main():
    manager = NewsSummarizer()   
    st.write("Enter any keyword to search for the latest news globally")
    
    with st.form(key="user_input_form"):
        topic = st.text_input("Enter topic")
        num_news = st.number_input("Number of articles to retrieve", min_value=1, max_value=30, step=1, value=5)
        submit_button = st.form_submit_button(label="Summarize")
        
    if submit_button:
        st.write("Here are the latest news articles...")
        news = get_news(topic)
        news = news[:num_news]  # Limit the number of news articles based on user input
        
        if not news:  # Check if news list is empty
            st.write("No news found!")
        else:
            for i, article in enumerate(news, start=1):
                st.write(f"### Article {i}")
                st.write(article)
                
        message_content = f"exhibit {news}. please give a paragraph for each subject"
        with st.spinner("Thinking..."):
            message = manager.generate_response(message_content)
            time.sleep(5)  # Increase the runtime of the spinner (5 seconds in this example)
            
        st.write(message)
        st.write("Run Steps:")

if __name__ == "__main__":
    main()
