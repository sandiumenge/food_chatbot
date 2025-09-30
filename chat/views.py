from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserProfile
from .services import AgentA, parse_foods
from django import forms
import openai
import os
from .services.restaurant_recommender import recommend_restaurant

class UserAnswerForm(forms.Form):
    raw_responses = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control w-[400px]','placeholder':'Type your answer'})
    )


def chat_view(request):
    chat = []
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")

    try:
        agent = AgentA()
        question = agent.ask_question("Ask the interviewed what are their 3 favourite foods so that you can recomend them a restaurant")
        if not question:
            question = "What are your 3 favourite foods?"
    except Exception:
        question = "What are your 3 favourite foods?"

    chat.append({'role':'agent', 'text': question})

    if request.method == 'POST':
        form = UserAnswerForm(request.POST)
        if form.is_valid():
            raw_response = form.cleaned_data['raw_responses']
            chat.append({'role':'user', 'text': raw_response})

            try:
                foods, is_vegetarian = parse_foods(raw_response)
            except Exception:
                foods = []
                is_vegetarian = False

            if len(foods) < 3:
                chat.append({'role':'agent', 'text': "Sorry, I couldn't understand your answer. Please try again."})
            else:
                UserProfile.objects.create(
                    username="User",    # Could be improved with auth
                    foods=foods,
                    raw_responses=raw_response,
                    is_vegetarian=is_vegetarian
                )

                recomendation = recommend_restaurant(foods, is_vegetarian)
                chat.append({'role':'agent', 'text': recomendation})

    else:
        form = UserAnswerForm()

    return render(request, 'chat/chat.html', {'chat': chat, 'form': form})
