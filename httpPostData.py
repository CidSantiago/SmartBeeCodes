# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:40:11 2019

@author: Caio Cid Santiago
"""

import requests

def postdata(url:str, dictdata:dict):
    
    r = requests.post(url,json=dictdata)
    
    return r
    
def main():
    
    idcolmeia = 50
    url = "http://200.129.43.208:3000/coleta/add"
    #url = "http://httpbin.org/post"
    
    dictsensor = {"temperatura":"38",
                  "umidade":"70"}
    dictdata = {"id_colmeia":"{}".format(idcolmeia),
                "values":dictsensor}
    
    r = postdata(url, dictdata);
    
    print(r.text)
    
main()