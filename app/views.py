# app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat

def index(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '').strip().lower()

        if user_input == 'hello':
            response = "Hi there! How can I help you today?"
        elif user_input == 'how are you?':
            response = "I'm just a bot, but I'm functioning as expected!"
        elif user_input == 'bye':
            response = "Goodbye! Have a great day!"
        else:
            response = "Sorry, I didn't understand that."

        # Save the chat to the database
        chat = Chat(user_message=user_input, bot_response=response)
        chat.save()

        return JsonResponse({'response': response})

    # Retrieve the last 10 chats to display
    chats = Chat.objects.all().order_by('-timestamp')[:10]
    return render(request, 'chat.html', {'chats': chats})
