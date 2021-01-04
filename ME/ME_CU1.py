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
		num = [7,8,9,10]
		for i in num:
			button = self.driver.find_elements_by_class_name('mat-icon')
			#print("Btn cartitas ",len(button))
			button[i].click()
			time.sleep(1)
			self.driver.back()
			time.sleep(1)
		print("... Test Case 'Indice Evaluación' Successful ...")
		print("================================================")
