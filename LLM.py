from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_groq import ChatGroq

# Import your API keys securely (consider using environment variables)
GOOGLE_API_KEY = "your-google-api-key"
ANTHROPIC_API_KEY = "your-anthropic-api-key"
MISTRALAI_KEY = "your-mistralai-key"
GROQ_API_KEY = "your-groq-api-key"

# Initialize models
gemini_model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
claude_model = ChatAnthropic(model='claude-3-opus-20240229', api_key=ANTHROPIC_API_KEY, temperature=0)
mistral_ai_model = ChatMistralAI(api_key=MISTRALAI_KEY)
llama3_8b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama3-8b-8192")
mixtral_8x7b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")
llama3_70b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")
gemma_7b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="gemma-7b-it")

# Model response functions
def gemini_response(prompt):
    response = gemini_model.invoke(prompt)
    return response.content

def claude_response(prompt):
    response = claude_model.invoke(prompt)
    return response.content

def mistral_ai_response(prompt):
    response = mistral_ai_model.invoke(prompt)
    return response.content

def llama3_8b_response(prompt):
    response = llama3_8b_model.invoke(prompt)
    return response.content

def mixtral_8x7b_response(prompt):
    response = mixtral_8x7b_model.invoke(prompt)
    return response.content

def llama3_70b_response(prompt):
    response = llama3_70b_model.invoke(prompt)
    return response.content

def gemma_7b_response(prompt):
    response = gemma_7b_model.invoke(prompt)
    return response.content


llm.py