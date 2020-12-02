from selenium import webdriver
import time

#Registrar cuenta bancaria
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
        datos = ['Cuenta IPN', 'BBVA Bancomer',1234567887654321,'2800.00']
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos)):
            inp[i].send_keys(datos[i])
            time.sleep(1)
        #Btn Modal Agregar
        self.driver.find_element_by_name('btnModalAgregar').click()
        time.sleep(4)

    def registrar_campos_adicionales(self):

        self.driver.find_element_by_name('btnIrA').click()
        time.sleep(2)
        # btn Agregar datos
        self.driver.find_element_by_name('btnAgregarDatos').click()
        time.sleep(2)
        datos_adicionales =['','','','','Sucursal','CDMX']
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos_adicionales)):
            inp[i].send_keys(datos_adicionales[i])
            time.sleep(2)   
        #Btn Modal Agregar   
        self.driver.find_element_by_name('btnModalAgregar').click()
        time.sleep(2)





