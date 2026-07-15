
from dataclasses import dataclass


@dataclass(frozen=True)
class User:    
    name: str
    age: int   
    email: str 
    
class UserBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.email = None

    def set_name(self,name):
        self.name = name
        return self
    def set_age(self,age):
        self.age = age
        return self
    def set_email(self,email):
        self.email = email
        return self
    def build(self):
        # we can have validations here
        return User(name=self.name, age=self.age, email=self.email)

q =(UserBuilder().set_name("John").set_age(30).set_email("jhon@gmail.com").build()) 
print(q)  # Output: John