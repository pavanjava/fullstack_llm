from llama_index import SQLDatabase
from llama_index.llms import OpenAI
from llama_index.callbacks import CallbackManager, TokenCountingHandler
from llama_index import ServiceContext
from llama_index.indices.struct_store.sql_query import NLSQLTableQueryEngine
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
import os
import tiktoken

_ = load_dotenv(find_dotenv())


class Text2SqlAgent:
    def __init__(self):
        connection_string = os.getenv('POSTGRE_URI')
        engine = create_engine(url=connection_string)
        table_details = {
            "customers": "stores customer’s data.",
            "products": "stores a list of products along with their price details",
            "orders": "stores sales orders placed by customers.",
            "order_details": "stores sales order line items for each sales order.",
            "employees": "stores all employee information as well as the organization structure such as who reports to whom.",
            "suppliers": "stores the complete suppliers information along with their contact information",
            "categories": "stores different categories",
            "shippers": "stores the details of all shippers available"
        }
        sql_database = SQLDatabase(engine=engine, sample_rows_in_table_info=2)
        token_counter = TokenCountingHandler(tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode)
        callback_manager = CallbackManager([token_counter])
        llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
        service_context = ServiceContext.from_defaults(llm=llm, callback_manager=callback_manager)
        self.query_engine = NLSQLTableQueryEngine(sql_database=sql_database, service_context=service_context)

    def query(self, prompt):
        # query_str = "get me the order that has the highest order amount"
        response = self.query_engine.query(prompt)
        return {'result': response.response, 'query': response.metadata['sql_query']}
