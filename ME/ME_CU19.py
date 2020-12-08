import unittest
from selenium import webdriver
import time

class Visualizar_Aplicaciones:

    def __init__(self, driver):
        self.driver = driver

    def visualizar_aplicaciones(self):
        
        def eliminar(self):
            self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-aplicacion/div/div/div[2]/div/div[7]/button[2]').click()
            time.sleep(4)
            #self.driver.find_element_by_name('btnConfiramar').click()
            #time.sleep(3)

        eliminar(self)