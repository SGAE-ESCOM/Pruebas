from ME_CU15 import *
import unittest
from selenium import webdriver
import time

class Editar_Preguntas:

    def __init__(self, driver):
        self.driver = driver
    
    def editar_preguntas(self):
        #Boton ir Evaluación
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
        time.sleep(2)
        #Boton ir a Gestinar Evaluacion
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]/div').click()
        time.sleep(2)
       #Apartir de aqui inicia el metodo
       #Boton ir a preguntas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-gestionar-evaluacion/div/div/div/app-cards/div/div[1]').click()
        time.sleep(2)

        #Boton de ir a gestionar temas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[2]/button[1]').click()
        time.sleep(2)

        #Boton ir a gestionar preguntas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[3]/button[1]').click()
        time.sleep(2)

        #Boton Editar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/form/div[3]/app-crear-simulador/form/div[2]/div[3]/div/button[1]').click()
        time.sleep(2)

        #Enunciado
        enunciado  =  self.driver.find_element_by_name('enunciado')
        enunciado.clear()
        time.sleep(1)
        enunciado.send_keys('Ciencia que se encarga del estudio de la materia.')
        time.sleep(1)

        #Imagen Enunciado
        imagen = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[3]/div/div/mat-form-field/div/div[1]/div[1]/ngx-mat-file-input/input')
        imagen.send_keys(r"C:\Users\Andrez\Pictures\FERMAT\images.jpg")

        #Editar Respuestas
        er = Editar_Preguntas_Respuestas(self.driver)
        er.editar_preguntas_respuestas()

        #Respuesta
        permisos = [2]
        for x in range(0,len(permisos)):
            self.driver.find_element_by_name('respuesta').click()
            time.sleep(2)
            opc_per = self.driver.find_elements_by_class_name('mat-option')[permisos[x]]
            opc_per.click()
            time.sleep(2)
        self.driver.find_element_by_name('btnModalActualiza').click()
        time.sleep(3)
