from abc import ABC, abstractmethod
from enum import Enum

class Notifier(ABC):
    @abstractmethod
    def send(self, to, msg): ...

class EmailNotifier(Notifier):
    def send(self, to, msg):
        print(f"sending email {to} with message {msg}")

class SmsNotifier(Notifier):
    def send(self, to, msg):
        print(f"sending sms {to} with message {msg}")

class Channel(Enum):
    EMAIL = "email"
    SMS   = "sms"

class NotifierFactory:
    _Registry = {Channel.EMAIL: EmailNotifier, Channel.SMS: SmsNotifier}

    def get(self, channel: Channel) -> Notifier:
        notifier_cls = self._Registry.get(channel)
        if notifier_cls is None:
            raise ValueError("channel not found, please try again")
        return notifier_cls()          # ← instantiate!

factory = NotifierFactory()
factory.get(Channel.EMAIL).send("sandula.navin@gmail.com", "Hi this is simple factory")
# sending email sandula.navin@gmail.com with message Hi this simple factory