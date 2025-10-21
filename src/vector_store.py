from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os


# Load environment variables
current_dir = os.path.dirname(os.path.abspath("__file__"))  
base_dir = os.path.dirname(current_dir)
env_path = os.path.join(base_dir, "api.env")
load_dotenv(env_path)


class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_dir: str = "chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vectorstore(self):
        # Load CSV data
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )
        data = loader.load()

        # Split text into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        # Build Chroma vector store
        db = Chroma.from_documents(texts, self.embedding, persist_directory=self.persist_dir)

        # Save database
        db.persist()

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)