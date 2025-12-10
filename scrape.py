import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import schedule
import time
from datetime import datetime
from pathlib import Path

now = datetime.now()
date_time = now.strftime("%m-%d-%Y")
csvfile = Path("TripleM " + date_time)

if not csvfile.is_file():
    print("enter loop")
    file = open(csvfile,"w")
    writer = csv.writer(file)
    writer.writerow(["Songs"])
    file.close()
else:
    print("did not enter")


def addSongToCSV(songAndArtist) :
    print("Song has not been played today")
    file = open(csvfile,"a")
    writer = csv.writer(file)
    writer.writerow([songAndArtist])
    file.close()

# def scan():
options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)

with driver:
    driver.get("https://play.listnr.com/station/mmm-sydney?referrer=triplem&_gl=1*11ucxey*_ga*NjcwNTY4MTM3LjE3NjI1ODM3Mzg.*_ga_FYX3DQJM1Q*czE3NjQyODgzNDgkbzIkZzAkdDE3NjQyODgzNDgkajYwJGwwJGgw")

track = driver.find_element(By.CLASS_NAME,"funuFA")
song = track.find_element(By.CLASS_NAME, "gjxUCu").text
artist = track.find_element(By.CLASS_NAME, "dFNMHX").text
driver.close()

songAndArtist = song + ": " + artist

print(songAndArtist)

if songAndArtist.strip() != "Triple M Sydney 104.9:":
    print("Song playing")
    df = pd.read_csv(csvfile)
    if len(df)>0 :
        last_row = df.tail(1)
        prevSong = last_row.iloc[0,0]
        
        if songAndArtist != prevSong:
            print("Song is not last recorded")
            
            #Condition if duplicate is found, Put bot message here
            if df['Songs'].str.contains(songAndArtist).any():
                print('Song has been played today')
                #bot message loguic here
            else:
                addSongToCSV(songAndArtist)
        
        else:
            print("Song is last recorded")
    else:
        addSongToCSV(songAndArtist)
else:
    print("Song is not playing")

# schedule.every(2).minutes.do(scan)

# while True:
#     schedule.run_pending()
#     time.sleep(1)