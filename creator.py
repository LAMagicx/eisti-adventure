import json, os
from setup import printError

# finds the next id by finding the last max id used then add 1
def calculateId():
    existing_ids = [-1]
    for f in os.listdir('states/'):
        file_name, ext = os.path.splitext(f)
        if ext == 'json':
            try:
                existing_ids.append(file_name)
            except:
                printError('WARNING', 'file: {} not conform'.format(file_name))
        else:
            printError('WARNING', 'file {} not json type'.format(file_name))
    return max(existing_ids) + 1

class State:
    def __init__(self):
        self.id = calculateId()
        self.title = ''
        self.text = ''
        self.options = {}
        self.commands = {}
        self.script = {}
        self.fillState()

    def fillState(self):
        while True:
            os.system('clear')
            print("""
                    State ID: {0}
                    1 - Title: {1}
                    2 - Text: {2}
                    3 - Options: {3}
                    4 - Commands: {4}
                    5 - SCRIPT: {5}
                    """.format(
                        self.id,
                        self.title,
                        self.text,
                        json.dumps(self.options),
                        json.dumps(self.commands),
                        self.script
                     )
                 )
            choice = int(input("Choose what you would like to do: [1-5]\n> "))
            if choice == 1:
                self.setTitle()
            elif choice == 2:
                self.setText()
            elif choice == 3:
                self.setOptions()
            elif choice == 4:
                self.setCommands()
            elif choice == 5:
                self.setScript()
            elif choice == 6:
                break
            else:
                print("Not a valid choice please choose a number between [1-5]")
    def setTitle(self):
        self.title = input('Title: ')

    def setText(self):
        self.text = input('Text: ')

    def setOptions(self):
        while True:
            print('Options:')
            print(json.dumps(self.options))
            print("""
                    1 - add option
                    2 - edit option
                    3 - delete option
                    4 - exit
                    """)
            choice = int(input('What would you like to do ?'))
            if choice == 1:
                self.createOption()
            elif choice == 4:
                break
            else:
                print('choice not an option')

    def createOption(self):
        text = input('Option text: ')
        id_ = int(input('Id of next state: '))
        self.options.update({text: id_})

    def setCommands(self):
        while True:
            print('Commands:')
            print(json.dumps(self.commands))
            print("""
                    1 - add command
                    2 - edit command
                    3 - delete command
                    4 - exit
                    """)
            choice = int(input('What would you like to do ?'))
            if choice == 1:
                self.createCommand()
            elif choice == 4:
                break
            else:
                print('choice not an option')

    def createCommand(self):
        text = input('Command: ')
        response = int(input('Command response: '))
        self.commands.update({text: response})

    def setScript(self):
        scripts = os.listdir('scripts/')
        print("0 - enter path for script")
        for i, f in enumerate(scripts):
            print(i, '-', f)
        choice = int(input('What script: '))
        # check choice
        if choice == 0:
            self.script = input('Script name: ')
        else:
            self.script = scripts[choice]
