from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
API_KEY = ""

llm = ChatOpenAI(api_key="API_KEY")
output_parser = StrOutputParser()

def chat(template,message):
    prompt = ChatPromptTemplate.from_messages( [
    ("system", template),
    ("user", "{input}")
    ])
    prompt.input_variables.pop(0)
    chain = prompt | llm | output_parser

    response = chain.invoke({"input": message})
    return response
