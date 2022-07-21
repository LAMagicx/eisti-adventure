import json, os
from setup import printError
from creator import State

def listStates(): 
    if not os.path.exists("states/"):
        return {}
    else:
        files = {}
        for f in os.listdir("states/"):
            file = json.loads(open("states/"+f, 'r').read())
            if file['EDITABLE'] == 1:
                files.update({file['ID']:file['TITLE']})
        return files


def chooseState(files):
    not_valid_id = True
    while not_valid_id:
        print("Choose a state to add an option: ")
        for id_ in files:
            print(id_, files[id_])

        state_id = input("id: ")
        not_valid_id = state_id not in files 
        if not_valid_id:
            os.system("clear")
            printError("WARNING", "invalid id")
    
    return state_id
    

def Edit():
    files = listStates()
    if files:
        state_id = chooseState(files)
        State(state_id)
    else:
        printError("ERROR", "no editable states")


if __name__ == "__main__" :
    Edit()


