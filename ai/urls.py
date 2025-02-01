from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_question, name='home'),  # Home page with form
    # path('ask/', views.make_question, name='ask_question'),  # Form submission URL
]
