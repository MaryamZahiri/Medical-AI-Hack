from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def gpt_agent(text_data):
    response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": f"You are a lab assistant. A medical lab report will be passed and user ask some question, respond them based on the information provided in the lab report. This is the lab report:\n {text_data}"},
        {"role": "user", "content": "Do I have anything wrong in the report?"}]
    )
    return response.choices[0].message.content

def chat_bot(user_message):
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[{"role": "user", "content": user_message}],
        # prompt=user_message,
        max_tokens=50
    )

    chatbot_response = response.choices[0].message.content
    return chatbot_response