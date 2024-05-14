import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from dotenv import dotenv_values
from sorter import get_news


class NewsSummarizer:
    def __init__(self):
        self.secrets = dotenv_values('.env')
        self.hf_email = self.secrets['EMAIL']
        self.hf_pass = self.secrets['PASSWORD']
        self.chatbot = None

        # Initialize the messages list in the session state
        if 'messages' not in st.session_state:
            st.session_state.messages = []

    def generate_response(self, prompt_input):
        try:
            # Hugging Face Login
            sign = Login(self.hf_email, self.hf_pass)
            cookies = sign.login()
            # Create ChatBot
            self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            response = self.chatbot.chat(prompt_input)
            return response
        except Exception as e:
            st.error(f"Error occurred: {e}")
            return "Sorry, I encountered an error. Please try again later."

    def run(self):
        st.title("News Summarizer")

        # User-provided prompt
        if prompt := st.chat_input(disabled=not (self.hf_email and self.hf_pass)):
            st.session_state.messages.append({"role": "user", "content": prompt})

            # If chatbot object is not initialized or if the last message is from the assistant, generate a response
            if not self.chatbot or (st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant"):
                with st.spinner("Thinking..."):
                    response = self.generate_response(prompt)
                    st.write("Archie:", response)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)
            # Otherwise, reuse the existing response
            else:
                st.write("Archie:", self.chatbot.chat(prompt))

if __name__ == "__main__":
    news_summarizer = NewsSummarizer()
    news_summarizer.run()
