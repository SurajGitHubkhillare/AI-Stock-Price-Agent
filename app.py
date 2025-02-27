from google.colab import userdata
gemini_key=userdata.get('API_KEY')

import os
os.environ["GOOGLE_API_KEY"] = gemini_key

###########################################################################################################################
from google.colab import userdata
serpi_key=userdata.get('serpi_key')
# Set up SerpAPI key (Replace with your actual API key)
os.environ["SERPAPI_API_KEY"] = serpi_key

#############################################################################################################################
%%writefile app.py
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper


# Initialize Gemini AI model
gemini_llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)



# Initialize SerpAPI search tool
search = SerpAPIWrapper()
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Use this tool to search the internet for real-time stock prices, financial news, and comparisons."
)

# Define the agent with additional capabilities
agent = initialize_agent(
    tools=[search_tool],
    llm=gemini_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Streamlit UI
st.title("📈 AI Stock Price & Market News Bot")
st.write("Fetch the latest stock prices, compare multiple stocks, or get financial news summaries!")

# User selects a query type
query_type = st.selectbox(
    "What do you want to do?",
    ["Fetch Latest Stock Price", "Compare Multiple Stocks", "Get Stock Market News"]
)

if query_type == "Fetch Latest Stock Price":
    stock_name = st.text_input("Enter Stock Name (e.g., ICICI Bank, HDFC Bank)")
    if stock_name and st.button("Get Stock Price"):
        with st.spinner("Fetching latest stock price..."):
            query = f"Latest {stock_name} share price in INR on NSE/BSE (National Stock Exchange of India or Bombay Stock Exchange). Provide only the latest number."
            response = agent.run(query)
        st.success(f"📊 Latest Price: {response}")

elif query_type == "Compare Multiple Stocks":
    stock_names = st.text_input("Enter Stock Names (comma-separated, e.g., ICICI Bank, HDFC Bank, SBI)")
    if stock_names and st.button("Compare Stocks"):
        with st.spinner("Fetching stock comparisons..."):
            query = f"Compare the latest share prices of {stock_names} on NSE/BSE in INR."
            response = agent.run(query)
        st.success(f"📊 Stock Comparison:\n{response}")

elif query_type == "Get Stock Market News":
    company_name = st.text_input("Enter Company Name (e.g., ICICI Bank, TCS)")
    if company_name and st.button("Get Market News"):
        with st.spinner("Fetching latest market news..."):
            query = f"Summarize the latest news and stock performance of {company_name} in the last month."
            response = agent.run(query)
        st.success(f"📰 Latest News:\n{response}")

#############################################################################################################################
from google.colab import userdata
ngrok_auth=userdata.get('ngrok_auth')

#############################################################################################################################

from pyngrok import ngrok
ngrok.kill()
ngrok.set_auth_token(ngrok_auth)

# create the tunnel
ngrok_tunnel=ngrok.connect(addr="5000",proto="http")
print("Tracking uri:",ngrok_tunnel.public_url)

!streamlit run --server.port 5000 app.py
