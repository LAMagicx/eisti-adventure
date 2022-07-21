import json,os
from setup import log

def getState(id_='0'):
    return json.loads(open("states/"+id_+".json", 'r').read())

def showState(data):
    os.system("clear")
    print(
"""{0}

{1}

""".format(data["TITLE"], data["TEXT"])
    )
    if data["OPTIONS"]:
        print("Options: ")
        for i,o in enumerate(data["OPTIONS"]):
            print("{0} - {1}".format(i, o))

    if data["COMMANDS"]:
        print("Commandes: ")
        for i,o in enumerate(data["COMMANDS"]):
            print("{0} - {1}".format(i+len(data["OPTIONS"]), o))
    print("")


def run():
    data = getState()
    running = True
    while running:
        showState(data)
        choice = input(" > ")
        if choice.isdigit():
            if int(choice) < len(data["OPTIONS"]):
                choice_key = list(data["OPTIONS"].keys())[int(choice)]
            elif int(choice) - len(data["OPTIONS"]) < len(DATA["COMMANDS"]):
                choice_key = list(data["COMMANDS"].keys())[int(choice) - len(DATA["OPTIONS"])]
            else:
                choice_key = -1
        else:
            if choice in data["OPTIONS"]:
                choice_key = choice
            elif choice in data["COMMANDS"]:
                choice_key = choice
            else:
                choice_key = -1
        if choice_key == -1:
            print(choice)
        else:
            print(choice_key)
        break



if __name__ == "__main__" :
    run()
