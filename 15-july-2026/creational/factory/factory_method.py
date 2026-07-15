from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, msg: str): ...

class EmailNotifier(Notifier):
    def send(self, msg): print(f"[email] {msg}")

class SmsNotifier(Notifier):
    def send(self, msg): print(f"[sms] {msg}")

# ---------- Factory Method ----------
class NotificationCreator(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier: ...

    # base controls the invariant algorithm; product is injected by subclass
    def notify(self, msg: str) -> None:
        notifier = self.create_notifier()
        notifier.send(msg)

class EmailCreator(NotificationCreator):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()

class SmsCreator(NotificationCreator):
    def create_notifier(self) -> Notifier:
        return SmsNotifier()

# usage
EmailCreator().notify("hi")   # [email] hi
SmsCreator().notify("hi")     # [sms] hi