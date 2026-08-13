import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from duckduckgo_search import DDGS
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# We will expect the GEMINI_API_KEY in the environment or .env file

OBSIDIAN_MD_PATH = r"C:\Users\USER\Documents\Obsidian Vault\5ers RAG\faq_data.md"

class RAGAgent:
    def __init__(self):
        # We handle case where api key is missing
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.vectorstore = None
        self.retriever = None
        self.llm = None
        if self.api_key:
            self._init_agent()
            
    def _init_agent(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=self.api_key, temperature=0)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=self.api_key)
        
        # Load documents
        if not os.path.exists(OBSIDIAN_MD_PATH):
            print(f"Warning: {OBSIDIAN_MD_PATH} not found. Vector store will be empty.")
            texts = []
        else:
            loader = TextLoader(OBSIDIAN_MD_PATH, encoding='utf-8')
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(docs)
            
        # Initialize Vector Store
        self.vectorstore = Chroma.from_documents(documents=texts, embedding=self.embeddings, persist_directory="./chroma_db")
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 4})

    def web_search(self, query: str) -> str:
        """Fallback tool to search the web using DuckDuckGo."""
        print(f"Performing web search for: {query}")
        try:
            results = DDGS().text(query, max_results=3)
            return "\n\n".join([f"Title: {r['title']}\nBody: {r['body']}" for r in results])
        except Exception as e:
            return f"Web search failed: {str(e)}"
            
    def get_answer(self, query: str) -> str:
        if not self.api_key:
            return "Error: GEMINI_API_KEY is not set. Please provide a Google Gemini API Key in the backend/.env file."
            
        # Retrieve context
        docs = self.retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Step 1: Check if answer is in context
        eval_prompt = f"""
        You are an evaluator. Determine if the following context provides the exact answer to the user's question.
        Context: {context}
        Question: {query}
        If the context provides a confident and accurate answer, output "YES". 
        If it does not provide enough information or is uncertain, output "NO".
        Output ONLY YES or NO.
        """
        eval_res = self.llm.invoke(eval_prompt).content.strip().upper()
        
        if "YES" in eval_res:
            prompt = f"""
            You are an expert support agent for The 5ers.
            Use the following pieces of retrieved context to answer the question exactly.
            If you don't know the answer, just say that you don't know.
            Context: {context}
            Question: {query}
            Answer:
            """
            return self.llm.invoke(prompt).content
        else:
            # Step 2: Web Search Fallback
            web_context = self.web_search(f"The 5ers {query}")
            fallback_prompt = f"""
            You are an expert support agent for The 5ers.
            The internal FAQ didn't have the answer, so a web search was performed.
            Use the following web search results to answer the question exactly.
            If the web search results do not contain the answer or you lack necessary data, clearly state: "I cannot answer the question because I lack the necessary data."
            Web Search Results: {web_context}
            Question: {query}
            Answer:
            """
            return self.llm.invoke(fallback_prompt).content
