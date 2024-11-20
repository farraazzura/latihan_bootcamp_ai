from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

# Ini AI OpenAI
os.environ['OPENAI_API_KEY'] = os.getenv('openai_api_key')
GPTLlm = ChatOpenAI(
    model='gpt-4o',
    temperature=0.2,
    api_key=os.environ['OPENAI_API_KEY']
)

# Ini AI Groq
os.environ['GROQ_API_KEY']=os.getenv('groqapi_key')
Groqllm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=os.environ['GROQ_API_KEY'],
    model_name="groq/llama3-8b-8192",
    temperature=0,
    max_tokens=1000,
)