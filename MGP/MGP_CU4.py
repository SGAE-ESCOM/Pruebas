from selenium import webdriver
import time

class Editar_Cuenta:
    def __init__(self,driver):
        self.driver = driver
    
    #Método para editar una cuenta bancaria
    def editar(self):
        self.driver.find_element_by_name('btnIrA').click()
        time.sleep(2)
        #Boton Editar
        self.driver.find_element_by_name('btnActualizarInfoCuenta').click()
        time.sleep(2)
        
        #Editar inputs
        datos = ['Cuenta UNAM','CitiBanamex',987654321021]
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
            time.sleep(1)

        #Btn Actualizar
        self.driver.find_element_by_name('btnActualizarInfoCuenta').click()
        time.sleep(4)

        #Grupos Asociados
        permisos = [0,2]
        toggles = self.driver.find_elements_by_class_name('mat-slide-toggle-bar')
        print("Longitud de toggle",len(toggles))
        for i in permisos:
            toggles[i].click()
            time.sleep(1)
        #Btn actualizar grupos asociados
        self.driver.find_element_by_name('btnActualizarGruposAsociados').click()
        time.sleep(4)

        #Btn Regresar
        self.driver.find_element_by_name('btnRegresar').click()
        time.sleep(2)