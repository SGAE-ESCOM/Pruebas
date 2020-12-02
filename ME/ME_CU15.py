import unittest
from selenium import webdriver
import time


class Editar_Preguntas_Respuestas:

    def __init__(self, driver):
        self.driver = driver
    
    def editar_preguntas_respuestas(self):
    
        #Opciones para respuesta
        datos = ['$Física$','$Biología$','$Química$','$Matemáticas$']
        #editar = [0,1,2,3]
        #imagenes = [r"C:\Users\Andrez\Pictures\FERMAT\hco.jpg",r"C:\Users\Andrez\Pictures\FERMAT\nah.jpg",r"C:\Users\Andrez\Pictures\FERMAT\hno.jpg",r"C:\Users\Andrez\Pictures\FERMAT\ho.jpg"]
        inp = []
        #img = []
        edit = ['/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[6]/app-lista-opciones/div/div/table/tbody/tr[1]/td/div[2]/button[1]',
                '/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[6]/app-lista-opciones/div/div/table/tbody/tr[2]/td/div[2]/button[1]',
                '/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[6]/app-lista-opciones/div/div/table/tbody/tr[3]/td/div[2]/button[1]',
                '/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div[6]/app-lista-opciones/div/div/table/tbody/tr[4]/td/div[2]/button[1]']
        for i in range(0,len(datos)):
            #Boton Editar respuesta
            editar_pr = self.driver.find_element_by_xpath(edit[i])                                       
            time.sleep(2)
            editar_pr.click()
            time.sleep(2)
            #actualizar respuestas
            inp.append(self.driver.find_element_by_name('item'))
            time.sleep(1)
            btn_actualizar_modal = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div/app-lista-opciones/form/div[3]/button[2]')
            inp[i].clear()
            inp[i].send_keys(datos[i])
            time.sleep(2)
            #Agregar Imagenes
            #img.append(self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/modal-pregunta/div/div/app-form-preguntas/div/div/div[2]/div/form/div/app-lista-opciones/form/div[2]/mat-form-field/div/div[1]/div[1]/ngx-mat-file-input/input'))
            #time.sleep(1)
            #img[i].send_keys(imagenes[i])
            #time.sleep(2)
            btn_actualizar_modal.click()
            time.sleep(2)

