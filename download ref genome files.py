#AUTHOR: Jyot Thesia
#DATE: 18/06/2024
#1. DESC.: Download reference genome file for hg38 and saves on target folder path

import os
import requests
import gzip
import shutil
from bs4 import BeautifulSoup

def download_files(url, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    response = requests.get(url)
    soup= BeautifulSoup(response.text, 'html.parser')     
    for link in soup.select("a[href$='.fa.gz']"):
        filename = os.path.join(target_folder, link['href'])
        with open(filename, 'wb') as f:
            f.write(requests.get(url + link['href']).content)
            
        # Unzip the file
        with gzip.open(filename, 'rb') as f_in:
            with open(filename[:-3], 'wb') as f_out:  # remove the '.gz' from the filename
                shutil.copyfileobj(f_in, f_out)
        
        # Delete the original .gz file
        os.remove(filename)

    print("Download and extraction finished.")

# specify the URL and target folder here
url = "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/"
target_folder = r"C:\Users\jyott\Desktop\.py\new_folder\hg38"

#download_files(url, target_folder)
