import streamlit as st
from sorter import get_news

from hugchat import hugchat
from hugchat.login import Login
from dotenv import dotenv_values
import json

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
        
        
    def call_required_functions(self, required_actions):
        if not self.run:
            return 
        tool_output =  []
        for action in required_actions:
            function_name = action["function"]["name"]
            arguments = json.loads(action["function"]["arguments"])
            
            if function_name == "get_news":
                output = get_news(topic=arguments["topic"])
                print(f"NEWS: {output}")
                final_str = ""
                for item in output:
                    final_str += "".join(item)
                    
                tool_output.append({"tool_call_id": action["id"], "output": final_str})    

    
