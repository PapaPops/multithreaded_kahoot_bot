from time import sleep
from random import randint as rand
from kahoot_bot import kahootBotInstance
from sys import exit 

def main():
    bots = []
    code = int(input("code? : "))

    nrOfBots = int(input("how many bots ? : "))

    if nrOfBots < 1:
        print("cannot have 0 or negative bots")
        exit(1)


    name = ""
    special_name = None


    while True:
        name = input("special names ?(y/n) : ")
        if name.lower() not in ["y","n"]:
            continue
        else: 
            break
    
    if name == "y":
       special_name = input("name ? : ")
       name = True
    else:
        name = False

    for i in range(nrOfBots):
        bots.append(kahootBotInstance())
    
    for i in range(nrOfBots):
        if name:
            bots[i].login(code,kahootBotInstance.make_specialized_name(special_name))
        elif not name:
            bots[i].login(code)
        

    while True:
        sleep(0.3)


        if bots[0].get_website() == "https://kahoot.it/v2/ranking":
            for i in range(len(bots)):
                bots[i].close()

        for i in range(len(bots)):
            bots[i].answer_question(rand(0,3))
            sleep(0.5)



if __name__ == "__main__":
    main()