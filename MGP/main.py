from login import *
from MGP_CU1 import * 
from MGP_CU3 import *
from MGP_CU4 import *
import unittest
from selenium import webdriver
import time


class Main(unittest.TestCase):
	
	def setUp(self):
		self.url = 'https://sgae-escom.firebaseapp.com/#/'

	def test_main(self):
		# Instancia de webDriveR
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\Andrez\OneDrive - Instituto Politecnico Nacional\ESCOM\TT1\PRUEBAS\WebDriver\chromedriver.exe")
		self.driver.get(self.url)
		self.driver.maximize_window()
		time.sleep(2)
		#Iniciar Sesion
		loginA = Login('root@test.com','root1234',self.driver)
		loginA.login()

		#Indice Pagos
		ip = Indice_pagos(self.driver)
		ip.indice()

		#Registrar Cuenta Bancaria
		rcb = Registrar_Cuenta(self.driver)
		rcb.registrar()
		rcb.registrar_campos_adicionales()

		#Editar Cuenta Bancaria
		ecb = Editar_Cuenta(self.driver)
		ecb.editar()
		ecb.editar_campos_adicionales() 

		
	def tearDown(self):
		self.driver.quit()




