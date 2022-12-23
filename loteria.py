import os, sys, time, io
import random
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def banner():
 os.system("clear")
 print(f"""{color.cyan}
██╗      █████╗ ████████╗███████╗██████╗ ██╗ █████╗
██║     ██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║██╔══██╗
██║     ██║  ██║   ██║   █████╗  ██████╔╝██║███████║
██║     ██║  ██║   ██║   ██╔══╝  ██╔══██╗██║██╔══██║
███████╗╚█████╔╝   ██║   ███████╗██║  ██║██║██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{color.fin}""")
def contacto():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)

def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)


def inicio():
 banner()
 contacto()
 print(f"{color.amarillo}")
 print(f"{color.verde}[1]JUGAR")
 print(f"{color.amarillo}[2]AYUDA")
 print(f"{color.rojo}[0]SALIR{color.fin}")
 eleccion = input(f"{color.cyan}ELIJE UN NUNERO >> {color.fin}")
 if eleccion == "1":
  loteria()
 elif eleccion == "2":
  ayuda()
 elif eleccion =="0":
  os.system("clear")
 else:
  incorrecto()
  inicio()

def loteria():
 banner()
 contacto()
 print(f"""{color.morado}
             BIENVENIDO AL JUEGO DE LA LOTERIA
{color.fin}""")
 print(f"""{color.verde}
   TENDRAS QUE ELEGIR HASTA QUE NUMERO QUIERES JUGAR
 """)
 try:
  numero = int(input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}{color.fin}"))
  juego(numero)
 except:
  incorrecto()
  loteria()

def juego(numero):
 jugados = []
 banner()
 contacto()
 secreto=random.randint(0,numero)
 while True:
  banner()
  contacto()
  print()
  print(f"{color.amarillo}NUMEROS JUGADOS {color.rojo}",jugados)
  print(f"""

                     {color.morado}PRUEBA SUERTE
""")
  eleccion = int(input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin}"))
  if eleccion != secreto:
   jugados.append(eleccion)
  else:
   ganar(secreto)
   break

def ganar(secreto):
 banner()
 contacto()
 print(f"""{color.amarillo}

 ██████╗  █████╗ ███╗  ██╗ █████╗  ██████╗████████╗███████╗
██╔════╝ ██╔══██╗████╗ ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║  ██╗ ███████║██╔██╗██║███████║╚█████╗    ██║   █████╗
██║  ╚██╗██╔══██║██║╚████║██╔══██║ ╚═══██╗   ██║   ██╔══╝
╚██████╔╝██║  ██║██║ ╚███║██║  ██║██████╔╝   ██║   ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝{color.fin}
""")
 print(f"""{color.verde}
              NUMERO GANADOR {secreto}
""")
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] JUGAR OTRA VEZ")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  inicio()
 elif var == "0":
  os.system("clear")
 else:
  incorrecto()
  ganar(secreto)



def ayuda():
 banner()
 contacto()
 print(f"""

  {color.morado}NUESTRO OBJETIVO SERA ADIVINAR EL NUMERO.{color.verde}

  ELEGIREMOS HASTA QUE NUMERO QUEREMOS JUGAR
  Y SE ASIGANRA AL AZAR UN NUMERO ALEATORIO
  ENTRE EL 0 Y EL NUMERO ELEGIDO
  AMBOS INCLUIDOS
  MUCHA SUERTE
""")
 input(f"{color.cyan} PULSA CUALQUIER TECLA PARA CONTINUAR >>>{color.fin}")
 inicio()

inicio()
