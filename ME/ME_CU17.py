import unittest
from selenium import webdriver
import time

class Registrar_Evaluaciones:

    def __init__(self, driver):
        self.driver = driver

    def registrar_evaluaciones(self):
        #Boton ir Evaluación
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
        time.sleep(2)
        #Boton ir a Gestinar Evaluacion
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]/div').click()
        time.sleep(2)
       
        #Apartir de aqui inicia el metodo
        #Boton ir a Evaluación
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-gestionar-evaluacion/div/div/div/app-cards/div/div[2]').click()
        time.sleep(2)


        #Boton de ir a gestionar temas
        self.driver.find_element_by_name('btnAgregar').click()
        time.sleep(2)

        #Nombre 
        self.driver.find_element_by_name('nombre').send_keys('Químina Inorganica')
        time.sleep(2)

        #Temas
        permisos = [1,2,3,4,5]
        checkbox = self.driver.find_elements_by_class_name('mat-checkbox')
        for i in permisos:
            checkbox[i].click()
            time.sleep(1)
        
        #Agregar
        self.driver.find_element_by_name('btnModalAgregar').click()
        time.sleep(2)

        