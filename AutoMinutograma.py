from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import schedule
import time

usuario1 = "nnnn"
password1 = "nnn"


def ejecutar_tarea():
    print("Versión de Selenium:", selenium.__version__)
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # ejecutar Chrome en no visible
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get("http://172.24.43.27:8008/Semaforo_Claro/index.php")
    driver.implicitly_wait(30)

    usuario = driver.find_element(By.ID, 'user')
    usuario.send_keys(usuario1)

    password = driver.find_element(By.ID, 'password')
    password.send_keys(password1)

    login_button = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div/div[1]/div/form/input')
    ActionChains(driver).move_to_element(login_button).click().perform()

    driver.implicitly_wait(30)

    Marcar = driver.find_element(By.XPATH, '//*[@id="sidebar-nav"]/div/div[1]/nav/ul/li[3]/a/span')
    ActionChains(driver).move_to_element(Marcar).click().perform()

    driver.implicitly_wait(30)

    Marcar = driver.find_element(By.XPATH, '//*[@id="subPages2"]/ul/li[1]/a')
    ActionChains(driver).move_to_element(Marcar).click().perform()

    driver.implicitly_wait(30)

    Marcar = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div/div/div/div/div/form/center/form/center/input')
    ActionChains(driver).move_to_element(Marcar).click().perform()

    driver.implicitly_wait(30)
    print("Proceso se realizo correctamente")
    driver.quit()


schedule.every(30).minutes.do(ejecutar_tarea)
ejecutar_tarea()

while True:
    schedule.run_pending()
    time.sleep(1)
