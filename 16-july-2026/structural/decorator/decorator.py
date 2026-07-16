from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, to, msg):...

class smsNotifier(Notifier):
    def send(self, to, msg):
        print(f"message sent to ${to} with msg ${msg}")

class notifierDecorator(Notifier):
    def __init__(self,notifier):
        self._notifier = notifier
    def send(self,to,msg):
        self._notifier.send(to, msg)

class loggerDecorator(notifierDecorator):
    def send(self,to,msg):
        print("logginig the req....")
        super().send(to,msg)

class retryDecorator(notifierDecorator):   
    def send(self,to,msg):
        for i in range(3):
            try:
                print(f"ateempt {i}")
                super().send(to, msg)
                break
            except:
                print(f"ateempt ${i} failed")


            
def alert(n: Notifier, to: str, message: str):
    n.send(to, message) 
alert(retryDecorator(loggerDecorator(smsNotifier())), "sand@gmail.com","hi")
              