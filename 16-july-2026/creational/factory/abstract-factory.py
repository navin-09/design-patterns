from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, msg):...
class RecipietTracker(ABC):
    @abstractmethod
    def track(self, msg_id):...

class TwillioSmsNotifier(Notifier):
    def send(self, msg):print(f"sending sms  ${msg}")
class TwilioReceiptTracker(RecipietTracker):
    def track(self, msg_id): print(f"[twilio receipt] {msg_id}")
class SendgridEmailNotifier(Notifier):
    def send(self, msg):print(f"sending email  ${msg}")
class SendgridReceiptTracker(RecipietTracker):
    def track(self, msg_id): print(f"[sengrid receipt] {msg_id}")
class NotificationFactory(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier: ...

    @abstractmethod
    def create_receipt_tracker(self) -> Notifier: ...

class TwilioFactory(NotificationFactory):
    def create_notifier(self):        return TwillioSmsNotifier()
    def create_receipt_tracker(self): return TwilioReceiptTracker()

class SendGridFactory(NotificationFactory):
    def create_notifier(self):        return SendgridEmailNotifier()
    def create_receipt_tracker(self): return SendgridReceiptTracker()



def send_with_tracking(factory:NotificationFactory, msg: str, msg_id: str):
    notifier = factory.create_notifier()
    receipt_tracker = factory.create_receipt_tracker()
    notifier.send(msg)
    receipt_tracker.track(msg_id)

send_with_tracking(TwilioFactory(),'hi', 'm1-id')
send_with_tracking(SendGridFactory(),'hi', 'm2-id')
