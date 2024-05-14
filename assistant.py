import openai
from dotenv import find_dotenv, load_dotenv
import time
from datetime import datetime
import logging


class OpenAssist:
    def __init__(self, assistant_id=None, thread_id=None):
        self.client = openai.OpenAI()
        self.assistant_id = assistant_id
        self.thread_id = thread_id
        self.run = None
        self.summary = None
        
        if self.assistant_id is None:
            self.assistant = self.client.beta.assistants.create(model="gpt-3.5-turbo-16k")
            self.assistant_id = self.assistant.id
        else:
            self.assistant = self.client.beta.assistants.retrieve(
                assistant_id = self.assistant.id)    
            
        if self.thread_id is None:
            self.thread = self.client.beta.threads.create()
            self.thread_id = self.thread.id
        else:
            self.thread = self.client.beta.threads.retrieve(
                thread_id = self.thread.id)
            
            
    def create_message(self, message_content):
        message = self.client.beta.threads.messages.create(
            thread_id=self.thread_id, role="user", content=message_content
        )
        return message

    def run_assistant(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id,
        )
        return run
    
    def wait_for_run_completion(self, run_id, sleep_interval=2):
        while True:
            try:
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread_id, run_id=run_id
                )
                if run.completed_at:
                    messages = self.client.beta.threads.messages.list(thread_id=self.thread_id)
                    summary = []
                    last_message = messages.data[0]
                    response = last_message.content[0].text.value
                    summary.append(response)
                    self.summary = "\n".join(summary)
                    print(f"Assistant Response: {response}")
                    break
            except Exception as e:
                logging.error(f"An error occurred while retrieving the run: {e}")
                break
            logging.info("Waiting for run to complete...")
            time.sleep(sleep_interval)
            
    def get_summary(self):
        return self.summary  
    

            
