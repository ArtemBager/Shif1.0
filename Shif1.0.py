# цель реализовать несколько методов шифровки сообщений используя GUI

#Дохера библиотек
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tkinter import  *
from rsa import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from des import DesKey

global a,b,c

#ФУНКЦИИ
#Шифруемся
def zash():
    global a, b, c
    if a==1:                                         #RSA шифровка
        f = PbK.get()
        with open(f, 'rb') as f:
            key = PublicKey.load_pkcs1(f.read())
            f.close()
        soob = soobsh.get(1.0, END)
        zashifr = encrypt(soob.encode('utf8'), key)
        zashifr1['state'] = 'normal'
        zashifr1.delete(1.0, END)
        zashifr1.insert(1.0, zashifr.hex())
        zashifr1['state'] = 'disabled'
    elif b==1:                                      #AES шифровка
        soob = soobsh.get(1.0, END)
        bytext = bytes(soob, 'utf-8')
        key = pad(bytes(Klych.get(), 'utf-8'), AES.block_size)
        iv1 = pad(bytes(iv.get(), 'utf-8'), AES.block_size)
        padded = pad(bytext, AES.block_size)
        AES_obj = AES.new(key, AES.MODE_CBC, iv1)
        shif = AES_obj.encrypt(padded).hex()
        zashifr1['state'] = 'normal'
        zashifr1.delete(1.0, END)
        zashifr1.insert(1.0, shif)
        zashifr1['state'] = 'disabled'
    elif c==1:                                      #DES шифровка
        soob = soobsh.get(1.0, END)
        soob=bytes(soob, 'utf-8')
        key=Klych.get()
        key = bytes(key, 'utf-8')
        key0 = DesKey(key)
        b = key0.encrypt(soob, padding=True).hex()
        zashifr1['state'] = 'normal'
        zashifr1.delete(1.0, END)
        zashifr1.insert(1.0, b)
        zashifr1['state'] = 'disabled'

#Расшифровываемся
def rashif():
    global a, b, c
    if a==1:                                            #RSA расшифровка
        f = PrK.get()
        with open(f, 'rb') as f:
            keyD = PrivateKey.load_pkcs1(f.read())
            f.close()
        shifr = shif.get(1.0, END)
        shifr = bytes.fromhex(shifr)
        rashifr = decrypt(shifr, keyD)
        rashifr1['state'] = 'normal'
        rashifr1.delete(1.0, END)
        rashifr1.insert(1.0, rashifr.decode('utf8'))
        rashifr1['state'] = 'disabled'
    elif b==1:                                          #AES расшифровка
        shifr = shif.get(1.0, END)
        shifr = bytes.fromhex(shifr)
        key = pad(bytes(Klych.get(), 'utf-8'), AES.block_size)
        iv1 = pad(bytes(iv.get(), 'utf-8'), AES.block_size)
        AES_obj=AES.new(key, AES.MODE_CBC, iv1)
        raw=AES_obj.decrypt(shifr)
        extract=unpad(raw, AES.block_size)
        rashifr1['state'] = 'normal'
        rashifr1.delete(1.0, END)
        rashifr1.insert(1.0, extract)
        rashifr1['state'] = 'disabled'

    elif c==1:
        shifr = shif.get(1.0, END)                      #DES расшифровка
        shifr = bytes.fromhex(shifr)
        key = Klych.get()
        key = bytes(key, 'utf-8')
        key0 = DesKey(key)
        rashifr= key0.decrypt(shifr, padding=True).decode('utf8')
        rashifr1['state'] = 'normal'
        rashifr1.delete(1.0, END)
        rashifr1.insert(1.0, rashifr)
        rashifr1['state'] = 'disabled'

#Чистим ввод/вывод, активируем кнопки
def obhee():
    rashifr1['state'] = 'normal'
    rashifr1.delete(1.0, END)
    rashifr1['state'] = 'disabled'
    zashifr1['state'] = 'normal'
    zashifr1.delete(1.0, END)
    zashifr1['state'] = 'disabled'
    soobsh.delete(1.0, END)
    shif.delete(1.0, END)
    btn1['state'] = 'normal'
    btn2['state'] = 'normal'

#Функции определения метода шифрования
def vid1():
    global a, b, c
    a, b, c=0, 0, 0
    a=1
    obhee()
def vid2():
    global a, b, c
    a, b, c = 0, 0, 0
    b=1
    obhee()
def vid3():
    global a, b, c
    a, b, c = 0, 0, 0
    c=1
    obhee()

#Тело окна
wind=Tk()
wind.geometry('550x250')
wind.title('Shif')
wind.resizable(False, False)

