import requests
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
rget = requests.get(url)
rget_num = rget.text.split()[12].split('=')[0]
rpost = requests.post(url,data = {'v':eval(rget_num)})
print(rpost.text)
