import datetime
import time
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
    
    def get_all_links(self):
        """
        Return a list of links from the webpage
        

        """
        prop_container = self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table')
        table_body_container = prop_container.find_element(by=By.XPATH, value='./tbody')
        table_row_list = table_body_container.find_elements(by=By.XPATH, value='./tr')
        
        
        link_list = []

        for crypto in table_row_list:
            a_tag = crypto.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)
        
        print(link_list)
        return link_list
    
    def get_data_from_links(self,link_list: list) -> dict:
        """
        Gets all the data from the given links and packages it into one
        easy dictionary

        Parameters
        ----------
        link_list: list of links to be scraped from

        Returns
        -------
        dict: of data from every link visited

        """
        stats_figures = list()
        stats_name = list()
        data = list()

        for i in range(2): #visits the first five links on the page
            self.driver.get(link_list[i])
            
            #locate where the coin name is stored on the webpage
            coin_name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@class="coin-name-pc"]')))
            
            #get the innerHTML attribute which is the coin name
            coin_name = coin_name.get_attribute("innerHTML")
            stats_name.append('Coin name')
            stats_figures.append(coin_name)

            #locate the price of the coin at the moment
            section_overview = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="section-coin-overview"]/div[2]')))
            price =section_overview.find_element(By.TAG_NAME, 'span').get_attribute("innerHTML")
            stats_name.append('Price')
            stats_figures.append(price)

            #locate the coin statistics
            section_overview = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="section-coin-stats"]')))
            statistics = section_overview.find_elements(By.TAG_NAME, 'dd')
            statistics_names = section_overview.find_elements(By.TAG_NAME, 'dt')
            for stat in statistics:
                print(stat.text)
                stats_figures.append(stat.text.replace('\n'," "))
            for names in statistics_names:
                stats_name.append(names.text.replace('\n', ""))

            #add a timestamp to the data collected
            stats_name.append('timestamp')
            stats_figures.append(datetime.datetime.fromtimestamp(time.time()).strftime("%m/%d/%Y %H:%M:%S"))
            
            coin_data = dict(zip(stats_name, stats_figures))

            data.append(coin_data)    
        
        return data
        


if __name__ == "__main__":
    webscraper = Scraper('https://coinmarketcap.com/')
    webscraper.open_webpage()
    webscraper.accept_cookies()
    webscraper.scroll_to_bottom_of_page()
    link_list=webscraper.get_all_links()
    webscraper.get_data_from_links(link_list)