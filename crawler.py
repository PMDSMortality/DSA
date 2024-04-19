from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pandas as pd
import re

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

def extract_from_entries(entries: list, elements_to_find: list):
    collected_entries = []

    for entry in entries:
        finds = []
        for tag in elements_to_find:
            found_elements = entry.find_all(tag, recursive=True)
            for x in found_elements:
                text =  x.getText()
                text = text.replace("  ", "")
                text = text.replace("\n", "")
                text = text.strip()
                if text:
                    finds.append(text)

        if len(finds) > 0:                    
            finds = list(dict.fromkeys(finds))
            collected_entries.append(finds)

    print(collected_entries)
    return collected_entries

def get_components_from_local_html(tag_type: str, class_name = ""):
    # read from local stored html (result of crawler)
    HTMLFile = open("data/crawler_output.html", "r") 
    index = HTMLFile.read() 
    # Creating a BeautifulSoup object and specifying the parser 
    soup = BeautifulSoup(index, 'html.parser') 
    # print(S.body)

    if class_name:
        entries = soup.find_all(tag_type, {"class": class_name})
    else:
        entries = soup.find_all(tag_type)

    return entries

def extract_happenings_as_json(extracted_elements: list):
    months = {
        "Januar": "01",
        "Februar": "02",
        "März": "03",
        "April": "04",
        "Mai": "05",
        "Juni": "06",
        "Juli": "07",
        "August": "08",
        "September": "09",
        "Oktober": "10",
        "November": "11",
        "Dezember": "12",
    }

    keys = months.keys()
    results_list = []

    for elem in extracted_elements:
        date_str = elem[0]
        # print(len(elem))
        regex = r"^\d{1,2}. \w* \d{,4}"
        new_list_elem = elem.copy()

        if re.match(regex, date_str): 
            date_str = date_str.replace(".", "").replace(" ", "-")
            for key in keys:
                date_str = date_str.replace(key, months[key])
            date_format = '%d-%m-%Y'
            new_list_elem[0] = date_str
            results_list.append(new_list_elem)
    
    return results_list
        