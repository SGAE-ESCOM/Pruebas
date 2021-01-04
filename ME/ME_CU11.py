import unittest
from selenium import webdriver
import time

class Editar_Temas:

    def __init__(self, driver):
        self.driver = driver
    
    def editar_temas(self):
        #Boton ir Evaluación
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
        #time.sleep(2)
        #Boton ir a Gestinar Evaluacion
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]/div').click()
        #time.sleep(2)
       #Apartir de aqui inicia el metodo
       #Boton ir a preguntas
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-gestionar-evaluacion/div/div/div/app-cards/div/div[1]').click()
        time.sleep(2)

        #Boton de ir a gestionar temas
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[2]/button[1]').click()
        #time.sleep(2)
        buscar = self.driver.find_element_by_id('txtBuscar')
        buscar.send_keys("Elementos")
        time.sleep(2)
        buscar.clear()
        time.sleep(2)

        
        datos = ['', 'Elementos y Compuestos']
        btn_actualizar = self.driver.find_element_by_name('btnActualizar')
        btn_actualizar.click()
        time.sleep(2)
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
        time.sleep(2)
        self.driver.find_element_by_name('btnModalActualiza').click()
        time.sleep(4)
        print("... Test Case 'Editar Temas' Successful ...")
        print("==============================================")
