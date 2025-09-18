# Jarvis/features/google_search.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
import webbrowser

def google_search(query: str):
    # Fall back to system browser if Selenium/Chrome fails for any reason
    try:
        opts = Options()
        # comment the next line if you want to see the browser window
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--disable-dev-shm-usage")

        # On macOS this will auto-download a matching ChromeDriver and launch Chrome/Chromium
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

        # Do a very basic search open (you can expand to scraping later)
        q = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={q}"
        driver.get(url)

        # Keep the tab open for a bit or until other code closes it. For demo, leave it open 5s.
        # import time; time.sleep(5)
        # driver.quit()  # uncomment if you want it to close automatically
    except Exception as e:
        # As a fallback, just open the search in the default browser
        q = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={q}"
        webbrowser.open(url)
        print("Selenium failed; opened in default browser instead:", e)
