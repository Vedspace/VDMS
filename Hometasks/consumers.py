from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join a group
        await self.channel_layer.group_add("task_notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard("task_notifications", self.channel_name)

    async def task_message(self, event):
        # Send message to WebSocket client
        await self.send(json.dumps({
            'title': event['message']['title'],
            'details': event['message']['details']
        }))
