from nltk.stem import WordNetLemmatizer
from helpers.pandas_helper import clean_listing, get_listing_for_date, get_credit_amount_from_date, get_debit_amount_from_date
import pandas as pd

class DataFetcher:
    def __init__(self,client_id):
        data = pd.read_csv("../Processed_Data.csv")
        data['txn_date'] = pd.to_datetime(data["txn_date"])
        if client_id not in data["clnt_id"].unique():
            print("Invalid Client Id, Quitting!!")
            exit()
        self.data = data[data["clnt_id"] == int(client_id)]
        self.categories = data["lemm_cat"].unique()
        self.merchants = data["lemm_merchant"].unique()
        self.lemmatizer = WordNetLemmatizer()
    

    def GetTransactions(self,dates):
        listing = get_listing_for_date(self.data,dates)
        listing = clean_listing(listing)
        dates = [date for date in dates.values()]
        
        if len(dates)==1:
            return f"Following are your Transactions for the date : {dates[0]}\n {listing}"
        else:
            return f"Following are your Transactions between : {dates[0]} and {dates[1]}.\n {listing}"
    
   
    def GetTransactionsAmount(self,trn_type,dates):
        dates = [date for date in dates.values()]
        if trn_type == "credit":
            return get_credit_amount_from_date(self.data,dates)
            
        else:
            return get_debit_amount_from_date(self.data,dates)
                
    def _get_cat_or_merch(self,cat_or_merch): # Checks if user is filtering on category or merchant
        if cat_or_merch in self.merchants:
            return "lemm_merchant"
        elif cat_or_merch in self.categories:
            return "lemm_cat"
        else:
            return None
        

    def GetCategoryTransactions(self,merchant,dates=None):
        filtered_data = self.data
        if self._is_valid_date(dates):
            filtered_data = get_listing_for_date(self.data,dates)
        merchant = self.lemmatizer.lemmatize(str(merchant).lower())
        listing = None
        column = self._get_cat_or_merch(merchant)
        if column is None:
            return f"Sorry, {merchant} not found"
        listing = filtered_data[filtered_data[column] == merchant]
        
        if listing is not None and len(listing) > 0:
            listing = clean_listing(listing)
            return f"Following are your transactions for {merchant}.\n{listing}"
        else:
            return "No transaction found"
    
    def GetCategoryTransactionsAmount(self,trn_type,merchant,dates=None):
        filtered_data = self.data
        if self._is_valid_date(dates):
            filtered_data = get_listing_for_date(self.data,dates)
        amount = 0
        listing = None
        merchant = self.lemmatizer.lemmatize(str(merchant).lower())
        column = self._get_cat_or_merch(merchant)
        if column is None:
            return f"Sorry {merchant} not found"
        listing = filtered_data[filtered_data[column] == merchant]
        if listing is not None and len(listing) > 0:
            amount = listing[listing["amt"]<0]["amt"].sum() * -1 if trn_type == "credit" else listing[listing["amt"]>0]["amt"].sum()
        return f"You have spent {round(amount)} for {merchant}"
    
    def _is_valid_date(self,dates): # Check if GPT outputted a date or not
        if dates:
            dates = [date for date in dates.values() if date != ""]
            if dates:
                return True
        return False
