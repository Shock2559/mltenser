from requests import post

#print(post('http://localhost:8098/topic', json={'q1': 4, 'q2': 2, 'q3': 3, 'q4': 1}).json())
print(post('https://af48-195-239-50-94.ngrok-free.app/topic', json={'q1': 4, 'q2': 2, 'q3': 3, 'q4': 1}).json())
