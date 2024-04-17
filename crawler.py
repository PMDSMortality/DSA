from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas
import time

def crawl_page_lazy_loading(save_as_file=False):
    chrome = webdriver.Chrome()
    chrome.get("https://www.bundesgesundheitsministerium.de/coronavirus/chronik-coronavirus")

    #scroll parameters
    scrollHeight = 2000
    new_height = scrollHeight
    last_height = 0
    pause = 0.2

    # scroll page (not sure if the px of 225000 fit at all)
    while new_height < 225000:
        chrome.execute_script("window.scrollTo("+ str(last_height) +", " + str(new_height) + ");")
        time.sleep(pause)
        new_height += scrollHeight
        last_height += scrollHeight
        if new_height % 25000 == 0:
            print(new_height)  


    source = chrome.page_source
    soup = BeautifulSoup(source,"html.parser")

    if save_as_file:
        #stores crawled output after lazy loading the entire page 
        with open("./data/crawler_output.html", "w", encoding = 'utf-8') as file: 
            # prettify the soup object and convert it into a string   
            file.write(str(soup.prettify()))

    entries = soup.find_all("div", {"class": "c-component"})
    return entries

def extract_from_entries(entries, elem_to_find):
    collected_entries = []

    for entry in entries:
        elements = entry.find_all(elem_to_find, recursive=True)
        for x in elements:
            text =  x.getText()
            # text = text.replace(" ", "")
            text = text.replace("\n", "")
            text = text.strip()
            collected_entries.append(text)
        
    return collected_entries


    