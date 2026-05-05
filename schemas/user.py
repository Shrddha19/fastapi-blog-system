from pydantic import BaseModel

class demo(BaseModel):
    email:str
    password:str
    
class goo(BaseModel):
    title:str 
    context:str   