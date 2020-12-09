from selenium import webdriver
import time

# Login
class Login:

	def __init__(self,user,password,driver):
		self.user = user
		self.password = password
		self.driver = driver

	def login(self):
		self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-toolbar/a[2]').click()
		time.sleep(2)
		#User
		self.driver.find_element_by_name('email').send_keys(self.user)
		#Password
		self.driver.find_element_by_name('password').send_keys(self.password)
		#IniciarSesion
		self.driver.find_element_by_xpath('//*[@id="login"]/div/div/div/div/div/div/form/button').click()
		time.sleep(4)