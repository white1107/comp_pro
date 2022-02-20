import requests,bs4

url = 'https://atcoder.jp/contests/abc238/tasks/abc238_a'
res = requests.get(url)
# res = requests.get('https://ja.wikipedia.org/wiki/Python')

soup = bs4.BeautifulSoup(res.text, "html.parser")

res  = {} 
flag = 0

tmp = ""
tmt_txt = ''
for i in soup.find_all(['p','h2','h3','h4','ul']):
    if not flag and "概要" in i.get_text():
        flag = 1
    if flag:
        if '<h2' in str(i) or '<h3' in str(i):
            flag+=1
            if flag>=2 :
                res[tmp] = tmt_txt
            tmp = i.get_text()
            tmp = tmp.replace('\n','')
            tmp = tmp.replace('\r','')
            print(tmp)
            tmt_txt = ''
        else:
            tmt = i.get_text()
            tmt = tmt.replace('\n','')
            tmt = tmt.replace('\r','')
            tmt = tmt.replace('\u3000','')
            tmt_txt += " "+tmt
#             print('key',tmt)

print(res)