from channels.consumer import SyncConsumer,AsyncConsumer
from channels.consumer import StopConsumer
from .models import Patients
from django.core import serializers
from django.http import JsonResponse
from time import sleep
import json
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket conncted.........',event)
        self.send(
            {
                'type':'websocket.accept',
                
            }
        )
    def websocket_receive(self,event):
        print('websocket received.........',event)
        print('received message is',event['text'])
        all_pateints=Patients.objects.all()
        data=serializers.serialize('json',all_pateints)
        
        
        self.send({
                'type':'websocket.send',
                'text':data
            })
            

    def websocket_disconnect(self,event):
        print('websocket disconnected.........',event)
        raise StopConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connected.........',event)
        await self.send(
            {
                'type':'websocket.accept'
            }
        )
    async def websocket_receive(self,event):
        print('websocket received.........',event)
        print('received message is',event['text'])

    async def websocket_disconnect(self,event):
        print('websocket disconncted.........',event)
        raise StopConsumer


