from requests import post
print(post('http://localhost:8098/api', json={'text':'Живи так чтобы увидеть, как ты становишься сильнее и живешь счастливой, полноценной жизнью'}).json())