#Вкладки сверху
tab_cont=ttk.Notebook(wind)
tab1=ttk.Frame(tab_cont)
tab2=ttk.Frame(tab_cont)
tab3=ttk.Frame(tab_cont)
tab4=ttk.Frame(tab_cont)
tab5=ttk.Frame(tab_cont)
tab_cont.add(tab1, text='Шифратор')
tab_cont.add(tab2, text='Дешифратор')
tab_cont.add(tab3, text='Метод шифрования')
tab_cont.add(tab4, text='Как пользоваться')
tab_cont.add(tab5, text='О методах шифровки')
lt1=Label(tab1)
lt2=Label(tab2)
lt3=Label(tab3)
lt4=Label(tab4)
lt5=Label(tab5)
lt1.grid(column=0, row=0)
lt2.grid(column=0, row=0)
lt3.grid(column=0, row=0)
lt4.grid(column=0, row=0)
lt5.grid(column=0, row=0)
tab_cont.pack(expand=1, fill='both')

#Вкладка шифратор
soobsh=Text(tab1,width=50, height=4, padx=0, pady=0, wrap=WORD)
soobsh.place(relx=0, rely=0)
zashifr1=Text(tab1, width=50, height=4, padx=0, pady=0, state='disabled')
zashifr1.place(relx=0, rely=0.5)
#Дешифратор
shif=Text(tab2,width=50, height=4, padx=0, pady=0, wrap=WORD)
shif.place(relx=0, rely=0)
rashifr1=Text(tab2, width=50, height=4, padx=0, pady=0, state='disabled')
rashifr1.place(relx=0, rely=0.5)
#Тексты
lbl1=Label(tab1, text='Ваше сообщение').place(relx=0.75, rely=0)
lbl2=Label(tab1, text='Шифротекст').place(relx=0.75, rely=0.5)
lbl3=Label(tab2, text='Зашифрованное \n сообщение').place(relx=0.75, rely=0)
lbl4=Label(tab2, text='Расшифровка').place(relx=0.75, rely=0.5)
#Кнопочки
btn1=Button(tab1, text='Зашифровать', command=zash, state='disabled')
btn1.place(relx=0.26, rely=0.35)
btn2=Button(tab2, text='Расшифровать', command=rashif, state='disabled')
btn2.place(relx=0.26, rely=0.35)
#Методы шифровки
rad1 = Radiobutton(tab3, text='RSA', value=1, command=vid1)
rad2 = Radiobutton(tab3, text='AES', value=2, command=vid2)
rad3 = Radiobutton(tab3, text='DES', value=3, command=vid3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

#Необходимые данные для шифровки
#RSA
PrK=Entry(tab3, width=50)
PrK.place(relx=0, rely=0.7)
PbK=Entry(tab3, width=50)
PbK.place(relx=0, rely=0.8)
privatekey=Label(tab3, text='Ссылка на privatekey для RSA', padx=0, pady=0).place(relx=0.6, rely=0.7)
publickey=Label(tab3, text='Ссылка на publickey для RSA', padx=0, pady=0).place(relx=0.6, rely=0.8)
#DES
Klych=Entry(tab3, width=50)
Klych.place(relx=0, rely=0.4)
LBK=Label(tab3, text='Ключ DES', padx=0, pady=0).place(relx=0.6, rely=0.4)
#AES
iv=Entry(tab3, width=50)
iv.place(relx=0, rely=0.6)
KlychAES=Entry(tab3, width=50)
KlychAES.place(relx=0, rely=0.5)
LBKA=Label(tab3, text='Ключ AES', padx=0, pady=0).place(relx=0.6, rely=0.5)
LBKI=Label(tab3, text='iv AES', padx=0, pady=0).place(relx=0.6, rely=0.6)

#Как пользоваться
inf1=Label(tab4, text='1) Выбрать метод шифрования').place(relx=0, rely=0)
inf2=Label(tab4, text='2) Узнать данные для метода через генератор ключей или придумать самому(кроме RSA)').place(relx=0, rely=0.08)
inf3=Label(tab4, text='3) Указать необходимые данные для метода шифрования').place(relx=0, rely=0.16)
inf4=Label(tab4, text='4) Вводим сообщение и нажимаем зашифровать').place(relx=0, rely=0.24)
inf5=Label(tab4, text='Или Вставляем зашифрованное сообщение и нажимаем расшифровать').place(relx=0, rely=0.32)

#О методах шифрования
infS1=Label(tab5, text='RSA ассиметричный шифр (имеет открытый и закрытый ключи, последний секретный)').place(relx=0, rely=0)
infS2=Label(tab5, text='Этот алгоритм достаточно криптостойкий, но есть один байт зная который можно взломать').place(relx=0, rely=0.08)
infS3=Label(tab5, text='AES DES 3DES симметричный ключ (имеет один закрытый ключ который секретен)').place(relx=0, rely=0.16)
infS4=Label(tab5, text='DES и 3DES выбирается автоматически в зависимости от размера ключа').place(relx=0, rely=0.24)
infS5=Label(tab5, text='DES - 16байт, 3DES - 24байта').place(relx=0, rely=0.32)

wind.mainloop()