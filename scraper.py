from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper():

    def __init__(self, url: str) -> None:
        self.url = url
        self.driver = webdriver.Chrome()

    def open_webpage(self) -> None:
        """
        Method for opening the given url webpage
        & maximising the window

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        
        self.driver.get(self.url)
        self.driver.maximize_window()

    def accept_cookies(self) -> None:
        """
        Accept the cookies prompt presented by the website

        Parameters
        ----------
        None

        Returns
        -------
        None

        '''
        """
        
        try:
            accept_cookie_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button#onetrust-accept-btn-handler')))
            accept_cookie_button.click()
        except TimeoutError:
            print('cookie acception took too long and has timed out')
    
    def scroll_to_bottom_of_page(self) -> None:
        """
        Scrolls to the bottom of given page

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


if __name__ == "__main__":
    webscraper = Scraper('https://coinmarketcap.com/')
    webscraper.open_webpage()
    webscraper.accept_cookies()
    webscraper.scroll_to_bottom_of_page()