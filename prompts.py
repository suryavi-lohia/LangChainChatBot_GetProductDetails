from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schema import AboutProduct

output_parser = JsonOutputParser(pydantic_object=AboutProduct)

prompt = PromptTemplate(
    template="Answer the user query\n{format_instruction}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instruction": output_parser.get_format_instructions()}
)
