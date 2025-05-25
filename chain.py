import os
from langchain_groq import ChatGroq


from prompts import prompt, output_parser

# Load environment variables (make sure these are set in your environment or .env)
os.environ["LANGCHAIN_TRACING_V2"] = "true"

model = ChatGroq(model="gemma2-9b-it")

# Combine prompt -> model -> output parser
chain = prompt | model | output_parser

def run_chain(query: str):
    return chain.invoke({"query": query})
