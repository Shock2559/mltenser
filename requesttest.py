from requests import post, get

#print(post('http://localhost:8098/api', json={'text':'Установите и регулярно обновляйте антивирусное программное обеспечение на своем компьютере. Это поможет защитить ваши файлы от вредоносных программ'}).json())

#print(get('http://localhost:8099/send_message_bot', json={'message':'test message 3'}).json())

print(post('https://af48-195-239-50-94.ngrok-free.app/api', json={'text':'Установите и регулярно обновляйте антивирусное программное обеспечение на своем компьютере. Это поможет защитить ваши файлы от вредоносных программ'}).json())
