from sqlalchemy import Column,String,Integer,ForeignKey
from database import base,engine;

class shr(base):
    __tablename__="demo"
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(89))
    password=Column(String(78))
    
class hey(base):
    __tablename__="posted"
    id=Column(Integer,primary_key=True)
    title=Column(String(78))    
    context=Column(String(78))
    user_id=Column(Integer,ForeignKey("demo.id"))
    
class comment(base):
    __tablename__="commits"   
    r_no=Column(Integer,primary_key=True, autoincrement=True) 
    cmd=Column(String(78))
    ref_id=Column(Integer,ForeignKey("posted.id"))
    
    
    
    