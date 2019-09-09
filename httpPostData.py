# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:40:11 2019

@author: Caio Cid Santiago
"""

import requests

def postdata(url:str, dictsensor:dict, idcolmeia: int):
    
    sensorpost = str()
    
    for key,val in dictsensor.items():
        sensorpost = sensorpost + "\"{}\":\"{}\",\n".format(key,val)
    
    sensorpost = sensorpost[:-2] + "\n" # Deleting last comma
    
    data = """{{
    \"id_colmeia\":\"{0}\",
    \"values\":{{
    {1}
    }}
    }}"""
    
    data = data.format(idcolmeia, sensorpost)
    
    #r = requests.post(url,json=data)
    
    return data
    #return r
    
def main():
    
    #idcolmeia = 50
    #url = "http://200.129.43.208:3000/coleta/add"
    
    dictsensor = {"temperatura":"38",
                  "umidade":"70"}
    dictdata = {"idcolmeia":"50",
                "values":dictsensor}
    
    r = requests.post("http://200.129.43.208:3000/coleta/add",json=dictdata)
    
    print(r.json)
    #print(r.text)
    
main()