import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

information = """

"""

if __name__ == '__main__':
    # print("hello LangChain!")
    # print(os.environ['OPENAI_API_KEY'])


    summary_template ='''
    given the LinkedIn information {information} about a person I want you to create:
    1. a very short summary
    2. two interesting facts
    '''

    summary_prompt_template = PromptTemplate(input_variables=["information"], template = summary_template)
    llm = ChatOpenAI(temperature=0,model_name="gpt-4o")
    # llm = ChatOllama(model="llama3")
    # llm = ChatOllama(model="mistral")
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/jorisfalter")

    res = chain.invoke(input={"information": linkedin_data})

    print(res)