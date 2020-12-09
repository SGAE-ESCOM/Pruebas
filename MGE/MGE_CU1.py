from selenium import webdriver
import time


class Definir_Etapas:

    def __init__(self, driver):
        self.driver = driver

    def definir_etapas(self):
        self.driver.find_element_by_name('btnIrA').click()
        time.sleep(2)

        #Etapas Necesarias
        etapas = [0,1,2,3]
        etapas_seleccionadas = self.driver.find_elements_by_class_name('mat-pseudo-checkbox')
        for i in etapas:
            etapas_seleccionadas[i].click()
            time.sleep(1)

        #Botones
        botones = ['btnPaso2','btnPaso3','btnFinalizar']
        for i in botones:
            btn = self.driver.find_element_by_name(i)
            btn.click()
            if i == 'btnPaso3':
                time.sleep(5)
            else:
                time.sleep(2)


        #Btn Modal Confirmar
        self.driver.find_element_by_name('btnConfiramar').click()
        time.sleep(5)