from abc import ABC, abstractmethod
from enum import Enum

class Notifier(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotifier(Notifier):
    def send(self):
        print("Sending email notification")

class SMSNotifier(Notifier):
    def send(self):
        print("Sending SMS notification")



class Channel(Enum):
    EMAIL = "email"
    SMS   = "sms"    
    
_Registry = {
    Channel.EMAIL: EmailNotifier,
    Channel.SMS: SMSNotifier
}

def get_notifier(notifier_type: Channel) -> Notifier:
    cls = _Registry.get(notifier_type)
    if cls is None:
        raise ValueError(f"unknown notifier: {notifier_type}")
    return cls()
get_notifier(Channel.EMAIL).send()  # Output: Sending email notification