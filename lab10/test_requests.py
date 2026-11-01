import requests
import pytest
class UsersClient:
    def __init__(self,url):self.url=url
    def send(self,method,suffix='',**kwargs):return requests.request(method,self.url+suffix,timeout=3,**kwargs)
@pytest.fixture
def client(api_url):return UsersClient(api_url)
def test_contract(client):
    result=client.send('GET');assert result.status_code==200
    assert 'application/json' in result.headers['Content-Type']
    assert all({'id','name','username','email'}<=item.keys() for item in result.json())
def test_single(client):
    result=client.send('GET','/1');assert result.status_code==200
    assert result.json()['email']=='pavel@example.com'
def test_crud(client):
    data=dict(name='Daria',username='daria',email='daria@example.com')
    created=client.send('POST',json=data);assert created.status_code==201
    identifier=created.json()['id'];suffix=f'/{identifier}'
    replacement=dict(data,username='new_daria')
    response=client.send('PUT',suffix,json=replacement)
    assert response.status_code==200 and response.json()['username']=='new_daria'
    assert client.send('GET',suffix).json()==dict(replacement,id=identifier)
    assert client.send('DELETE',suffix).status_code==204
    assert client.send('GET',suffix).status_code==404
@pytest.mark.parametrize('method',['GET','PUT','DELETE'])
def test_unknown_entity(client,method):assert client.send(method,'/987',json={}).status_code==404
@pytest.mark.parametrize('body',[{},dict(name='X',username='x',email='broken')])
def test_bad_body(client,body):assert client.send('POST',json=body).status_code==400
