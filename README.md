### README.md

Hi! This is AoCUtilsDenz the short form of *"Advent of Code Utilities by Denzven"* its a small automation tool (WIP) to make it easier for people to solve the questions of AoC and organize and neaten up their code in the challenge.

for now, the code makes a boilerplate file system with all years ie,(2015 to 2020) and all days (Day0 - Day25) all the Day0 days are empty and are kept as a place holder:

the file tree system are as follows:

```html
D:.
|
\---AdventOfCode
    +---<year>
    |   +---<day>
    |   |       <day>Input.txt ()
    |   |       <day>Part1.py
    |   |       <day>Part2.py
    |   |       <day>Ques.txt
    |   |       README_<day>.md
    |   |
    |   \---<day>
    |	       <day>Input.txt
    |	       <day>Part1.py
    |	       <day>Part2.py
    |	       <day>Ques.txt
    |	       README_<day>.md
```
see the whole file system at [tree_fig.txt](https://github.com/denzven/AoCUtils_Denz/blob/main/tree_fig.txt)

In addition to the file system, it fills the `<day>Input.txt` with the input of the puzzle using a SessionID [see here for more info]()
and fills `<day>Part1.py` and `<day>Part2.py` with some boiler plate code like this:

```py
#Part <part> of Day<day>

import time
StartTime = time.time()
InputFileLines = open('Day<day>Input.txt').readlines()

#Code

FinalAnswer = 

EndTime = time.time()
print(f"Final score: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')
```

This code dynamically changes adding the <part> and <day> in each file.

This project is still in WIP and I have planned to add a lot more funtions and features to make solving these puzzles easier and not a headache in organising hundreds of files :)

Please Note that right now the code is *extremely slow* taking about [300 to 350 seconds](https://github.com/denzven/AoCUtils_Denz/blob/main/cmd_output.txt#L198) to complete from start to finish (about 5-6 mins approx.)


Please do Star the repo if you found it useful [⭐](https://github.com/denzven/AoCUtils_Denz)

If you feel something needs to be added, open a issue to put in the suggestion or fork the repo and make a pull request 💜

Made by [Denzven](https://github.com/denzven/) with love 💜 and [Python](https://github.com/topics/python)  


### Dislaimer
```
I DO NOT RECOMMEND TO USE THIS TOOL TO ABUSE AND CAUSE DAMAGE TO AOC SERVERS/PARTICPANTS ETC.  
USE THIS JUSDICIOUSLY AND UNDER STRICT OBSERVATION.  

I DO NOT TAKE RESPONSIBILITY OF ANY DAMAGE OCCURED TO ANY PERSON   
OR PROPERTY OR ANY ACCOUNT BANNED FROM AOC.  

PLEASE USE CAUTIOUSLY AND CAREFULLY, UNDERSTANDING ALL RISKS INVOLVED  

THANK YOU,
REGARDS,
DENZVEN
```