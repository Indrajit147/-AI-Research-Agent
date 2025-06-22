from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun # Import prebuilt tool interfaces from LangChain Community integrations
from langchain_community.utilities import WikipediaAPIWrapper # Import the Wikipedia API wrapper to configure how Wikipedia search works
from langchain.tools import Tool # Generic Tool wrapper from LangChain used to define custom or wrapped tools
from datetime import datetime # Import datetime for timestamping when saving to file

# Custom Python function to save research data to a .txt file
def save_to_txt(data: str, filename: str = "research_output.txt"): 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get current date and time in a readable format
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n" # Format the content with a header and timestamp for readability

    # Open the file in append mode and write the formatted content
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}" # Return a confirmation message (this becomes the tool's output)

# Wrap the custom save function as a LangChain tool
# This allows the agent to call this function when it decides to save data
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

# Instantiate a DuckDuckGo search tool from the community pack
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search", # Tool name exposed to the agent
    func=search.run, # The method that runs the query
    description="Search the web for information",
)

# Create a Wikipedia API wrapper to fetch 1 top result, limited to 100 characters
# This helps reduce verbose outputs and keeps results concise for quick summary
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper) # Create a tool to query Wikipedia using the above wrapper