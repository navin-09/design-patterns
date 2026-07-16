from abc import ABC, abstractmethod
# interface.py
class Notifier(ABC):
    @abstractmethod
    def send(self, to, message):
        pass
# notifiers.py
class EmailNotifier(Notifier):
    def send(self, to, message):
        # Logic to send an email
        print(f"Sending email to {to}: {message}")
class SMSNotifier(Notifier):
    def send(self, to, message):
        # Logic to send an SMS
        print(f"Sending SMS to {to}: {message}")

# decorators.py
class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, to, message):
        self.notifier.send(to, message)

class LoggingNotifierDecorator(NotifierDecorator):
    def send(self, to, message):
        # Log the message before sending
        print(f"Logging: Sending message to {to}: {message}")
        super().send(to, message)

class RetryNotifierDecorator(NotifierDecorator):
    def send(self, to, message):
        # Retry logic before sending
        for attempt in range(3):
            try:
                print(f"Attempt {attempt + 1}: Sending message to {to}: {message}")
                super().send(to, message)
                break  # Exit loop if successful
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == 2:
                    print("All attempts failed.")

# client.py
# ── CLIENT: depends ONLY on Notifier, never on EmailNotifier or SMSNotifier ──
def alert(n: Notifier, to: str, message: str):
    n.send(to, message) 
if __name__ == "__main__":

    alert(LoggingNotifierDecorator(RetryNotifierDecorator(EmailNotifier())), "+1234", "hi")  # [logging → retry → email → +1234] hi
    print("\n")
    alert(RetryNotifierDecorator(LoggingNotifierDecorator(EmailNotifier())), "+1234", "hi")  # [logging → retry → email → +1234] hi
    print("\n")
    alert(LoggingNotifierDecorator(RetryNotifierDecorator(SMSNotifier())), "+1234555", "hi")  # [logging → retry → email → +1234] hi
    print("\n")
    alert(RetryNotifierDecorator(LoggingNotifierDecorator(SMSNotifier())), "+12345555", "hi")  # [logging → retry → email → +1234] hi