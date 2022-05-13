# eisti-adventure
Text adventure journey though eisti. 

The aim of this project is to create a customizable cli text adventure game that is created by the students of EISTI. 

## COMMENTS

Need a global set of commands that you can enter:
look, search, go to, take, pick up...

For coding each 'senario / state' shall be represented by a single file, containing all the infomation about that action.

### Exemple : state_1.rpg

```json
{
  ID: 1,
  TEXT: "The corridor leads you to the dreaded room 218...",
  OPTIONS: {
    "enter the room" : 2,
    "continue" : ID_OF_NEXT_STATE
  },
  COMMANDS: {
    "look": "there is nothing to look for",
    "search":"..."
  },
  SCRIPT: game_script
}
```

```c
ID // the id of this state, used when 'jumping' to a diffent state
TEXT // the text to be displayed when the file is called
OPTIONS // if nessisary the options to choose from, each one will 'point' to a different state file using its ID
COMMANDS // using the global commands to add interaction in the game
SCRIPT // if nesisary can be used to start a game / challenge
```

At the end there sould be a binary tree with each of the different state ID's

![Binary Tree](https://www.cdn.geeksforgeeks.org/wp-content/uploads/binary-tree-to-DLL.png)

### More comments

Like to have a function that 'reads' these files, parses the text and finds the key infomation; ID, TEXT...
then with that info 'creates' the game.

In addition to that a file that creates these files could make it easier to write out the story.

In order to read and write just write it from scratch in C!

Choose between options and command or both.

### Future addtions

- scoring
- saving
