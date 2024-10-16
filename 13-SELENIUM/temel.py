#selenium dosyaları indirildi , selenium pip3 edildi (indirilien dosyalarla çalışma dosyaları aynı klasörde olmalı)

from selenium import webdriver
import time #bekletmeler için

driver = webdriver.Chrome() #çalışılacak tarayıcı atanır

url = "https://www.linkedin.com/feed/" #gidilecek sayfa urlsi

driver.get(url) #girilen url yi açma
time.sleep(2) #2sn beklet

driver.maximize_window() #açılan sayfayı büyütme
driver.save_screenshot("linkedinn-homepage.png") #ekran resmi kaydetme

url = "https://www.linkedin.com/in/denizbayat1/"
driver.get(url)

print(driver.title) #açılan sayfanın sekme başlığını yazdırma

if "denizbayat" in driver.title: #sayfa başlığı içinde "denizbayat" varsa
    driver.save_screenshot("linkedin-ndeniz.png")

time.sleep(2) 
driver.back() #önceki sayfa gelir

time.sleep(2)
driver.close()