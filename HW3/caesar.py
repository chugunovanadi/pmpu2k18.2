from HW3.caesar_logic import encrypt, decrypt

p = input("Вы хотите зашифровать или расшифровать файл?")
text = input("Введите текст")
offset = int(input("Введите смещение"))
if p == 'e':
    print("Зашифрованный текст:", encrypt(offset, text))
elif p == 'd':
    print("Расшифрованный текст:", decrypt(offset, text))
else:
    print("Некорректный ответ")
