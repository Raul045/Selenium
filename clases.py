from lib2to3.pgen2 import driver
from operator import index
from tabnanny import check
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

class pagina():
    global driver
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    driver.get('http://127.0.0.1:8000')
    def creardatos(nombre,apellido,correo,edad,genero,telefono,pais):
        archivo = open("usuarios.txt","w")
        archivo.write(nombre+','+apellido+','+correo+','+edad+','+genero+','+telefono+','+pais+'\n')
        archivo.close()

    def leertxt():
        global user
        global apellido
        global corr
        global edad
        global genero
        global telefono
        global Pais
        global gotdata
        with open('usuarios.txt') as users:
            for i, line in enumerate(users):
                usuario = (line)
                sep = ","
                dividir = usuario.split(sep)
                try:
                    gotdata = dividir[1]
                    user = dividir[0]
                    apellido = dividir[1]
                    corr = dividir[2]
                    edad = dividir[3]
                    genero = dividir[4]
                    telefono = dividir[5]
                    Pais = dividir[6]


                except IndexError:
                    gotdata='nulo' 

    def llenar():
        with open('formulario.json') as datos:
            rutas = json.load(datos)
            for ruta in rutas:
                in_nombre = driver.find_element(By.XPATH, ruta.get('input_nombre'))
                in_ape = driver.find_element(By.XPATH, ruta.get('input_apellido'))
                in_correo = driver.find_element(By.XPATH, ruta.get('input_correo'))
                in_edad = driver.find_element(By.XPATH, ruta.get('input_edad'))
                in_genero = driver.find_element(By.XPATH, ruta.get('input_genero'))
                in_telefono = driver.find_element(By.XPATH, ruta.get('input_telefono'))
                in_pais = driver.find_element(By.XPATH, ruta.get('input_pais'))    
                in_nombre.send_keys(user)
                time.sleep(2)
                in_ape.send_keys(apellido)
                time.sleep(2)
                in_correo.send_keys(corr)
                time.sleep(2)
                in_edad.send_keys(edad)
                time.sleep(2)
                in_genero.send_keys(genero)
                time.sleep(2)
                in_telefono.send_keys(telefono)
                time.sleep(2)
                in_pais.send_keys(Pais)
                time.sleep(2)
                boton = driver.find_element(By.XPATH, ruta.get('check_button'))
                boton.click()
                time.sleep(2)
                enviar = driver.find_element(By.XPATH, ruta.get('button'))
                enviar.click()
                
if __name__ == '__main__':
    pagina.leertxt()
    pagina.llenar()
