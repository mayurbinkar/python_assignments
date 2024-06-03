from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

#url = 'https://www.google.com/finance/quote/NIFTY 50:NSE'
url = 'https://www.google.com/finance/quote/ITC:NSE'
#url = 'https://www.google.com/finance/quote/TCS:NSE'
#url = 'https://www.google.com/finance/quote/NIFTY 50:NSE'

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scroll(0,document.body.scrollHeight)")
        page.screenshot(path="tcs.png", full_page=True)
        #page.screenshot(path="ITC.png", full_page=True)
        #page.screenshot(path="NIFTY.png", full_page=True)
        googlePage = page.inner_html("body")
        bs4FlipHtml = BeautifulSoup(googlePage, "html.parser")
        print(bs4FlipHtml)

