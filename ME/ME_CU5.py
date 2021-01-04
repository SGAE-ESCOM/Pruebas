import unittest
from selenium import webdriver
import time

class Visualizacion_GestionEvaluacion:
    def __init__(self, driver):
        self.driver = driver

    def visualizacion(self):
        #Boton ir a Gestinar Evaluacion
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]/div').click()
        time.sleep(2)
        num = [10,11]
        for i in num:
            button = self.driver.find_elements_by_class_name('mat-icon')
            button[i].click()
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
        print("... Test Case 'Indice Gestión Evaluación' Successful ...")
        print("==============================================")



