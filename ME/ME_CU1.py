from selenium import webdriver
import time

#Caso de Indice Evaluación 
class Indice_evaluacion:
	def __init__(self,driver):
		self.driver = driver

	def indice(self):
		#Boton ir Evaluación
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/app-cards/div/div[2]').click()
		time.sleep(2)
		num = [9,10,11,12]
		for i in num:
			button = self.driver.find_elements_by_class_name('mat-icon')
			button[i].click()
			time.sleep(2)
			self.driver.back()
			time.sleep(2)
