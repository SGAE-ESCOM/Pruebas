from login import *
from MGE_CU1 import *
from MGE_CU2 import *
from MGE_CU3 import *


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

        #Indice Gestión de etapas.
        ie = Indice_Gestión_Etapas(self.driver)
        ie.indice()

        def definir_etapas(self, driver):
            de = Definir_Etapas(self.driver)
            de.definir_etapas()

        def definir_fechas(self,driver):
            df = Definir_Fechas(self.driver)
            df.definir_fechas()
        

        #definir_etapas(self,self.driver)
        definir_fechas(self, self.driver)

    def tearDown(self):
        self.driver.quit()
