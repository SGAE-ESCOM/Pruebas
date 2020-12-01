import unittest
from selenium import webdriver
import time

class Registrar_Temas:

    def __init__(self, driver):
        self.driver = driver
    
    def registrar_temas(self):
        #Boton ir Evaluación
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
        #time.sleep(2)
        #Boton ir a Gestinar Evaluacion
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]/div').click()
        #time.sleep(2)
       #Apartir de aqui inicia el metodo
       #Boton ir a preguntas
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-gestionar-evaluacion/div/div/div/app-cards/div/div[1]').click()
        #time.sleep(2)

        #Boton de ir a gestionar temas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[2]/button[1]').click()
        time.sleep(2)

        datos = ['Reacciones Químicas','Elementos']
        inp = []
        btn_agregar = self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[1]/div[2]/div/div/button')
        for i in range(0,len(datos)):
            btn_agregar.click()
            time.sleep(1)
            inp.append(self.driver.find_element_by_name('nombre'))
            time.sleep(1)
            btn_agregar_modal = self.driver.find_element_by_name('btnModalAgregar')
            inp[i].send_keys(datos[i])
            time.sleep(2)
            btn_agregar_modal.click()
            time.sleep(2)
        