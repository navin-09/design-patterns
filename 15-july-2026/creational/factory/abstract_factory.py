from abc import ABC, abstractmethod

# ---------- Product interfaces ----------
class Notifier(ABC):
    @abstractmethod
    def send(self, msg: str): ...

class ReceiptTracker(ABC):
    @abstractmethod
    def track(self, msg_id: str): ...

# ---------- Twilio family (coherent set) ----------
class SmsNotifier(Notifier):
    def send(self, msg): print(f"[twilio sms] {msg}")

class TwilioReceiptTracker(ReceiptTracker):
    def track(self, msg_id): print(f"[twilio receipt] {msg_id}")

# ---------- SendGrid family (coherent set) ----------
class EmailNotifier(Notifier):
    def send(self, msg): print(f"[sendgrid email] {msg}")

class SendGridReceiptTracker(ReceiptTracker):
    def track(self, msg_id): print(f"[sendgrid receipt] {msg_id}")

# ---------- Abstract Factory ----------
class NotificationFactory(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier: ...
    @abstractmethod
    def create_receipt_tracker(self) -> ReceiptTracker: ...

class TwilioFactory(NotificationFactory):
    def create_notifier(self):        return SmsNotifier()
    def create_receipt_tracker(self): return TwilioReceiptTracker()

class SendGridFactory(NotificationFactory):
    def create_notifier(self):        return EmailNotifier()
    def create_receipt_tracker(self): return SendGridReceiptTracker()

# ---------- Client: gets a GUARANTEED-compatible family ----------
def send_with_tracking(factory: NotificationFactory, msg: str, msg_id: str):
    notifier = factory.create_notifier()
    tracker  = factory.create_receipt_tracker()
    notifier.send(msg)
    tracker.track(msg_id)   # can't mismatch: sms+twilio OR email+sendgrid

# usage
send_with_tracking(TwilioFactory(),  "hi", "m1")   # sms + twilio receipt
send_with_tracking(SendGridFactory(), "hi", "m2")  # email + sendgrid receipt