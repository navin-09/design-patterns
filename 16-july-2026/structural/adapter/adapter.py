from abc import ABC, abstractmethod


class TwillioSDK():
    def send_message(self,to,message):
        print(f"message sent to ${to} with ${message}")


class Notifier(ABC):
    @abstractmethod
    def send(self,to,msg):...

class TwillioAdapter(Notifier):
    def __init__(self,sdk):
        self._sdk = sdk
    def send(self, to, msg):
        self._sdk.send_message(to,msg)

        
def alert(notifier:Notifier, to:str, msg:str):
    notifier.send(to,msg)
    
alert(TwillioAdapter(TwillioSDK()),"sand@gmail.com","hi")