
from dataclasses import dataclass


@dataclass
class User:
    name:str
    email:str
    phno:int

class UserBuilder:
    def __init__(self):
        self._name = None
        self._email = None
        self._phno = None

    def setName(self,name):
        self._name = name
        return self
    
    def setEmail(self,email):
        self._email = email
        return self
    
    def setPhno(self,phno):
        self._phno = phno
        return self
    
    def build(self):
        return User(name= self._name, email=self._email, phno=self._phno)


user = UserBuilder()
u = user.setName("Naveen").setEmail("sandul@gmail.com").setPhno(9090).build()
print(u)
    
    