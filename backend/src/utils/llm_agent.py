from typing import Annotated
    
from llama_index.core.tools import FunctionTool
import os

from llama_index.tools.tavily_research.base import TavilyToolSpec
tavily_api_key = os.environ["tavily_key"]
tavily_tool = TavilyToolSpec(tavily_api_key )
#from llama_index.llms.vllm import Vllm

from transformers import AutoTokenizer , AutoModelForCausalLM , pipeline
import ctransformers as CT
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.agent.workflow import AgentWorkflow,FunctionAgent,ReActAgent


# def buy_actions(number_of_stocks : Annotated[str,"A number of stocks to be bought o nthe market"])->str:
#       """A function allowing a portfolio manager to buy stocks on the market

#       Args:
#          number_of_stocks (str): the number of stocks to be bought

#       Returns:
#          str: the number of bought actions
#        """
#       final_result = f"we bought {number_of_stocks} stocks"
#       return final_result
def load_models():
   
    llm = CT.AutoModelForCausalLM.from_pretrained('../../llms/Mistralv1.02',context_length = 5000 , hf = True  )




    tokenizer = AutoTokenizer.from_pretrained('../../llms/Mistralv1.02/tokenizer')

    return llm,tokenizer

async def run_agent(query : str , llm : HuggingFaceLLM , tokenizer : AutoTokenizer):

    #pipe = pipeline('text-generation', model=llm, tokenizer=tokenizer,max_new_tokens = 5000 ,device="cuda")
   hf = HuggingFaceLLM(model=llm, tokenizer= tokenizer, context_window=5000,max_new_tokens = 512)

   Query_agent=ReActAgent( name="Queryier",
                       tools = [tavily_tool.to_tool_list()[0] ] ,
                    llm=hf, verbose =True,
                       description= "an agent looking for info in the web , later on a database too",
                       system_prompt="You are an agent design either to answer directly to the user or \
                       to search in the web the info asked by the user using your tools. Please use at least 5 as max_result parameter in Tavily to help you.\
                        Please summarize the result in a clear final answer")

   result = await Query_agent.run(query)
   result = str(result)
   print('result : ',result)
   print('res type : ', type(result))

   return result
