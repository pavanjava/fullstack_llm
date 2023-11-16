import os

from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import MilvusVectorStore
from llama_index.text_splitter import SentenceSplitter
from llama_index.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
import logging

_ = load_dotenv(find_dotenv())
logger = logging.getLogger('uvicorn')


class KnowledgeAgent:
    def __init__(self, path):
        logger.info(f'path: {path}')
        # open ai initialization
        llm = OpenAI(model='gpt-4-1106-preview', temperature=0.0)
        # load documents
        documents = SimpleDirectoryReader(input_dir=path, required_exts=['.pdf']).load_data()
        vector_store = MilvusVectorStore(dim=1536, overwrite=False, collection_name=os.getenv('COLLECTION_NAME'),
                                         uri=os.getenv('DB_URI'))
        sentence_splitter = SentenceSplitter(chunk_size=1536, chunk_overlap=200)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        service_context = ServiceContext.from_defaults(llm=llm, text_splitter=sentence_splitter)
        # save the documents index to vector store
        self.index = VectorStoreIndex.from_documents(service_context=service_context, storage_context=storage_context,
                                                     documents=documents)

    def query(self, user_query):
        try:
            logger.info(f'query: {user_query}')
            query_engine = self.index.as_query_engine()
            response = query_engine.query(str_or_query_bundle=user_query)
            logger.info(f'response: {response.response}')
            return response.response
        except Exception as e:
            raise Exception(e.__cause__)
