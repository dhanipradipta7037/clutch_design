from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import time
import pandas as pd
import os
from bs4 import BeautifulSoup
from playwright_stealth import stealth_sync

def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries+1):
        time.sleep(sleep * i)
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                stealth_sync(page)
                page.goto(url, timeout=120000)
                print(page.title())
                html = page.inner_html(selector)
        except PlaywrightTimeout:
            print(f"timeout error on {url}")
            continue
        else:
            break
    return html

def data_html():
    selector ='ul.directory-list'
    url = 'https://clutch.co/agencies/design?reviews=10'
    data_url = url.split('/')[-2]
    data = get_html(url, selector)
    try:
        with open("data/{}.html".format(data_url), "w+", encoding="utf-8") as f:
            f.write(data)
    except:
        print(f"timeout error on {url}")

if __name__ == '__main__':
    data_html()

