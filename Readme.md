## Transaction Helper ChatBot

This Project aims to Help customers of a Bank Like App.
The aim is to convert different operations from clicking in app to natural language understanding,
Where a customer can ask different questions by typing or verbally. And the chatbot tries to identify the intent 
of user and come up with a possible answer of user query.

## How to install Dependencies.

1) Open a terminal in Project directory
2) Type following command to create a python pip virtual environment.
    python -m venv venv
3) activate the environment by typing
    linux > source venv/bin/activate
    windows > venv/Script/activate.exe
4) Install dependencies
   pip install -r requirements.txt


## How to run

1) type >  python main.py to load the main program
           enter a client ID upon prompt
           type in your query to get results.

2) There is a test file. type python test.py to run it.
   This file contains query that are manually tested in Test.ipynb
   It will run those queries automatically and fetch the results.


## Supported Queries
1) Fetch transaction for a particular date
2) Fetch transactions between certain time period
3) Get total expenditure on a particular date
4) Get total expenduture during a time period
5) Get amount deposited on a particular date
6) Get amount deposited during a certain time period
7) Get transactions done for a certain category
8) Get transactions done for a certain category on certain date
9) Get transactions done for a certain category for certain period of time
10) Get amount credited for a certain category
11) Get amount credited for a certain category on certain date
12) Get amount credited for a certain category for certain period of time
13) Get amount debited for a certain category
14) Get amount debited for a certain category on certain date
15) Get amount debited for a certain category for certain period of time.
16) Get transactions done for a certain merchant
17) Get transactions done for a certain merchant on certain date
18) Get transactions done for a certain merchant for certain period of time
19) Get amount credited for a certain merchant
20) Get amount credited for a certain merchant on certain date
21) Get amount credited for a certain merchant for certain period of time
22) Get amount debited for a certain merchant
23) Get amount debited for a certain merchant on certain date
24) Get amount debited for a certain merchant for certain period of time.




## Some Thought Processing
1) Multiple bank ID signifies use of multiple banks withing same app, queries can be extended to search transaction via specific bank. If data is provided.

2) Currently Pandas dataframe is used for queriying data, however on scale, this data should be stored on database and DB queries should be used for different operations.

3) I used two different templates one to fetch intent and other to get date, because openAI's pricing is based on number of tokens. If we use one concatenated template cost will remain same. However in my experience template size is directly proportional to hullocinations. Small paragraph often gets best result from GPT models.  
