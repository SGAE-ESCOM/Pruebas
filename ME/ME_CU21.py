import unittest
from selenium import webdriver
import time

class Editar_Aplicaciones:

    def __init__(self, driver):
        self.driver = driver

    def editar_aplicaciones(self):
        #Boton Editar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-aplicacion/div/div/div[2]/div/div[7]/button[1]').click()
        time.sleep(2)

        datos = ['Espñol','100','',2,40]
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        
        #Inputs
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
            time.sleep(1)

        #Grupo
        opc = [2]
        for x in range(0,len(opc)):
            self.driver.find_element_by_name('grupo').click()
            time.sleep(2)
            grupo = self.driver.find_elements_by_class_name('mat-option')[opc[x]]
            grupo.click()
            time.sleep(2)

        #Fecha
        day = [21]
        for x in range(0,len(day)):
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-dialog-container/modal-aplicacion/app-form-aplicacion/div/div[2]/div[1]/form/div[4]/input-fecha/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[3]').click()
            time.sleep(2)
            fecha = self.driver.find_elements_by_class_name('mat-calendar-body-cell')[day[x]]
            fecha.click()
            time.sleep(2)
        
        #Evaluaciones
        evaluaciones = [0]
        checkbox = self.driver.find_elements_by_class_name('mat-checkbox')
        for i in evaluaciones:
            checkbox[i].click()
            time.sleep(1)

        #Boton Agregar Modal
        self.driver.find_element_by_name('btnModalActualiza').click()
        time.sleep(2)