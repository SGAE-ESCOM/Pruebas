from selenium import webdriver
import time



class Subir_Evidencia:

    def __init__ (self, driver):
        self.driver = driver
    
    def subir_evidencia(self):
        #Seleccionar pagos
        self.driver.find_elements_by_class_name('mat-ripple.card.card-hover.mat-elevation-z2.bd-callout.bd-callout-primary.pt-2.pb-4.ng-tns-c117-8')[2].click()
        time.sleep(2)

        #Ver formato
        self.driver.find_elements_by_name('btnIrA')[0].click()
        time.sleep(2)

        self.driver.find_element_by_name('tipoDato').click()
        self.driver.find_elements_by_class_name('mat-option')[0].click()
        time.sleep(3)


        #Subir Evidencia
        self.driver.find_element_by_name('btnIrAEvidenciaPago').click()
        time.sleep(2)

        s = self.driver.find_element_by_id('fileDropRef')
        s.send_keys(r"C:\Users\Andrez\OneDrive - Instituto Politecnico Nacional\ESCOM\MOVILIDAD\LETONIA\PASAPORTE.pdf")
        time.sleep(10)

        #Enviar evidencia
        self.driver.find_element_by_name('btnEnviarArchivos').click()
        time.sleep(2)
        
        print("\n \n ... Test Case:  Successful ! ....\n \n")
