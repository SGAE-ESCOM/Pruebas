from selenium import webdriver
import time

class Registrar_Cuenta:
    def __init__(self,driver):
        self.driver = driver
    
    def registrar(self):
        #Gestion de cuentas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-pagos/div/app-cards/div/div[1]').click()
        time.sleep(2)
        #Dar click en Agregar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-gestionar-cuentas/div[2]/div/div/div/button').click()
        time.sleep(2)
        #Input
        datos = ['Cuenta IPN', 'BBVA Bancomer',1234567887654321]
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos)):
            inp[i].send_keys(datos[i])
            time.sleep(1)
    
        #Agregar
        self.driver.find_element_by_name('btnModalAgregar').click()
        time.sleep(4)
