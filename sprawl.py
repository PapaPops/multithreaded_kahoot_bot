from kahoot_bot import kahootBotInstance
from sys import exit

lookup_table = {
    "r":0,
    "b":1,
    "y":2,
    "g":3
}
def main():
    code = int(input("code? : "))
    nr_of_bots = int(input("how many bots ? : "))

    bots = []

    if nr_of_bots<1:
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

    for i in range(nr_of_bots):
        bots.append(kahootBotInstance())

    for i in range(nr_of_bots):
        if name:
            bots[i].login(code,kahootBotInstance.make_specialized_name(special_name))
        elif not name:
            bots[i].login(code)


    while True:
        answer = input("answer ? : ")
        answer = answer.lower()
        if answer not in ["r","b","g","y"]:
            continue

        elif answer in ["close","exit","stop"]:
            break

        else:
            for i in range(len(bots)):
                bots[i].answer_question(answer = lookup_table[answer])


    for i in range(len(bots)):
        bots[i].close()

    exit(0)    
    

if __name__ == "__main__":
    main()
