import pandas as pd


def clean_listing(listing): # Drops columns not necessary for Client and renames other for better understanding
        # """
        # Cleans the listing DataFrame by dropping unnecessary columns, renaming columns, and resetting the index.

        # Parameters:
        #     listing (DataFrame): The DataFrame containing the listing data.

        # Returns:
        #     DataFrame: The cleaned listing DataFrame with renamed columns and reset index.
        # """
        listing = listing.drop(['clnt_id','bank_id','acc_id','txn_id','lemm_merchant','lemm_cat'],axis=1)
        listing.rename(columns={'txn_date': 'Transaction Date', 'desc': 'Description', 'amt': 'Amount', 'cat': 'Category', 'merchant': 'Merchant'}, inplace=True)
        listing = listing.reset_index()
        return listing

def get_listing_for_date(data,dates): # Filters data based on dates
        # """
        # Filters the given data based on the provided dates.

        # Parameters:
        #     data (DataFrame): The data to be filtered.
        #     dates (dict): A dictionary containing the dates to filter the data.

        # Returns:
        #     DataFrame: The filtered data based on the provided dates.
        # """
        dates = [date for date in dates.values()]
        if len(dates)==1:
            listing = data[data["txn_date"] == pd.to_datetime(dates[0])]
        else:
            listing = data[(data["txn_date"] >= pd.to_datetime(dates[0])) & (data["txn_date"] <= pd.to_datetime(dates[1]))]
        return listing

        
def get_credit_amount_from_date(data,dates): # Filters data based on dates and get the sum of credits
    #  """
    # Filters the given data based on the provided dates and calculates the sum of credits.

    # Parameters:
    #     data (DataFrame): The data to be filtered.
    #     dates (list): A list of dates to filter the data. If only one date is provided, it filters the data for that specific date. If two dates are provided, it filters the data for the range between the two dates (inclusive).

    # Returns:
    #     str: A formatted string indicating the total amount spent on credits for the specified dates. If only one date is provided, the string includes the date. If two dates are provided, the string includes the range of dates.
    # """
    if len(dates)==1:
        listing = data[data["txn_date"] == pd.to_datetime(dates[0])]
        return f"You spent {str(round(listing[listing['amt']<0]['amt'].sum())).lstrip('-')} on {dates[0]}\n "

    else:
        listing = data[(data["txn_date"] >= pd.to_datetime(dates[0])) & (data["txn_date"] <= pd.to_datetime(dates[1]))]
        return f"You spent {str(round(listing[listing['amt']<0]['amt'].sum())).lstrip('-')} between {dates[0]} and {dates[1]}\n "
    
   

def get_debit_amount_from_date(data,dates): # Filters data based on dates and get the sum of debits

#     Filters the given data based on the provided dates and calculates the sum of debits.
# 
#     Parameters:
#         data (DataFrame): The data to be filtered.
#         dates (list): A list of dates to filter the data. If only one date is provided, it filters the data for that specific date. If two dates are provided, it filters the data for the range between the two dates (inclusive).
# 
#     Returns:
#         str: A formatted string indicating the total amount deposited for the specified dates. If only one date is provided, the string includes the date. If two dates are provided, the string includes the range of dates.
#     """
    if len(dates)==1:
        listing = data[data["txn_date"] == pd.to_datetime(dates[0])]
        return f"You deposited {str(round(listing[listing['amt']>0]['amt'].sum())).lstrip('-')} on {dates[0]}\n "

    else:
        listing = data[(data["txn_date"] >= pd.to_datetime(dates[0])) & (data["txn_date"] <= pd.to_datetime(dates[1]))]
        return f"You deposited {str(round(listing[listing['amt']>0]['amt'].sum())).lstrip('-')} between {dates[0]} and {dates[1]}\n"