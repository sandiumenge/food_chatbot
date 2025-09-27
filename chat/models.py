from django.db import models

# Doesn't make sense now but it's for a future use
from django.contrib.auth.models import User

class Conversation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    conversation_number = models.IntegerField(unique=True)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=20, choices=[
        ('chatgpt_a', 'ChatGPT A'),
        ('chatgpt_b', 'ChatGPT B'),
        ('user', 'Human User') # For future use (if I want to extend to human users)
    ])
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.sender_type} at {self.created_at}: {self.message_text[:50]}"
    
class UserProfile(models.Model):
    conversation = models.OneToOneField(Conversation, on_delete=models.CASCADE, related_name='user_profile')
    username = models.CharField(max_length=50)
    foods = models.JSONField(default=list)
    is_vegetarian = models.BooleanField(default=False) # Vegetarian/Vegan
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Profile of {self.username} (Vegetarian: {self.is_vegetarian})"