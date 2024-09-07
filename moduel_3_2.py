def send_email(message, recipient, *,sender = "university.help@gmail.com"):
    domen = ['.com', '.ru', '.net']
    while True:
        if "@" in recipient and "@" in sender:
            a = True
        else:
            a = False
        if any(word in recipient for word in domen):
            b = True
        else:
            b = False
        if any(word_1 in sender for word_1 in domen):
            c = True
        else:
            c = False
        if a == False or b == False or c == False:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
            break
        if sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            break
        if sender != "university.help@gmail.com":
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса{sender} на адрес {recipient}.')
            break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')