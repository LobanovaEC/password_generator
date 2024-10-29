import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuatio =  "'!#$%&*+-=?@^_"
chars = ''
kol = int(input("Количество паролей для генерации - "))
long = int(input('Длина одного пароля в символах - '))
num = input('Включать ли цифры? - Да=д Нет=н - ')
propis = input('Включать ли прописные буквы - Да=д Нет=н - ')
stoka = input('Включать ли строчные буквы - Да=д Нет=н - ')
simvol = input('Включать ли символы - !#$%&*+-=?@^_ Да=д Нет=н - ')
exception = input('Исключать ли неоднозначные символы - il1Lo0O- Да=д Нет=н - ')
if num.lower() == 'д':
    chars += digits
if propis.lower() == 'д':
    chars += uppercase_letters
if stoka.lower() == 'д':
    chars += lowercase_letters
if simvol.lower() == 'д':
    chars += punctuatio
if exception.lower() == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i , '')
def generate_password(long, chars):
    password = ''
    for j in range(long):
        password += random.choice(chars)
    return password
for _ in range(kol):
    print(generate_password(long, chars))



