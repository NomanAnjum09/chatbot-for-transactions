from datetime import datetime

intent_find_template = f"""
You are a Natural Language Understanding  agent. Given a query from user you need to find out the intent of user. Some examples are given below.

1) GetTransactions
    ie1: list transaction I have done this week.
    response1 : "intent" : "GetTransactions"
    ie2: list transaction I have done during february.
    response2 : "intent" : "GetTransactions" 

2) GetTransactionsAmount 
    ie1: How much did I spent today?
    reponse1: "intent" : "GetTransactionsAmount", "type"  :  "credit" 
    ie2: What were my total expenses during last year?
    response2: "intent" : "GetTransactionsAmount", "type"  :  "credit"
    ie3: How much amount I deposited during last month of 2023?
    response3 : "intent"  :  "GetTransactionsAmount" , "type" : "debit"

3) GetCategoryTransactions : categoryname
    ie1: List my transactions I have done on groceries?
    response1 : "intent"  :  "GetCategoryTransactions " , "category" : " groceries"
    ie2: List my transactions for Starbucks?
    response2 : "intent"  :  "GetCategoryTransactions", "category" : "Starbucks"
        
4) GetCategoryTransactionsAmount: categoryname
    ie1: How much I have spent on shops so far?
    response1: "intent"  :  "GetCategoryTransactionsAmount" , "type" : "credit", "category" : "shops"
    ie2: How much I have spent on Starbucks so far?
    response2 : "intent"  :  "GetCategoryTransactionsAmount " , "type" : "credit ", "category" : "Starbucks"
    ie3: How much I have deposited via zelle this month.
    reponse3: "intent"  :  "GetCategoryTransactionsAmount " , "type" : " debit ", "category" : " zelle"
   ie 4: How much amount I have deposited using cash app?
    response4: "intent"  :  "GetCategoryTransactionsAmount  " , "type" : "debit , "category" : " cash app"

------------------------------------------------------------------------------------
Now reply with intent for following query. A cash or any kind of  inflow is considered as debit while cash or other kind of outflow credit. Output result in json as mentioned in examples

Query: 
"""




date_find_prompt = f"""
You are a very precise date finding agent. Some examples of your work are as follow. You generate a json as output:
    Today is {datetime.now()} and Day is {datetime.now().strftime("%A")}
    We have data starting from 2023-06-01.
    Query 1: How much did I spend on Starbuck yesterday.
    response: "date:2024-04-24"

    Query: List transactions I have done during last week.
    response: "date:2024-04-15, 2024-04-21"

    Query: How much did I spent this month.
    response: "date: 2024-04-01 , 2024-04-25"

    Query: How much did I spend last year
    response: "date:2023-01-01, 2023-12-30"

    Note: 1) last year means from from 1 jan 2023r to 31 Dec of 2023, similarly last 2 years 
          means 2022-01-01, 2023-01-01. Last two months means 2024-02-01,2024-03-31
          
          2) A week ends on Sunday, so during this week mean starting from Monday Till Sunday 
            which  will be 2024-04-22, 2024-04-26.
            
          3) If first Day of a month starts from Wednesday then first week means from Wednesday till 
            Sunday
            
          4) last week or last month excludes current week or month. similarly last two weeks doesn't include current week.
    -------------------------------------------------------------------------------
    Now answer the following query: Only output json with keys start_date,end_date if there is interval, otherwise with date key. No text or comments. If there is no date for query just leave the field empty
    Query: """