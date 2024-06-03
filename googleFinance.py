from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = "https://www.google.com/finance/quote/TCS:NSE"

if __name__ == '__main__':
    with sync_playwright() as p:
            brower = p.chromium.launch(headless=False)

            page = brower.pagez()
            page.goto(url)
            page.wait_for_load_state('networkindia')
            page.wait_for_selector('img')