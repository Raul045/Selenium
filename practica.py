from email import generator
import time
from clases import pagina
# from lib2to3.pgen2 import driver
# from operator import index
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
while 1==1:
    print("*************************")
    print("-----Bienvenido------")
    print("Este es el menu...")
    print("1.- Ingresar datos del formulario")
    print("2.- Llenar el formulario de la pagina")
    print("3.- Almacenar datos de la pagina")
    opcion = input("Elige una opcion: ")
    print("")
    if opcion == '1':
        print("--------------")
        print("ingrese los datos:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo: ")
        edad = input("Edad: ")
        genero = input("Genero: ")
        telefono = input("telefono: ")
        pais = input("pais: ")
        pagina.creardatos(nombre,apellido,correo,edad,genero,telefono,pais)
    if opcion == '2':
        print("---------------")
        print("Llenado formulario...")
        pagina.leertxt()
        pagina.llenar()
    print("**************************\n")


# driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
# driver.get('http://127.0.0.1:8000')
# hola = "peroo"
# jala = "smn"

# with open('hola.json') as datos:
#     rutas = json.load(datos)
#     for ruta in rutas:
#         nombre = driver.find_element(By.XPATH, ruta.get('input_nombre'))
#         nombre.send_keys(hola)
#         time.sleep(2)
#         ape = driver.find_element(By.XPATH, ruta.get('input_apellido'))
#         ape.send_keys(jala)
# with open('pagina.txt') as file:
#             for i, line in enumerate(file):
#                 usuario = (line)
#                 sep = ","
#                 dividir = usuario.split(sep)
#                 try:
#                     input_nombre = dividir[0]
#                     ape = dividir[1]

#                     # correo = dividir[2]
#                     # edad = dividir[3]
#                     # genero = dividir[4]
#                     # telefono = dividir[5]
#                     # Pais = dividir[6]


#                 except IndexError:
#                     gotdata='nulo'
                
# archivo = open("datos1.txt","a")
# print("Hola Bienvenido")
# while 1==1:
#     opcion = input("Deseas registrar un usuario S/N: ")
#     if opcion == 'N' or opcion == 'n':
#         break
#     usuarios = input("Ingrese el nombre de usuario: ")
#     apellidos = input("Ingrese el apellido: ")
#     correos = input("Ingrese el correo: ")
#     edad = input("Ingresa la edad: ")
#     genero = input("Ingresa el genero: ")
#     telefono = input("Ingresa el telfono: ")
#     pais = input("Ingrese el pais: ")
#     archivo.write(usuarios+','+apellidos+','+correos+','+edad+','+genero+','+telefono+','+pais+'\n')
# archivo.close()

# pagina.leer()

# nombre = "Raul"
# password="12345"
 
# input_nombre = driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[1]/input') 
# input_nombre.send_keys(nombre)

# time.sleep(2)

# input_check=driver.find_element(By.XPATH, '/html/body/div/div[1]/form/div[8]/div/input')
# input_check.click()

# time.sleep(2)

# driver.close()
# palabra = "HTML Tutorial"

# buscar = driver.find_element(By.XPATH, '//input[@id="search2"]')

# buscar.send_keys(palabra)
# time.sleep(2)
# boton = driver.find_element(By.XPATH, '//button[@id="learntocode_searchbtn"]')
# boton.click()
# time.sleep(2)
# boton1 = driver.find_element(By.XPATH, '//html/body/div[4]/div/div[1]/a[4]')
# boton1.click()
# texto = driver.find_element(By.XPATH, '//html/body/div[7]/div[1]/div[1]/h2[2]').text
# print("------------------------")
# print(texto)
# print("------------------------")


# user = "8713958702"

# password="28dic2001"

# input_user = driver.find_element(By.XPATH, '//input[@name="username"]')
# input_password = driver.find_element(By.XPATH, '//input[@name="password"]')

# input_user.send_keys(user)
# input_password.send_keys(password)

# boton = driver.find_element(By.XPATH, '//class["login__form_action_container"]')

# boton.click()


