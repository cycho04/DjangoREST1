import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU5OTc4ODc2LCJqdGkiOiI1NzU0ODU5N2UwNWE0MTg0OTQ4ZTRmYTcxMGU0NTJkNSIsInVzZXJfaWQiOjF9.txT53k8eZ74gQ2Sss58RrGrlzVdh0AW3CiRIJbcDu7o'

r = requests.get('https://localhost:8000/paradigms', headers = headers)

print(r.text)