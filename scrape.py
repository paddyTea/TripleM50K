# from selenium import webdriver
import undetected_chromedriver as uc

# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pickle
# import time
from selenium.webdriver.common.by import By
# import csv

options = uc.ChromeOptions()
options.headless = False


driver = uc.Chrome(options=options)  

filename = "TripleM"

with driver:
    driver.get("https://play.listnr.com/station/mmm-sydney?referrer=triplem&_gl=1*11ucxey*_ga*NjcwNTY4MTM3LjE3NjI1ODM3Mzg.*_ga_FYX3DQJM1Q*czE3NjQyODgzNDgkbzIkZzAkdDE3NjQyODgzNDgkajYwJGwwJGgw")

artist = "dnw"
track = driver.find_element(By.CLASS_NAME,"funuFA")
song = track.find_element(By.CLASS_NAME, "gjxUCu").text
artist = track.find_element(By.CLASS_NAME, "dFNMHX").text


print(track)
print(song)
print(artist)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
try:
    with open(filename, "wb") as file:
        pickle.dump(soup, file)
    print("Successful Dump", filename)
except Exception as e:
    print("Error during pickling object (Possibly unsupported):", {e})

# file = open("MyCSVFile.csv","w")
# writer = csv.writer(file)
# writer.writerow(["test"])
# file.close()

# print(soup.prettify())
# print(filename)
driver.close()

