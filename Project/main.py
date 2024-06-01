import json
import nltk
nltk.download('wordnet')
from helpers.data_fetcher import DataFetcher
from helpers.llm import chat
from helpers.templates import intent_find_template,date_find_prompt

def resolve_function(class_inst,method_name): # Since gpt outputs name of function this method extract gpt specified function from the class
    method = None
    try:
        method = getattr(class_inst, method_name)
    except AttributeError:
        raise NotImplementedError("Class `{}` does not implement `{}`".format(class_inst.__class__.__name__, method_name))

    return method


class TransactionHelperBot:
    def __init__(self,client_id) -> None:
        self.data_fetcher = DataFetcher(client_id)

    def _resolve_intent(self,query):
        intent,date = chat(intent_find_template,query),chat(date_find_prompt,query)
        return [json.loads(intent),json.loads(date)]
    
    def _fetch_result(self,resolved_query):
        definition,date = resolved_query[0],resolved_query[1]
        func = definition["intent"]
        method = resolve_function(self.data_fetcher,func) #Get appropriate function from the class to handle query
        category = definition.get("category",None)
            
        type = definition.get("type",None)
        if category: # Queries for Category or Merchant
            if type:    
                answer = method(type,category,date) # user interested in debit or credit queries
            else:
                answer = method(category,date) # user wants all transactions
        else:         # Transactions without category or merchant
            if type:
                answer = method(type,date) 
            else:
                answer = method(date)
        return answer
    
    def process_query(self,query):
        resolved = self._resolve_intent(query)  # Resolve the intent, as well as get date if specified
        result = self._fetch_result(resolved) # Get results based on intent and dates
        return result






if __name__=="__main__":
    print("Hello There! I am you transaction information guide.")
    client_id = input("Please enter your client id: ")
    client_id = int(client_id)
    thb = TransactionHelperBot(client_id)
    while True:
        query = input("Please enter your query: ")
        result = thb.process_query(query)
        print()
        print(result)
        print("#"*100)
        print("\n\n")