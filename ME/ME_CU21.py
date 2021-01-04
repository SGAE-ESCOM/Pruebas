import unittest
from selenium import webdriver
import time

class Editar_Aplicaciones:

    def __init__(self, driver):
        self.driver = driver

    def editar_aplicaciones(self):
        #Boton Editar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-aplicacion/div/div/div[2]/div/div[6]/button[1]').click()
        time.sleep(2)

        datos = ['Examen de Química','2',2,30]
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        
        #Inputs
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
            time.sleep(1)
        
        #Evaluaciones
        evaluaciones = [0,3]
        checkbox = self.driver.find_elements_by_class_name('mat-checkbox')
        for i in evaluaciones:
            checkbox[i].click()
            time.sleep(1)

        #Grupo
        #opc = [0]
        #for x in range(0,len(opc)):
        #    self.driver.find_element_by_name('grupo').click()
        #    time.sleep(2)
        #    grupo = self.driver.find_elements_by_class_name('mat-option')[opc[x]]
        #    grupo.click()
        #    time.sleep(2)

        #Fecha
        self.driver.find_element_by_name('editarItem').click()
        time.sleep(2)
        day = [2,3]
        for x in range(0,len(day)):
            if x == 0:
                inicio = self.driver.find_elements_by_class_name('mat-focus-indicator.mat-icon-button.mat-button-base')[1]
                #print("Longitud de btn calendario ",len(inicio))
                inicio.click()
                time.sleep(2)
            else:
                fin = self.driver.find_elements_by_class_name('mat-focus-indicator.mat-icon-button.mat-button-base')[2]
                fin.click()
                time.sleep(2) 
            fecha = self.driver.find_elements_by_class_name('mat-calendar-body-cell')[day[x]]
            fecha.click()
            time.sleep(2)
        self.driver.find_element_by_name('actualizarItem').click()
        time.sleep(2)
        

        #Boton Agregar Modal
        self.driver.find_element_by_name('btnModalActualiza').click()
        time.sleep(2)

        print("... Test Case 'Edición de Aplicaciones' Successful ...")
        print("=======================================================")