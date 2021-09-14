import requests
import pytest

#GET
r = requests.get('https://api.github.com/events')
print(r)

# Post
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r)

#Params in URL
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r)

#Printing Response content
print(r.text)


# Data in POST
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

# Get Status code
print(r.status_code)


def testGoogleGET():
	r = requests.get("https://google.com")
	assert r.status_code == 200
