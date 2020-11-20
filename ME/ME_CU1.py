from selenium import webdriver
import time

#Caso de Indice Evaluación 
class Indice_evaluacion:
	def __init__(self,driver):
		self.driver = driver

	def indice(self):
		#Boton ir Evauación
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
		time.sleep(2)
		#Boton Ir Gestionar Evaliuación
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[2]').click()
		time.sleep(2)
		self.driver.back()
		time.sleep(2)
		#Boton Ir Gestionar Grupos
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-evaluacion/div/app-cards/div/div[1]').click()
		time.sleep(2)
		self.driver.back()
		time.sleep(2)
