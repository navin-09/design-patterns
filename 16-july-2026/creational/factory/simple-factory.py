from abc import ABC, abstractmethod
from enum import Enum
# interface.py
class Notifier(ABC):
    @abstractmethod
    def send(self, to, msg):
        pass

# notifiers.py
class EmailNotifier(Notifier):
    def send(self,to, msg):
        print(f"sending email ${to} with message ${msg}")

class SmsNotifier(Notifier):
    def send(self,to, msg):
        print(f"sending sms ${to} with message ${msg}")

class Channel(Enum):
    EMAIL = "email"
    SMS = "sms"

class NotifierFactory:
    _Registry = {Channel.EMAIL : EmailNotifier,Channel.SMS : SmsNotifier} 
    def get(cls, channel:Channel) -> Notifier:
        if not cls._Registry[channel]:
            raise ValueError("channel not found please try again")
        return cls._Registry[channel]



# Client
factory = NotifierFactory()
factory.get(Channel.EMAIL).send("sandula.navin@gmail.com","Hi this simple factory")