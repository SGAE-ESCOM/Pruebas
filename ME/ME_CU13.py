import unittest
from selenium import webdriver
import time

class Registrar_Preguntas:

    def __init__(self, driver):
        self.driver = driver
    
    def registrar_preguntas(self):
        #Boton ir Evaluación
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
        time.sleep(2)
        #Boton ir a Gestinar Evaluacion
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]/div').click()
        time.sleep(2)
       #Apartir de aqui inicia el metodo
       #Boton ir a preguntas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-gestionar-evaluacion/div/div/div/app-cards/div/div[1]').click()
        time.sleep(2)

        #Boton de ir a gestionar temas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[2]/button[1]').click()
        time.sleep(2)

        #Boton ir a gestionar preguntas
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/div/div[2]/app-tabla/div[2]/div/table/tbody/tr[1]/td[3]/button[1]').click()
        time.sleep(2)

        #Boton Agregar
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-preguntas/div/form/div[3]/app-crear-simulador/form/div[1]/div/div/div/button[2]').click()
        time.sleep(2)

        #Enunciado
        self.driver.find_element_by_name('enunciado').send_keys('¿Cuál de los siguientes compuestos corresponde a un hidruro?')
        time.sleep(1)
        #Imagen Enunciado
        imagen = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[3]/div/div/mat-form-field/div/div[1]/div[1]/ngx-mat-file-input/input')
        imagen.send_keys(r"C:\Users\Andrez\Pictures\FERMAT\images.jpg")
        #Opciones para respuesta
        datos = ['$H_2CO_3$','$NaH$','$HNO_2$','$H_2O_2$']
        imagenes = [r"C:\Users\Andrez\Pictures\FERMAT\hco.jpg",r"C:\Users\Andrez\Pictures\FERMAT\nah.jpg",r"C:\Users\Andrez\Pictures\FERMAT\hno.jpg",r"C:\Users\Andrez\Pictures\FERMAT\ho.jpg"]
        inp = []
        img = []
        for i in range(0,len(datos)):
            time.sleep(1)
            #Agregar respuestas
            inp.append(self.driver.find_element_by_name('item'))
            time.sleep(1)
            btn_agregar_modal = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[6]/app-lista-opciones/form/div[3]/button')
            inp[i].send_keys(datos[i])
            time.sleep(2)
            #Agregar Imagenes
            img.append(self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[6]/app-lista-opciones/form/div[2]/mat-form-field/div/div[1]/div[1]/ngx-mat-file-input/input'))
            time.sleep(1)
            img[i].send_keys(imagenes[i])



            btn_agregar_modal.click()
            time.sleep(2)
            inp[i].clear()

        #Respuesta
        permisos = [0,1]
        for x in range(0,len(permisos)):
            self.driver.find_element_by_name('respuesta').click()
            time.sleep(2)
            opc_per= self.driver.find_elements_by_class_name('mat-option')[permisos[x]]
            opc_per.click()
            time.sleep(2)
        self.driver.find_element_by_name('btnModalAgregar').click()
        time.sleep(3)
