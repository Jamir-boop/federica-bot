import os
from time import sleep
from federicabot import FedericaBot

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('WALLET_PASSWORD')
    bot = FedericaBot(email=email,
                      password=password,
                      dashboard_url="https://web.budgetbakers.com/dashboard")
    bot.login()
    bot.record()
    sleep(10)  # tiempo para insepeccionar
    bot.close()
