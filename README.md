# eisti-adventure

Text adventure journey though eisti. 

The aim of this project is to create a customizable cli text adventure game that is created by the students of EISTI. 

## Concept

the concept behind this is too have a script (python) that runs the game. the game is composed of a number of json files where each file is named with a unique ID. Each file will represent a state/node. At each state, a text is read depicting the current state, a set options that will allow the user to move to a different state, a set of commmands that the user can execute that will say / do something and finally a script that will be executed after the text has been shown.

### Exemple : 1.json

```json
{
  "ID": 1,
  "TITLE": "This is a title",
  "TEXT": "The corridor leads you to the dreaded room 218...",
  "OPTIONS": {
    "enter the room" : 2,
    "continue" : "ID_OF_NEXT_STATE"
  },
  "COMMANDS": {
    "look": "there is nothing to look for",
    "search":"..."
  },
  "SCRIPT": "game_script",
  "EDITABLE": 0 / 1
}
```

### ID

the id will be a number incrementaly attributed to each new state. this will allow for states to jump to different states.

### TITLE

the state's title, useful when selecting a state to jump to.

### TEXT

the text that will be shown at the start of each state. this should depict the current surrounding of the area. 

### OPTIONS

these options will be state specific, allowing for a wide range of customisation. they should move the user onto a new state identified by the id. 

### COMMANDS

these will be a set of commands that the user can run whilst at this state, if it is a number then goto this state, needs to be thought about.

### SCRIPT 

an executable that can be launched by the the program to play a senario of some sort. 

### EDITABLE

whether or not anyone can edit the file or not



## PERMISSIONS

since there are multiple users creating and modifying states, a system of permissions are in place.

each python file is readable and executable but only writable by the host (me)

logs are only readable by the host but writeable only by running the script.

states are readable and writable by their owner, anyone else can't read or write unless using the program.




At the end there sould be a binary tree with each of the different state ID's

![Binary Tree](https://www.cdn.geeksforgeeks.org/wp-content/uploads/binary-tree-to-DLL.png)

## DONE

	- creation script is done, allowing the user to easily create a script

## TODO

### script that creates a state

	- makes it easier for the user to create states
	- easy way to 'select' the next state to jump to
	- cli obviously..
	- need to check if script if conform -> return value of script needs to be checked -> used for jumping to next state
	- check read/write permissions of script, need to be rw but the creator and ro to everyone else

### script that runs the program

	- starts with '0.json'
	- reads each state and depending on the user interaction reads a new file and loops
	- need to figure out end condition

## Future additions

	- a way to score ?
	- a way to save ?
	- edit state ?
	- a way to monitor who created a state and when ?


:)
