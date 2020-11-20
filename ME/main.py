from login import *
from ME_CU1 import * 
from ME_CU2 import * 
from ME_CU3 import *
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
		#Indice Evaluacion
		ie = Indice_evaluacion(self.driver)
		ie.indice()
		#Registrar Grupo
		rg = Gestionar_Grupos(self.driver)
		rg.crear_grupo()
		#Editar grupo
		ed = Editar(self.driver)
		ed.editar_grupo()

	def tearDown(self):
		self.driver.quit()




