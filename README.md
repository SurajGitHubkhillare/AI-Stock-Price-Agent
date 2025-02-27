📈 AI Stock Price & Market News Bot
A Streamlit-based AI-powered stock market assistant that fetches real-time stock prices, compares multiple stocks, and retrieves the latest financial news using Google Gemini AI and SerpAPI.

🚀 Features
✅ Fetch the latest stock prices in INR from NSE/BSE.
✅ Compare multiple stock prices side by side.
✅ Get summarized stock market news for any company.
✅ Powered by LangChain AI Agent + Google Gemini + SerpAPI.

🛠 Tech Stack
Python
Streamlit (Web App)
LangChain (AI Agent Framework)
Google Generative AI (Gemini-Pro)
SerpAPI (Real-time Search for Stock Prices & News)
Pyngrok (For public URL in Colab)
📌 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/AI-Stock-Price-Agent.git
cd AI-Stock-Price-Agent
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up API Keys
You'll need API keys for Google Gemini AI and SerpAPI:

Get Google Gemini API Key → Google AI Console
Get SerpAPI Key → SerpAPI Website
Set them in your environment:

bash
Copy
Edit
export GOOGLE_API_KEY="your_google_gemini_api_key"
export SERPAPI_API_KEY="your_serpapi_key"
▶️ Running the Application
🖥️ On Local Machine
bash
Copy
Edit
streamlit run app.py
☁️ On Google Colab (With ngrok)
Set up ngrok authentication:

python
Copy
Edit
from google.colab import userdata
ngrok_auth = userdata.get('ngrok_auth')

from pyngrok import ngrok
ngrok.kill()
ngrok.set_auth_token(ngrok_auth)
ngrok_tunnel = ngrok.connect(addr="5000", proto="http")
print("Tracking URI:", ngrok_tunnel.public_url)
Run the Streamlit app:

bash
Copy
Edit
!streamlit run --server.port 5000 app.py
💡 How to Use the App?
1️⃣ Open the Streamlit web UI.
2️⃣ Select an option from:

Fetch Latest Stock Price 🏦
Compare Multiple Stocks 📊
Get Stock Market News 📰
3️⃣ Enter stock/company names & click Submit.
4️⃣ Get real-time stock prices, comparisons, or news insights! 🚀
📽️ Video Walkthrough
🔗 Video Demo Link

📜 License
This project is open-source under the MIT License.

📧 Contact
Developed by Suraj Khillare
📩 Email: your-email@example.com
🔗 LinkedIn

