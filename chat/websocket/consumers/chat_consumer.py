from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.contrib.auth.models import User

from chat.models import OneToOneMessage

from profiles.models import Profile


class ChatConsumer(WebsocketConsumer):

    def __init__(self):
        self.room_name = None
        self.room_group_name = None
        self.sender = None
        self.receiver = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        sender_identifier, receiver_identifier = self.room_name.split('><')
        self.sender = Profile.objects.get(user__username=sender_identifier)
        self.receiver = Profile.objects.get(user__username=receiver_identifier)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

        # Receive message from room group

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
