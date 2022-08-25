import requests
from twilio.rest import Client

class SendMessage:
    def __init__(self):
        self.account_sid = ''
        self.auth_token = ''
        self.client = Client(self.account_sid, self.auth_token)

    def create_message(self, msg_body):
        message = self.client.messages.create(
            body=msg_body,
            from_='+17753466808',
            to='+13609997488'
        )