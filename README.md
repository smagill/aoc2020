# Advent of Code 2020 Solutions

Currently this just contains a Python script to generate the Prolog code needed to solve the Day 7 challenge.
To use it, store the day 7 challenge input in some text file (my input is included as input7.txt to serve as an example).
Then run the script to generate a Prolog input file.  The output just goes to standard out, so redirect to store it.
```
python3 day7.py input7.txt > day7.pl
```
Next start up SWI Prolog (available via apt, brew, etc.).
```
swipl
```
At the Prolog prompt, first load the file.
```
[day7].
```
The system should respond with `true`.  Next execute the query for Part 1.
```
findall(X,transitive_in(X,shiny_gold),Solutions), length(Solutions, Len).
```
The system should respond with the following.
```
Solutions = [shiny_lavender, posh_red, mirrored_salmon, shiny_yellow, dotted_white, plaid_yellow, bright_fuchsia, posh_salmon, dotted_yellow|...],
Len = 177.
```
The answer is 177.  Next solve Part 2.
```
size([shiny_gold],Z).
```
The system responds with "Z = 34988".  The answer is 34988.