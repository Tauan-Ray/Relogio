from tkinter import Tk
from tkinter import *
import os
from PIL import Image, ImageTk
from time import strftime

# Cores
dark = '#201c1e'
light = '#ffffff'
font = '#6721b0'

# Criando janela do relógio
app = Tk()
app.title('Relógio')
app.geometry('600x328')
app.config(bg=dark)
app.resizable(False, False)


# Função para trocar o tema
def changeTheme():
    if app['bg'] == dark:
        app['bg'] = light
        darkMode_button['bg'] = light
        darkMode_button['image'] = iconLight
        hours['bg'] = light
        date['bg'] = light
        welcome['bg'] = light

    else:
        app['bg'] = dark
        darkMode_button['bg'] = dark
        darkMode_button['image'] = iconDark
        hours['bg'] = dark
        date['bg'] = dark
        welcome['bg'] = dark


# Função para dar bom dia/boa noite
def getWelcome():
    username = os.getlogin()
    if strftime('%H:%M:%S') >= '18:00:00' or strftime('%H:%M:%S') < '00:00:00':
        welcome.config(text='Boa noite ' + username)

    else:
        welcome.config(text='Bom dia ' + username)


# Função para obter a data
def getDate():
    currentDate = strftime('%a, %d %b %Y')
    date.config(text=currentDate)


# Função para obter as horas
def getHours():
    currentTime = strftime('%H:%M:%S')
    hours.config(text=currentTime)
    hours.after(1000, getHours)


# Criando icones do botão
iconDark = Image.open('Relógio/images/dark.png')
iconDark = iconDark.resize((26, 26))
iconDark = ImageTk.PhotoImage(iconDark)

iconLight = Image.open('Relógio/images/light.png')
iconLight = iconLight.resize((26, 26))
iconLight = ImageTk.PhotoImage(iconLight)


darkMode_button = Button(app, image=iconDark, command=changeTheme,
                         width=30, height=30, bg=dark, relief='flat', overrelief='ridge')
darkMode_button.pack()

welcome = Label(app, bg=dark, fg=font, font=('Ivy 17'))
welcome.pack(pady=3)

date = Label(app, bg=dark, fg=font, font=('Ivy 17'))
date.pack(pady=5)

hours = Label(app, bg=dark, fg=font, font=('Ivy 50 bold'))
hours.pack(pady=20)

# Chamando as funções
getWelcome()
getDate()
getHours()
app.mainloop()
