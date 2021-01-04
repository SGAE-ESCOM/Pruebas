import unittest
from selenium import webdriver
import time

class Editar_Secciones:

    def __init__(self, driver):
        self.driver = driver
    
    def editar_secciones_preguntas(self):
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
        #Busqueda
        def buscar(self):
            buscar = self.driver.find_element_by_id('txtBuscar')
            buscar.send_keys("Química")
            time.sleep(2)

        buscar(self)    
        datos = ['', 'Química I']
        btn_actualizar = self.driver.find_element_by_name('btnActualizar')
        btn_actualizar.click()
        time.sleep(2)
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
        time.sleep(2)
        self.driver.find_element_by_name('btnModalActualiza').click()
        time.sleep(1)
        #self.driver.refresh()
        time.sleep(3)
        print("... Test Case 'Editar Secciones' Successful ...")
        print("==============================================")


        
        