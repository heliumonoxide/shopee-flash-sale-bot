from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pause
from datetime import datetime
import time
import json
import os
from functools import reduce
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import 

#Scheduler
year = 2022
month = 10
day = 30
hour = 18
minute = 0

#Metode bayar
bank = 'Bank BNI'
bayarvia = 'Transfer Bank'
metodePembayaran0 = "//div[contains(text(),'" + bayarvia + "')]"
metodePembayaranBank = "//div[contains(text(),'" + bank + "')]"

#User Info
EMAIL = 'kikirahman@gmail.com'
PASSWORD = '28Januari2002'

#Target Shopee Link
targetURL = 'https://shopee.co.id/HP-11-CHROMEBOOK-N4020-4GB-160GB-11.6-HD-LAPTOP-PELAJAR-TERMURAH-NEW-ORIGINAL-i.392375505.8745642630'
pathFeatures = np.array(['BUNDLE NORMAL', '32GB'],dtype=object)

class ChromeWithPrefs(webdriver.Chrome):
    def __init__(self, *args, options=None, **kwargs):
        if options:
            self._handle_prefs(options)

        super().__init__(*args, options=options, **kwargs)

        # remove the user_data_dir when quitting
        self.keep_user_data_dir = False

    @staticmethod
    def _handle_prefs(options):
        if prefs := options.experimental_options.get("prefs"):
            # turn a (dotted key, value) into a proper nested dict
            def undot_key(key, value):
                if "." in key:
                    key, rest = key.split(".", 1)
                    value = undot_key(rest, value)
                return {key: value}

            # undot prefs dict keys
            undot_prefs = reduce(
                lambda d1, d2: {**d1, **d2},  # merge dicts
                (undot_key(key, value) for key, value in prefs.items()),
            )

            # create an user_data_dir and add its path to the options
            user_data_dir = "C:\\Users\\Bryan\\AppData\\Local\\Google\\Chrome\\User Data"
            options.add_argument(f"--user-data-dir={user_data_dir}")

            # create the preferences json file in its default directory
            default_dir = os.path.join(user_data_dir, "Profile 1")
            os.mkdir(default_dir)

            prefs_file = os.path.join(default_dir, "Preferences")
            with open(prefs_file, encoding="latin1", mode="w") as f:
                json.dump(undot_prefs, f)

            # pylint: disable=protected-access
            # remove the experimental_options to avoid an error
            del options._experimental_options["prefs"]


if __name__ == "__main__":
# use the derived Chrome class that handles prefs

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Force Login
    driver.get(str(targetURL))

    # Click Login
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Log In']")))
    driver.find_element(By.XPATH, "//a[normalize-space()='Log In']").click()
    time.sleep(0.2)

    # Login
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='No. Handphone/Username/Email']")))
    driver.find_element(By.XPATH, "//input[@placeholder='No. Handphone/Username/Email']").send_keys(EMAIL)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(Keys.RETURN)
    time.sleep(0.3)

    pause.until(datetime(year, month, day, hour, minute))

    # Click Buy and Features
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='beli sekarang']")))

    for i in range(len(pathFeatures)):
        driver.find_element(By.XPATH, "(//button[normalize-space()='" + pathFeatures[i] + "'])[1]").click()

    driver.find_element(By.XPATH, "//button[normalize-space()='beli sekarang']").click()

    #Checkout
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='kcsswk']")))
    driver.find_element(By.XPATH,
                        "//span[@class='kcsswk']").click()

    #Customize metode pembayaran

    if bayarvia == 'Transfer Bank':
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                        "//button[normalize-space()='Transfer Bank']")))
        driver.find_element(By.XPATH,
                            "//button[normalize-space()='Transfer Bank']").click()
        time.sleep(0.3)
        driver.find_element(By.XPATH,
                            metodePembayaranBank).click()

    if bayarvia == 'ShopeePay':
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                        "(//span[contains(text(),'ShopeePay')])[1]")))
        driver.find_element(By.XPATH,
                            "(//span[contains(text(),'ShopeePay')])[1]").click()

    if bayarvia == 'Cash on Delivery':
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                        "//button[normalize-space()='COD (Bayar di Tempat)']")))
        driver.find_element(By.XPATH,
                            "//button[normalize-space()='COD (Bayar di Tempat)']").click()


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                    "//button[normalize-space()='Buat Pesanan']")))

    time.sleep(1)

    #Buat pesanan/bayar
    driver.find_element(By.XPATH,
                        "//button[normalize-space()='Buat Pesanan']").click()

    time.sleep(10)