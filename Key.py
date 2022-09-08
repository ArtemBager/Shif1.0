from tkinter import  *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.ttk import Radiobutton
from rsa import *
import os

global a, b, c

def f0():
    global a, b, c
    if a==1:
        random_key = os.urandom(8).hex()
        put0['state'] = 'normal'
        put0.delete(1.0, END)
        put0.insert(1.0, random_key)
        put0['state'] = 'disabled'
        put00['state'] = 'normal'
        put00.delete(1.0, END)
        put00['state'] = 'disabled'
    elif b==1:
        random_key = os.urandom(12).hex()
        put0['state'] = 'normal'
        put0.delete(1.0, END)
        put0.insert(1.0, random_key)
        put0['state'] = 'disabled'
        put00['state'] = 'normal'
        put00.delete(1.0, END)
        put00['state'] = 'disabled'
    elif c==1:
        random_key = os.urandom(16).hex()
        random_key0 = os.urandom(4).hex()
        put0['state'] = 'normal'
        put0.delete(1.0, END)
        put0.insert(1.0, random_key)
        put0['state'] = 'disabled'
        put00['state'] = 'normal'
        put00.delete(1.0, END)
        put00.insert(1.0, random_key0)
        put00['state'] = 'disabled'

def f1():
    razmer=int(combo.get())
    e=put2.get()
    d=put1.get()
    (public, priv)=newkeys(razmer)
    with open(e, 'wb') as e:
        e.write(public.save_pkcs1('PEM'))
        e.close()
    with open(d, 'wb') as d:
        d.write(priv.save_pkcs1('PEM'))
        d.close()

def vid1():
    global a, b, c
    a, b, c=0, 0, 0
    a=1
def vid2():
    global a, b, c
    a, b, c = 0, 0, 0
    b=1
def vid3():
    global a, b, c
    a, b, c = 0, 0, 0
    c=1

wind=Tk()
wind.geometry('450x200')
wind.title('Создание ключей RSA/AES/DES,3DES')
wind.resizable(False, False)


tab_cont=ttk.Notebook(wind)
tab0=ttk.Frame(tab_cont)
tab1=ttk.Frame(tab_cont)
tab2=ttk.Frame(tab_cont)
tab3=ttk.Frame(tab_cont)
tab_cont.add(tab0, text='Генератор DES/3DES/AES')
tab_cont.add(tab1, text='Генератор RSA')
tab_cont.add(tab2, text='Как пользоваться?')
tab_cont.add(tab3, text='О ключах RSA')
lt0=Label(tab0)
lt1=Label(tab1)
lt2=Label(tab2)
lt3=Label(tab3)
lt0.grid(column=0, row=0)
lt1.grid(column=0, row=0)
lt2.grid(column=0, row=0)
lt3.grid(column=0, row=0)
tab_cont.pack(expand=1, fill='both')

rad1 = Radiobutton(tab0, text='DES', value=1, command=vid1)
rad2 = Radiobutton(tab0, text='3DES', value=2, command=vid2)
rad3 = Radiobutton(tab0, text='AES', value=3, command=vid3)
rad1.grid(column=1, row=0)
rad2.grid(column=2, row=0)
rad3.grid(column=3, row=0)
put0=Text(tab0, width=35, height=1, state='disabled')
put0.place(relx=0.15, rely=0.5)
lbl0=Label(tab0, text='<--Метод шифровки').place(relx=0.35, rely=0)
put00=Text(tab0, width=35, height=1, state='disabled')
put00.place(relx=0.15, rely=0.3)
lbl00=Label(tab0, text='IV for AES').place(relx=0, rely=0.3)
lbl000=Label(tab0, text='key').place(relx=0, rely=0.5)

combo=Combobox(tab1, width=5)
combo['values'] = (256, 512, 1024, 2048, 4096)
combo.current(0)
combo.place(relx=0.4, rely=0)
put1=Entry(tab1, width=30)
put1.place(relx=0.4, rely=0.2)
put2=Entry(tab1, width=30)
put2.place(relx=0.4, rely=0.4)

lbl1=Label(tab1, text='Размер ключа (бит)').place(relx=0, rely=0)
lbl2=Label(tab1, text='Ссылка PrivateKey').place(relx=0, rely=0.2)
lbl3=Label(tab1, text='Ссылка PublicKey').place(relx=0, rely=0.4)

lblPS1=Label(tab2, text='Алгоритм RSA:').place(relx=0, rely=0)
lblPS2=Label(tab2, text='1)Создаем файлы для открытого ключа и закрытого .pem ').place(relx=0, rely=0.1)
lblPS3=Label(tab2, text='2)Указываем размер ключа').place(relx=0, rely=0.2)
lblPS4=Label(tab2, text='3)Указываем пути к файлам из п1').place(relx=0, rely=0.3)
lblPS5=Label(tab2, text='4) Нажимаем сгенерировать').place(relx=0, rely=0.4)
lblPS6=Label(tab2, text='Алгоритм для DES, 3DES, AES').place(relx=0, rely=0.5)
lblPS7=Label(tab2, text='1) Выбрать метод шифрования').place(relx=0, rely=0.6)
lblPS8=Label(tab2, text='2) Нажать сгенерировать').place(relx=0, rely=0.7)

lblN1=Label(tab3, text='Шифровать те сообщения, размер которых меньше ключа (RSA)').place(relx=0, rely=0)
lblN2=Label(tab3, text='Самый оптимальный ключ 2048 бит').place(relx=0, rely=0.1)
lblN3=Label(tab3, text='Время генерации ключа примерно от 0.01с до 72с').place(relx=0, rely=0.2)
lblN4=Label(tab3, text='Файл с закрытым ключем(PrivateKey) секретный!(RSA)').place(relx=0, rely=0.3)

btn1=Button(tab1, text='Сгенерировать', command=f1).place(relx=0.35, rely=0.75)
btn2=Button(tab0, text='Сгенерировать', command=f0).place(relx=0.35, rely=0.75)

wind.mainloop()