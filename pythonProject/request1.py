"""import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)"""
"""import requests

#the required first parameter of the 'delete' method is the 'url':
x = requests.delete('https://w3schools.com/python/demopage.php')

#print the response text (the content of the requested file):
print(x.text)"""
"""import requests

url = 'https://www.w3schools.com/python'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)
"""
"""import requests

url = 'https://www.w3schools.com/python'

x = requests.post(url)

#print the response text (the content of the requested file):

print(x.text)"""