import unittest
from selenium import webdriver
import time

class Visualizar_Aplicaciones:

    def __init__(self, driver):
        self.driver = driver

    def visualizar_aplicaciones(self):
        
        def eliminar(self):
            self.driver.find_elements_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-aplicacion/div/div/div[2]/div/div[6]/button[2]')[0].click()
            time.sleep(2)
            self.driver.find_elements_by_class_name('swal2-confirm.mat-button.mat-button-base.mat-danger')[0].click()
            time.sleep(2)
            self.driver.find_elements_by_class_name('swal2-confirm.mat-button.mat-button-base.mat-info')[0].click()
            time.sleep(2)

        eliminar(self)
        print("... Test Case 'Visualizar  Aplicaciones' Successful ...")
        print("=======================================================")