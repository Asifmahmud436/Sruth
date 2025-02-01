from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from groq import Groq
from django.views.generic import ListView
from .models import Ai

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
    # response.choices[0].message.content
)

def home(request):
    return render(request,'index.html')

class HomePageView(ListView):
    model = Ai
    template_name = 'index.html'
    context_object_name = 'all_chat_list'