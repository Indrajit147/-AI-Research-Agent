from dotenv import load_dotenv # Load environment variables from a .env file, which typically includes API keys and other secrets
from pydantic import BaseModel # Import Pydantic's BaseModel to define a structured output format with validation
from langchain_openai import ChatOpenAI # Import OpenAI model wrapper for chat models using LangChain
from langchain_anthropic import ChatAnthropic # Import Anthropic model wrapper in case you want to use Claude instead of OpenAI (optional in this example)
from langchain_core.prompts import ChatPromptTemplate # Prompt templating class to structure the conversation with system/user/AI roles
from langchain_core.output_parsers import PydanticOutputParser # Output parser that converts raw model output to structured Pydantic model
from langchain.agents import create_tool_calling_agent, AgentExecutor # Agent creation and execution utilities to handle tool calls and manage the agent's workflow
from tools import search_tool, wiki_tool, save_tool # Importing your custom tools from a local module (search, wiki lookup, save function)
load_dotenv() # Load variables from .env file into environment — essential for accessing API keys securely


# Define the schema for the research output using Pydantic
# This ensures that the LLM's final response must follow this structured format
class ResearchResponse(BaseModel):
    topic: str         # The research topic or subject
    summary: str       # A short summary of the findings
    sources: list[str] # List of sources used during research
    tools_used: list[str]  # Names of tools (e.g., wiki, search) used to gather information

    
# Initialize the LLM, i could use either OpenAI or Anthropic models
# For this example, I will use OpenAI's GPT-4o-mini model.
llm = ChatOpenAI(model= "gpt-4o-mini") 
# Create a parser that will convert the LLM's output into a validated ResearchResponse object
# It will throw an error if the format is incorrect, so you can catch and debug
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"), # Placeholder for previous conversation (optional if not using memory)
        ("human", "{query}"), # User question
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions()) # Injects JSON format instructions expected by the parser

#Define the list of tools the agent can use.
# These tools are imported from your `tools.py` file and provide enhanced abilities like searching online or saving results.
tools = [search_tool, wiki_tool, save_tool]
# Create an intelligent agent
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# Create an executor that wraps the agent and actually runs it.
# This handles things like memory, verbose logging, and invoking the toolchain behind the scenes
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research? ") # Take user input (research question) from the command line
raw_response = agent_executor.invoke({"query": query}) # Run the agent with the user's query and collect the raw response.

# Try parsing the model output using the Pydantic parser.
# This will turn the model's raw string response into a structured Python object with attributes: topic, summary, etc.
try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)# If parsing fails (e.g., invalid format), show the error and raw response for debugging

