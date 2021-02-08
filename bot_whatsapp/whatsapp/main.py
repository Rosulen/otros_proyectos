import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("/home/angie/Git/proyectos_python/bot_whatsapp/whatsapp/emoji.png", confidence = .6)
x = position1[0]
y = position1[1]

# Obtener mensaje
def get_message():
    global x, y

    position = pt.locateOnScreen("emoji.png", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration = .05)
    pt.moveTo(x + 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    mensaje_whats = pyperclip.paste()
    pt.click()
    print("Mesaje: " + mensaje_whats)

    return mensaje_whats

def respuesta(mensaje):
    global x, y

    position = pt.locateOnScreen("emoji.png", confidence = .6)
    x = position[0]
    y = position[1]

    pt.moveTo(x + 200, y + 20, duration = .5)
    pt.click()
    pt.typewrite(mensaje, interval = .01)

    position2 = pt.locateOnScreen("enviar.png", confidence = .6)
    x = position2[0]
    y = position2[1]
    pt.moveTo(x + 550, y + 560, duration = .5)
    pt.click()



    #pt.typewrite("\n", interval=.01)

def procesar_respuesta(mensaje):

    random_no = random.randrange(3)
    if "?" in str(mensaje).lower():
        return "Nada de preguntas, solo besame"
    else:
        if random_no == 0:
            return "La verdad no se"
        elif random_no == 1:
            return "¿Que fue? :v"
        else:
            return "Tengo mucha hambre :("
    
procesando_respuesta = procesar_respuesta(get_message())
respuesta(procesando_respuesta)

