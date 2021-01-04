import unittest
from selenium import webdriver
import time

class Registrar_Aplicaciones:

    def __init__(self, driver):
        self.driver = driver

    def registrar_aplicaciones(self):
        #Boton ir Evaluación
        #self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
        #time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        #Boton ir a Aplicación
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[3]').click()
        time.sleep(2)

        #Boton Agregar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-aplicacion/div/div/div/button').click()
        time.sleep(2)

        datos = ['Test Química','10',1,30]
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        
        #Inputs de la app
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
            time.sleep(1)

        #Evaluaciones
        evaluaciones = [3]
        checkbox = self.driver.find_elements_by_class_name('mat-checkbox')
        for i in evaluaciones:
            checkbox[i].click()
            time.sleep(1)

        #Grupo
        opc = [0]
        for x in range(0,len(opc)):
            self.driver.find_element_by_name('grupo').click()
            time.sleep(2)
            grupo = self.driver.find_elements_by_class_name('mat-option')[opc[x]]
            grupo.click()
            time.sleep(2)

        #Fecha
        day = [15,18]
        for x in range(0,len(day)):
            if x == 0:
                self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-aplicacion/div/div/app-form-aplicacion/div/div/div[2]/div/form/div[7]/app-lista-grupos-aplicacion/form/div[2]/input-fecha/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button').click()
                time.sleep(2)
            else:
                self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-aplicacion/div/div/app-form-aplicacion/div/div/div[2]/div/form/div[7]/app-lista-grupos-aplicacion/form/div[3]/input-fecha/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button').click()
                time.sleep(2) 
            fecha = self.driver.find_elements_by_class_name('mat-calendar-body-cell')[day[x]]
            fecha.click()
            time.sleep(2)
        self.driver.find_element_by_name('agregarItem').click()
        time.sleep(2)
    

        #Boton Agregar Modal
        self.driver.find_element_by_name('btnModalAgregar').click()
        time.sleep(4)

        print("... Test Case 'Registro de Aplicaciones' Successful ...")
        print("=======================================================")

