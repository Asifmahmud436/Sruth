from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from groq import Groq
from django.views.generic import ListView
from .models import Ai
from .forms import AiForm

# the AI key and setup
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

# def home(request):
#     return render(request,'index.html')

def ai_response(question):
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": 'You are very empathic. You will give honest and genuine advice. But if anyone asks anything about you, You will say you are a cat named Sruth.'
        },
        {
            "role": "user",
            "content": question
        }
        
    ],
    temperature=1,
    # max_completion_tokens=1024,
    # top_p=1,
    # stream=True,
    # stop=None,
    )
    return response.choices[0].message.content



def make_question(request):
    if request.method == "POST":
        ai_form = AiForm(request.POST)
        if ai_form.is_valid():
            chat = ai_form.save(False)
            print(ai_form.cleaned_data['question'])
            response = ai_response(ai_form.cleaned_data['question'])
            print(response)
            chat.question = ai_form.cleaned_data['question']
            chat.answer = response
            chat.save()
            ai_form = AiForm()
            
    else:
        ai_form = AiForm()
    all_chat_list = Ai.objects.all()
    return render(request,'index.html',{'form':ai_form,'all_chat_list':all_chat_list})