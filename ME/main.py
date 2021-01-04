from login import *
from ME_CU1 import * 
from ME_CU2 import * 
from ME_CU3 import *
from ME_CU5 import *
from ME_CU6 import *
from ME_CU7 import *
from ME_CU8 import *
from ME_CU9 import *
from ME_CU10 import *
from ME_CU11 import *
from ME_CU12 import *
from ME_CU13 import *
from ME_CU14 import *
from ME_CU16 import *
from ME_CU17 import *
from ME_CU18 import * 
from ME_CU19 import *
from ME_CU20 import *
from ME_CU21 import *
from selenium import webdriver
import unittest
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
		
		### Gestionar Grupos ###
		def gestionar_grupos(self,driver):
			#Registrar Grupo
			rg = Registrar_Grupos(self.driver)
			rg.crear_grupo()
			#Editar grupo
			ed = Editar(self.driver)
			ed.editar_grupo()
			time.sleep(2)
			

		### Gestionar Evaluacion ###
		def gestionar_evaluacion(self, driver):
			#Indice
			vge = Visualizacion_GestionEvaluacion(self.driver)
			vge.visualizacion()

			def secciones(self, driver):
				#Registrar Secciones
				rs = Registrar_Secciones(self.driver)
				rs.registrar_secciones_preguntas()
				#Editar Secciones
				es = Editar_Secciones(self.driver)
				es.editar_secciones_preguntas()
				#Visualizar Secciones
				vs = Visualizar_Secciones(self.driver)
				vs.visualizar_secciones()
			
			def temas(self,driver):
				#Registrar Temas
				rt = Registrar_Temas(self.driver)
				rt.registrar_temas()
				#Editar Temas
				et = Editar_Temas(self.driver)
				et.editar_temas()
				#Visualizar temas
				vt = Visualizar_Temas(self.driver)
				vt.visualizar_temas()

			def preguntas(self, driver):
				#Registrar Preguntas
				rp = Registrar_Preguntas(self.driver)
				rp.registrar_preguntas()
				#Editar Preguntas
				ep = Editar_Preguntas(self.driver)
				ep.editar_preguntas()
				#Visualizar preguntas
				vp = Visualizar_Preguntas(self.driver)
				vp.visualizar_preguntas()
			
			def evaluacion(self, driver):
				#Registrar Evluaciones
				re = Registrar_Evaluaciones(self.driver)
				re.registrar_evaluaciones()
				#Editar Evaluaciones
				ee = Editar_Evaluaciones(self.driver)
				ee.editar_evaluaciones()
				#Visualizar Evaluaciones
				ve = Visualizar_Evaluaciones(self.driver)
				ve.visualizar_evaluaciones()


			
			secciones(self,self.driver)
			temas(self,self.driver)
			preguntas(self, self.driver)
			evaluacion(self, self.driver)
		
		### Gestionar Evaluacion ###
		def aplicacion(self,driver):
			#Registrar Aplicaciones 
			ra = Registrar_Aplicaciones(self.driver)
			ra.registrar_aplicaciones()
			#Editar Aplicaciones
			ea = Editar_Aplicaciones(self.driver)
			ea.editar_aplicaciones()
			#Visualizar Aplicaciones
			va = Visualizar_Aplicaciones(self.driver)
			va.visualizar_aplicaciones()




		gestionar_grupos(self,self.driver)
		gestionar_evaluacion(self,self.driver)
		aplicacion(self,self.driver)


	def tearDown(self):
		self.driver.quit()




