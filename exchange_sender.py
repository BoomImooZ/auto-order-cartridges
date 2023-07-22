import sub_exchange


email = sub_exchange.preform_letter(0,quantity=10)
#print(email.to_recipients,'\r\nТема: ',email.subject,'\r\nТело: ',email.body) # Выведт пример того что будет собрано
email.send()