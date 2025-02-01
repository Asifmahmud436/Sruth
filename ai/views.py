from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from groq import Groq

MY_KEY = os.getenv('SRUTH_KEY')


client = Groq(
    api_key=MY_KEY
)
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Can you see this?"
        },
        
    ],
    temperature=1,
    # max_completion_tokens=1024,
    # top_p=1,
    # stream=True,
    # stop=None,
)

def home(request):
    return HttpResponse(response.choices[0].message.content)