

from main import TransactionHelperBot


if __name__=="__main__":
    client_id = 880
    queries = [
        "How much did I spent on empower during august 2023",
        "What are my transactions on moneylion so far.",
        "List my transaction during july 2023",
        "How much I deposited during 2023",
        "How much I added to my account between march and july 2023",
        "How much did I spend between march and july 2023",
        "How much Did I spend on 1st day of september 2023"
        
    ]
    thb = TransactionHelperBot(client_id)
    for query in queries:
        result = thb.process_query(query)
        print(result)
        print("#"*100)