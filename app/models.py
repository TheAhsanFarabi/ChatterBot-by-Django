from django.db import models

class Chat(models.Model):
    user_message = models.CharField(max_length=255)
    bot_response = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
