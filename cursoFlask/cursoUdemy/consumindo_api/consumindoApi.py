import json
import requests

URL = 'http://127.0.0.1:5000'

#Buscando hoteis
respostas_hoteis = requests.request('GET',URL + '/hoteis?cidade=São Paulo')

print (respostas_hoteis.status_code)

hoteis = respostas_hoteis.json()

listaHoteis = hoteis['hoteis']
for hotel in listaHoteis:
    print (hotel['nome'])

#Criando usuario
enpoint_cadastro = URL + '/cadastro'
body_cadastro = {
    'login':'Arystoteles',
    'senha':'12345'
}
headers_cadstro = {
    'Content-Type': 'application/json'
}

resposta_cadastro = requests.request('POST',enpoint_cadastro,json=body_cadastro,headers=headers_cadstro)
print(resposta_cadastro.status_code)
print(resposta_cadastro.json())

#realizando login
enpoint_login = URL + '/login'

body_login = body_cadastro
headers_login = headers_cadstro

resposta_login = requests.request('POST',enpoint_login,json=body_login,headers=headers_login)
token = resposta_login.json()
print(resposta_login.status_code)
print(token)

#Criando um hotel
endpoint_hotel_id = URL + '/hoteis/meuHotel'
body_hotel = {
    'nome': 'meuHotel',
    'estrelas': 4.6,
    'diaria': 200.00,
    'cidade': 'Alvorada',
    'site_id': 3
}

headers_hotel_id = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token['access_token']
}

resposta_hotel_id = requests.request('POST',endpoint_hotel_id,json=body_hotel,headers=headers_hotel_id)
print(resposta_hotel_id.json())

#Alterando Hotel
endpoint_hotel_id_put = URL + '/hoteis/meuHotel'
body_hotel_put = {
    'nome': 'meuHotel',
    'estrelas': 4.6,
    'diaria': 230.00,
    'cidade': 'Alvorada',
    'site_id': 3
}


resposta_hotel_id_put = requests.request('PUT',endpoint_hotel_id_put,json=body_hotel_put,headers=headers_hotel_id)
print(resposta_hotel_id_put.json())

#Deletando hoteis
endpoint_hotel_id_delete = URL + '/hoteis/meuHotel'
resposta_hotel_id_delete = requests.request('DELETE',endpoint_hotel_id_delete,headers=headers_hotel_id)
print(resposta_hotel_id_delete.json())

#Buscar usuarios 
endpoint_user_id = URL + '/usuarios/1'

headers_users_id = {
    'Content_Type': 'application/json',
    'Authorization': 'Bearer ' + token['access_token']
}

resposta_user_id = requests.request('GET',endpoint_user_id,headers=headers_users_id)
print(resposta_user_id.json())

#deletando usuarios
endpoint_user_id_delete = URL + '/usuarios/1'

headers_users_id = {
    'Content_Type': 'application/json',
    'Authorization': 'Bearer ' + token['access_token']
}

resposta_user_id_delete = requests.request('DELETE',endpoint_user_id_delete,headers=headers_users_id)
print(resposta_user_id_delete.json())
