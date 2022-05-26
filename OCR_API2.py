import requests
import json
import base64


# def OCR():
#     url = 'https://api.ocr.space/parse/image'
#     head = {"apikey":"K82133132788957"}

#     data = {"url":"https://track.thailandpost.co.th/img/receipt.a7ee55db.jpg",
#             "OCREngine" : "1",
#             "language": "eng"}

#     r = requests.post(url,headers = head,data = data)

#     res = json.loads(r.text)
#     res = res["ParsedResults"][0]['ParsedText']
#     a = res.replace(' ','').replace('\n','')
#     print('\nkerry\n',kerry(a),'\n\nthaipost\n',thaipost(a))

def thai_OCR():
    url = 'https://api.aiforthai.in.th/ocr'
    head = {"apikey":"gvcUFh6InaQCTBUBc5vnIHxfgeI9Im8O"}
    file = {'uploadfile':open('./slip.jpg', 'rb')}

    a = json.loads(requests.post(url,headers = head,files=file).text)['Original'].replace(' ','').replace('\n','')
   
    print('kerry\n',kerry(a),'\n\nthaipost\n',thaipost(a))






def thaipost(a): # str format EI12345678901TH 
    ans = []

    for i in range(len(a)):
        op, ed = i,i+13
        if(ed >= len(a)):
            break
        
        if(a[op:op+2] == "EI" and a[ed-2:ed]=="TH"):
            ok = True
        else:
            ok = False   
                
        if(ok and a[op+2:ed-2].isdigit()):
            ans.append(a[op:ed])

    return ans

def kerry(a): # str format ABCD123456789
    ans = []
    for i in range(len(a)):
        op, ed = i,i+13
        if(ed >= len(a)):
            break
        
        ok=True
        for alp in a[op:op+4]:
            if(alp >= 'A' and alp <= 'Z'):
                continue
            else:
                ok=False
        
        for alp in a[op+4:ed]:
            if(alp >='0' and alp <= '9'):
                continue
            else:
                ok=False
        
        if(ok):
            ans.append(a[op:ed])

    return ans

thai_OCR()