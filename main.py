from time import sleep
from federicabot import FedericaBot

if __name__ == "__main__":
    bot = FedericaBot(email="jeisereljamir@gmail.com",
                      password="!rZtuqQG*eWQfq*GTR5#h$T$7to4pf",
                      dashboard_url="https://web.budgetbakers.com/dashboard")
    bot.login()
    bot.record()
    sleep(10)  # tiempo para insepeccionar
    bot.close()
