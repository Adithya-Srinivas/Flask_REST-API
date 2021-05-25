import requests

BASE = 'http://127.0.0.1:5000/'

data = [{'name': 'how to eat', 'views': 100000, 'likes': 900},
        {'name': 'how to study', 'views': 90000, 'likes': 80},
        {'name': 'how to walk easily', 'views': 9000000, 'likes': 8900}]

for i in range(len(data)):
    response_put = requests.put(BASE + 'video/' + str(i), data[i])
    print(response_put.json())

input()

response_del = requests.delete(BASE + 'video/1')
print(response_del)

input()

response_get  = requests.get(BASE+ 'video/2')
print(response_get.json())