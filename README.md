BINANCE FUTURES CLI TRADING BOT

1.  PROJECT OVERVIEW 
The Binance Futures CLI Trading Bot is a Python-based command line
application that allows users to place Futures orders on the Binance
Testnet platform.

This project demonstrates: - REST API integration - Secure API
authentication using HMAC SHA256 - Command Line Interface development
using Typer - Input validation and structured logging - Modular Python
project architecture


------------------------------------------------------------------------

2.  OBJECTIVES

-   Understand Binance Futures API workflow
-   Implement secure API key handling using environment variables
-   Build a structured CLI application
-   Validate user inputs before order execution
-   Maintain proper logging for debugging

------------------------------------------------------------------------

3.  TECHNOLOGY STACK Programming Language: Python 3.8+ CLI Framework:
    Typer HTTP Requests: Requests Library Environment Variables:
    python-dotenv API Platform: Binance Futures Testnet

------------------------------------------------------------------------

4.  PROJECT STRUCTURE

binance-futures-cli-bot/ 
    │ 
    ├── cli.py 
    ├── requirements.txt 
    ├── .env 
    ├──.gitignore 
    │ └── bot/ 
        ├── client.py 
        ├── orders.py 
        ├── validators.py 
        └──logging_config.py

------------------------------------------------------------------------

5.  INSTALLATION STEPS

Step 1: Clone Repository git clone
https://github.com/your-username/binance-futures-cli-bot.git 
cd binance-futures-cli-bot

Step 2: Create Virtual Environment 
Windows: 
python -m venv venv
venv\Scripts\activate

Mac/Linux: 
python3 -m venv venv 
source venv/bin/activate

Step 3: Install Dependencies 
pip install -r requirements.txt

------------------------------------------------------------------------

6.  CONFIGURATION

Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here

Note: - Do not share API keys. 
Add .env to .gitignore.

------------------------------------------------------------------------

7.  EXECUTION

Run the application using: 
python cli.py menu

------------------------------------------------------------------------

8.  ORDER TYPES SUPPORTED

-   MARKET Order
-   LIMIT Order
-   STOP Order

------------------------------------------------------------------------

9.  LOGGING

All API requests and responses are logged in:
 trading.log

------------------------------------------------------------------------


