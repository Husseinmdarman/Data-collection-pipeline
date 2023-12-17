# Data-collection-pipeline

Industry-grade data collection pipeline that runs scalably in the cloud. It uses Python code to automatically control your browser, extract information from a website, and store it on the cloud in a data warehouse and data lake. The system conforms to industry best practices, such as being containerised in Docker and running automated#

# Decide which website you are going to collect data from

In this case the selected website that i will be collecting data from is [CoinMarketCap](https://coinmarketcap.com/), which can lead to better decision making or accepting a risky venture. The following avenues is where this data might be helpful in pursuing the overall business aims:
* overall monitoring of cyrtocurrancy
* Keeping Record of Government Decisions on Cryptocurrency
* Monitor Companies that Accept Payments in Cryptocurrency
* Price Monitoring & Analysis of Major Cryptocurrency Rates

# Finding links for each webpage we are concerned with

The main focus in this case, is to extract the data from the webpage, the first aim would be to find the links on the main page which are going to be visted to extract the data from

The following methods will help in finding the links on the main page aside from the Scraper init method:
* open_webpage: which in simplest terms opens the webpage
* accept_cookies: which waits for the element containing the on onetrust banner to be dynamically loaded afterward it clicks the accept button for the cookies
* get all links method: which locates the table where all the href are stored for each link on the crypto table to their specific crypto coin webpage

# Locating the data on the webpage

Now that all the links to the individual hrefs for each crypto coin has been located. The next aim will be to locate the data on each individual webpage.

There is only one method for this which is called get_data_from_links: 

This method uses the same get_all_links method from before and once that list is acquired, it iterates through the list, during iteration this method uses selenium to extract key information from the containers on the page.

Currently what we're looking at is: 
* "Coin name"
* "Price"
* "Market cap "
* "Volume (24h) "
* "Volume/Market cap (24h) "
*  "Circulating supply 
*  "Total supply "
*  "Max. supply "
*  "Fully diluted market cap "

## packing this found data

Now the aim for the section, is to turn these into some sort of structure. The thought behind this is due to already having key and value pairs each individual link creates their own dictionary, due to the nature of it. I have created two list one being stats_name and stats_figures, where their are the names of the keys and values respectively.

Now once this dict is created it is appends to the overall data list which is then returned after all iterations are ran through

# Creating the file structure

The aim is to allow the user to create the file structure with the name they intended. i.e 'raw-folder' then after there is a key method that takes the data created previously and makes individual folders and drops the json data into its respective files.

 create_crypto_folders(self, crypto_list: dict)

 