from selenium import webdriver
import time


#Clase para Registrar de grupos.
class Registrar_Grupos:
	def __init__(self,driver):
		self.driver = driver
	#crear grupo 
	def crear_grupo(self):
		#Boton Ir Gestionar Grupos
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[1]').click()
		time.sleep(2)
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-grupos/div/div/div[2]/app-tabla/div[1]/div[2]/div/div/button').click()
		time.sleep(2)
		programa = ['','Deep Learning']
		inp = self.driver.find_elements_by_class_name('mat-input-element')
		for i in range(0,len(programa)):
			inp[i].send_keys(programa[i])
		time.sleep(4)
		self.driver.find_element_by_name('btnModalAgregar').click()
		time.sleep(4)

