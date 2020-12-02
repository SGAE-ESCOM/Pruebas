from selenium import webdriver
import time

#Editar una cuenta bancaria
class Editar_Cuenta:
    def __init__(self,driver):
        self.driver = driver
    
    #Método para editar una cuenta bancaria
    def editar(self):
        #Boton Editar
        self.driver.find_element_by_name('btnActualizarInfoCuenta').click()
        time.sleep(4)
        
        #Editar inputs
        datos = ['Cuenta UNAM','CitiBanamex',987654321021,'3500.00']
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos)):
            inp[i].clear()
            inp[i].send_keys(datos[i])
            time.sleep(2)

        #Btn Actualizar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-revisar-cuenta/div/div[2]/div/div/div[2]/form/div[2]/div/button[2]').click()
        time.sleep(4)

        #Grupos Asociados
        permisos = [0,2]
        toggles = self.driver.find_elements_by_class_name('mat-slide-toggle-bar')
        #print("Longitud de toggle",len(toggles))
        for i in permisos:
            toggles[i].click()
            time.sleep(2)
            
        #Btn actualizar grupos asociados
        self.driver.find_element_by_name('btnActualizarGruposAsociados').click()
        time.sleep(4)


    def editar_campos_adicionales(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-revisar-cuenta/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tr/td[1]/button').click()
        time.sleep(2)
        datos_adicionales =['','','','','','Titular','Christian Cervantes']
        inp = self.driver.find_elements_by_class_name('mat-input-element')
        for i in range(0,len(datos_adicionales)):
            if( i == 5 or i == 6):
                inp[i].clear()
            inp[i].send_keys(datos_adicionales[i])
            time.sleep(2)   
        #Btn Modal Aactualizar   
        self.driver.find_element_by_name('btnModalActualizar').click()
        time.sleep(4)

        #Btn Regresar
        self.driver.find_element_by_name('btnRegresar').click()
        time.sleep(2)