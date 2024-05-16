"""
News Summarizer App Version 2:

This Streamlit application allows users to summarize news articles based on a keyword/topic.
Users can input a topic of interest, specify the number of articles to retrieve, and the
application will fetch the latest news articles from the web related to that topic. It then
summarizes the articles and provides the summarized information to the user.
Providing you a webview interface of returned topics.


Instructions:
- Enter a keyword/topic in the text input field.
- Specify the number of articles to retrieve using the number input field.
- Click on the "Summarize" button to initiate the summarization process.
- The application will display the retrieved news articles along with their summaries.
"""

#Todo: Sign in on your open ai account an add your API key to your created .env file to use features on this app

from dotenv import find_dotenv, load_dotenv
import streamlit as st
from sorter import get_news
from assistant import OpenAssist

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            # background-color: #ffffff;
            background-image: url('https://playgroundai-playground-v2-5.hf.space/--replicas/bdj8s/file=/tmp/gradio/faf42909ce8d442b570c02e55a68725a823b1946/b656e8b8-10ae-468d-991c-4e2005f80c5a.png');
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            margin-top: 50px;
        }

        h1{
            color: #00C29F;
            margin-bottom: 20px;
        }
        #hs{
        color: #00C29F;

        }

        p {
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>News Summarizer</h1>
        <p id="hs">The Best News Filter in the Globe</p>
    </div>
</body>
</html>
"""
st.markdown(html_code, unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

# Load environment variables from .env file
load_dotenv()

def main():
    manager = OpenAssist()   
    st.write("Enter any key word to search for the latest news in the globe")
    
    with st.form(key="user_input_form"):
        topic = st.text_input("Enter topic")
        num_news = st.number_input("Number of search", min_value=1, max_value=30, step=1, value=5)
        submit_button = st.form_submit_button(label="Run Assistant")

        
    if submit_button:
        st.write("Here are the latest news articles...")
        news = get_news(topic)
        news = news[:num_news]  # Limit the number of news articles based on user input
        if not news:  # Check if news list is empty
            st.write("No news found!")
                
        message_content = f"{news}"        
        manager.create_message(message_content)
        run = manager.run_assistant()
        manager.wait_for_run_completion(run.id)       
        summary = manager.get_summary()
        st.write(summary)
 
        st.text("Run Steps:")
    

if __name__ == "__main__":
    main()
