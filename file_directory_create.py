import json
import os

class FileDirectory():

    def __init__(self, folder_name: str):
        """
        Takes the folder name that you would like to create in your
        parent directory

        Input: folder_name (str)
        """
        parent_dir = os.path.dirname(os.getcwd())
        self.path = os.path.join(parent_dir, folder_name)

    def create_folder(self):
        """
        Checks whether folder is created if not, creates the folder
        """
        
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def create_crypto_folders(self, crypto_list: dict):
        """
        Creates the crypto folders for each crypto in the dictionary
        and writes the dictionary data

        Input: crypto_list (dict)
        """
        #loop through crypto dictionaries in the list
        for crypto_dict in crypto_list:
            
            #get the name of the coin which will be used to create the folder
            crypto_folder = crypto_dict['Coin name']
            crypto_folder_path = os.path.join(self.path, crypto_folder)

            #checks whether the crypto folder exists if not creates it
            if not os.path.exists(crypto_folder_path):
                os.mkdir(crypto_folder_path)
            
            #writes the json payload into a data.json file
            with open(os.path.join(crypto_folder_path, 'data.json'), 'w') as fp:
                json.dump(crypto_dict, fp)

if __name__ == "__main__":
    file_create = FileDirectory('raw_data')
    file_create.create_folder()
    file_create.create_crypto_folders([{'Coin name': 'Bitcoin', 'Price': '$41,892.99', 'Market cap ': '1.00% $819.94B', 'Volume (24h) ': '29.56% $13.85B', 'Volume/Market cap (24h) ': '1.71%', 'Circulating supply ': '19.57M BTC', 'Total supply ': '19.57M BTC', 'Max. supply ': '21M BTC', 'Fully diluted market cap ': '$879.78B'}, {'Coin name': 'Ethereum', 'Price': '$2,213.85', 'Market cap ': '1.77% $266,104,402,167', 'Volume (24h) ': '36.61% $6,487,025,456', 'Volume/Market cap (24h) ': '2.46%', 'Circulating supply ': '120,199,702 ETH', 'Total supply ': '120,199,702 ETH', 'Max. supply ': '∞', 'Fully diluted market cap ': '$266,273,107,112'}])