

import requests as req
import json

url = 'https://api.ocr.space/parse/image'
head = {"apikey":"K82133132788957"}

data = {"url":"https://obs.line-scdn.net/r/myhome/h/5043cd15f3f02b30964d83f6c27c725d/w960",
        "OCREngine" : "2",
        "language": "eng"}

r = req.post(url,headers = head,data = data)

res = json.loads(r.text)
res = res["ParsedResults"]
raw_res = res[0]['ParsedText']

print(type(raw_res))

print(len(raw_res))

# res_s1 = raw_res.split(' ',7)
# res_s2 = res_s1[7].split('\n')

# print(res_s2[12])

s_res = raw_res.split()
op = 0
ed = 0
INDEX = 0
status = 0
checkpoint = []

for i in s_res:
    try:    
        if(i[0:2] == "EI"):
            op = INDEX
            status=1
    except Exception:
        pass
    try:
        if(i[len(i)-2:len(i)] == "TH"):
            ed = INDEX
            checkpoint.append([op,ed])
            status=0
    except Exception:
        pass

    INDEX += 1

for point in checkpoint:
    op,ed = point
    ans = ""
    for i in range(op,ed+1):
        ans= ans+s_res[i]
    
    print(ans)