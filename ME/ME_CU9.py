import unittest
from selenium import webdriver
import time

class Visualizar_Temas:

    def __init__(self, driver):
        self.driver = driver

    def visualizar_temas(self):
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
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[2]/button[1]').click()
        #time.sleep(2)

        #Busqueda
        def buscar(self):
            buscar = self.driver.find_element_by_id('txtBuscar')
            buscar.send_keys("Atomos")
            time.sleep(3)
            buscar.clear()
        
        def eliminar(self):
            buscar(self)
            self.driver.find_element_by_name('btnEliminar').click()
            time.sleep(2)
            self.driver.find_element_by_name('btnConfiramar').click()
            time.sleep(4)
            #confirmar = [-1]
            #ok = self.driver.find_elements_by_class_name('swal2-confirm mat-button')
            #print(" longitud : ",len(ok))
            #for i in confirmar:
            #    ok[i].click()
            #time.sleep(2)

        eliminar(self)