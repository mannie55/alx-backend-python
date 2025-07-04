from rest_framework import serializers
from .models import Conversation, Message
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='get_full_name', read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 'first_name', 'last_name',
            'phone_number', 'bio', 'display_name', 'password'
        ]

    def create(self, validated_data):
        """
        Create a new user instance with the provided validated data.
        The password is set using the set_password method to ensure hashing.
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None or not user.is_active:
            raise serializers.ValidationError("Invalid credentials")
        return {'user': user}
    

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    short_message = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'message_id', 'conversation', 'sender', 'message_body',
            'sent_at', 'short_message'
        ]

    def get_short_message(self, obj):
        # Return the first 20 characters of the message body
        return obj.message_body[:20]

    def validate_message_body(self, value):
   #raise errors if the message body is empty
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']