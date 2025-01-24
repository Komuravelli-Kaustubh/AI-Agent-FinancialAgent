from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv
load_dotenv()

#web search agent
Sherlock_Holmes=Agent(
    name="Web Search Agent",
    role="Search the Web for Information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True
)


# Finance Agent
Harshad_Bhai = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,
                       company_news=True),
    ],
    instructions=["Use Tables to display the data"],
    show_tools_calls=True,
    markdown=True
) 

multi_ai_agent=Agent(
    team=[Sherlock_Holmes,Harshad_Bhai],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include Sources","Use Tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst recommendation and possible future for Szlon stock price",stream=True)
