import requests as r
import pandas as pd
import time
from datetime import date, timedelta, datetime
import hashlib
import pprint

private_key = "43fa6c6a2555f4a734f641514752881623501922" #Depois a chave privada
public_key = "d21372a3fb3270d48db29f67c5ca8e3d" #Depois a chave publica

#aqui vamos definir os parametros de hash conforme descrito no documento da API da Marvel
timestamp = str(time.time()) #datetime.now().strftime('%Y-%m-%d%H:%M:%S').encode('utf-8') #Primeiro trazemos o TS 


def hash_params():
    hash_md5 = hashlib.md5() #depois trazemos o md5 da library
    hash_md5.update(f'{timestamp}{private_key}{public_key}'.encode('utf-8')) #depois trazemos a junção e sempre convertendo com o utf-8
    hashed_params = hash_md5.hexdigest() #conforme instrucao do documento da API, trazer em digest.

    return hashed_params #construido o retorno de hash

def marvel_dataset_characters(): #inicia-se a construcao do dataset

    url = 'https://gateway.marvel.com:443/v1/public/characters' #URL padrao conforme documentacao
    
    params = { #constroi o conjunto de parametros baseado na documentacao: ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
    'ts': timestamp,  #primeiro ts
    'apikey': public_key, #segundo public key
    'hash': hash_params() #terceiro chama a hash_params
    }

    response = r.get(url, params) #unifica tudo em um comando de resposta
    data = response.json()  #transforma em um dicionario
  #  pprint.pprint(data) #leitura do resultado até aqui
    dt = data['data']['results'] #filtra o json para aparecer os dados que estao em results
  # print(dt) #leitura do resultado até aqui
    df = pd.DataFrame.from_records(dt, columns=['id','name','description','comics','series','stories','events']) #transforma em dataframe e seleciona as colunas que irao aparecer
 #   print(df) #leitura do resultado até aqui
    return df #me retorna os dados tabulados

#problema: falta converter o json que está dentro dos campos de comics, series, stories e events na etapa anterior ao de df
  
marvel_dataset_characters()
