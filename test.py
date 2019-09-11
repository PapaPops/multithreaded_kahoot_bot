import kahoot_bot
from time import sleep



bots = []

for i in range(4):
    bots.append(kahoot_bot.kahootBotInstance())

for i in range(len(bots)):
    bots[i].login(669664)

sleep(10)

for i in range(len(bots)):
    bots[i].close()