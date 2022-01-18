import pytest
import requests
import jwt

url = 'http://127.0.0.1:5000' 

def test_index_page():
    r = requests.get(url+'/') 
    assert r.status_code == 200 
def test_getUser():
    r = requests.get(url+'/GetUserInfo?uid=1') 
    assert r.status_code == 200 

def test_Postrequest():
    data ={"name":"arya","age":20,"city":"New york"}
    token=jwt.encode(data,key="JWT_p@ssword")
    r = requests.post(url+'/CreateUser',json={'token':token}) 
    assert r.status_code == 200 
    
def test_Putrequest():
    data ={"name":"jhonny","age":25}
    token=jwt.encode(data,key="JWT_p@ssword")
    r = requests.put(url+'/EditUser/2',json={'token':token}) 
    assert r.status_code == 200

def test_Deleterequest():
   token=jwt.encode({"action":"delete"},key="JWT_p@ssword")
   r = requests.delete(url+'/DeleteUser/2',json={'token':token}) 
   assert r.status_code == 200