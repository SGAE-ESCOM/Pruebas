from selenium import webdriver
import time


class Definir_Fechas:

    def __init__(self, driver):
        self.driver = driver

    def definir_fechas(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-sidenav/div/mat-sidenav-container/mat-sidenav-content/div/app-main-etapas/div/app-cards/div/div[2]').click()
        time.sleep(2)
        
        #Fecha
        fecha = [1,2,3,4,5,6,7,8,9,10,11,12]
        day =   [7,9,11,13,15,17,19,21,23,25,27,29]
        btnCalendar = self.driver.find_elements_by_class_name('mat-focus-indicator.mat-icon-button.mat-button-base')
        print("longitud BTN: ",len(btnCalendar))
        for i in fecha:
            btnCalendar[i].click()
            time.sleep(1)
            month = self.driver.find_elements_by_class_name('mat-calendar-body-cell.mat-focus-indicator.mat-calendar-body-active.ng-star-inserted')
            print("longitud mont: ",len(month))
            if i % 2 == 1:
                month[0].click()
                time.sleep(1)
            if day[i] > 27:
                next_month = self.driver.find_elements_by_class_name('mat-focus-indicator.mat-calendar-next-button.mat-icon-button.mat-button-base')
                next_month[1].click()
            dia = self.driver.find_elements_by_class_name('mat-calendar-body-cell')[day[i]]
            dia.click()
            time.sleep(1)
     

        #Grupo
        opc = [0,1,2,3,4,5]
        for x in opc:
            colores = self.driver.find_elements_by_class_name('mat-select')
            colores[x].click()
            time.sleep(1)
            color = self.driver.find_elements_by_class_name('mat-option')[opc[x]]
            color.click()
            time.sleep(1)


