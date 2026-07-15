from  abc import ABC, abstractmethod 

class TwilioSdk():
    def send_message(self, to, message):
        # Logic to send a message using Twilio's SDK
        print(f"Sending message to {to} via Twilio: {message}")

class Notifier(ABC):
    @abstractmethod
    def send(self, to, message):
        pass


class TwilioAdapter(Notifier):
    def __init__(self, twilio_sdk):
        self.twilio_sdk = twilio_sdk

    def send(self, to, message):
        # Adapting the interface to match the expected method
        self.twilio_sdk.send_message(to, message)

# ── CLIENT: depends ONLY on Notifier, never on Twilio ──
def alert(n: Notifier, to: str, message: str):
    n.send(to, message)

alert(TwilioAdapter(TwilioSdk()), "+1234", "hi")  # [twilio → +1234] hi
