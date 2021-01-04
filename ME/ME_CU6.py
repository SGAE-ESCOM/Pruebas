import unittest
from selenium import webdriver
import time

class Visualizar_Secciones:

    def __init__(self, driver):
        self.driver = driver

    def visualizar_secciones(self):
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
            buscar.send_keys("Historia")
            time.sleep(2)
            buscar.clear()
        
        def eliminar(self):
            buscar(self)
            self.driver.find_element_by_name('btnEliminar').click()
            time.sleep(2)
            self.driver.find_elements_by_class_name('swal2-confirm.mat-button.mat-button-base.mat-danger')[0].click()
            time.sleep(2)
            self.driver.find_elements_by_class_name('swal2-confirm.mat-button.mat-button-base.mat-info')[0].click()
            time.sleep(2)
            

        eliminar(self)
        print("... Test Case 'Visualizar Secciones' Successful ...")
        print("==============================================")
        
