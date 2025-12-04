import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import csv
import pandas as pd

options = uc.ChromeOptions()
options.headless = False


driver = uc.Chrome(options=options)  

filename = "TripleM"

with driver:
    driver.get("https://play.listnr.com/station/mmm-sydney?referrer=triplem&_gl=1*11ucxey*_ga*NjcwNTY4MTM3LjE3NjI1ODM3Mzg.*_ga_FYX3DQJM1Q*czE3NjQyODgzNDgkbzIkZzAkdDE3NjQyODgzNDgkajYwJGwwJGgw")

track = driver.find_element(By.CLASS_NAME,"funuFA")
song = track.find_element(By.CLASS_NAME, "gjxUCu").text
artist = track.find_element(By.CLASS_NAME, "dFNMHX").text
driver.close()

songAndArtist = song + ": " + artist

if songAndArtist != "Triple M" :
    
    df = pd.read_csv("MyCSVFile.csv")
    last_row = df.tail(1)
    print(last_row)
    prevSong = last_row.iloc[0,0]
    print(prevSong)
    # if(last_row contains songAndArtist)
    

    # print(songAndArtist)
    # file = open("MyCSVFile.csv","r")
    # csvreader = csv.reader(file)
    # for row in csvreader:
    #     print(row)
    # file.close()

    if songAndArtist != prevSong:
        file = open("MyCSVFile.csv","a")
        writer = csv.writer(file)
        writer.writerow([songAndArtist])
        file.close()


