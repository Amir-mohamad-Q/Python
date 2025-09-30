from concurrent.futures import thread
import streamlit as st
import requests as rq 
import threading

def check_site_avaliability(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64)'}
        response = rq.get(url = url, headers=header)
        if response.status_code == 200:
            return True
        else: return False
    except Exception as e:
        return False


website_for_check = {
    'https://www.pytopia.ai/',
    'https://www.google.com/',
    'https://www.mentorix.ir/',
} * 10


threads = []
for url in website_for_check:
    thread = threading.Thread(target = check_site_avaliability, args = url,)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()