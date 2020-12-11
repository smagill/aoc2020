import re
import sys

def parse_word(w):
    return w.replace(" ","_")

def parse_word_contained(w):
    x = re.match("(\d+) (\w+ \w+) bags?",w)
    if x is None:
        print(w)
    num = x.group(1)
    word = parse_word(x.group(2))
    return (word,num)

def parse_contained(str):
    if str == "no other bags":
        return []
    lst = str.split(', ')
    return list(map(parse_word_contained,lst))

def extract_color(contained):
    return [contained[0]] * int(contained[1])

def gen_rule(container,contained):
    just_colors = list(map(extract_color, contained))
    just_colors = [x for sub_list in just_colors for x in sub_list]
    color_text = '[' + ', '.join(just_colors) +']'
    return "in({}, {}).".format(container,color_text)

if len(sys.argv) < 2:
    print("Usage: day7.py <day7_input_filename>")
    exit(-1)
filename = sys.argv[1]
f = open (filename,"r")
lines = f.readlines()
for line in lines:
    m = re.match("(\w+ \w+) bags contain (.*).",line)
    if m is None:
        continue
    container = parse_word(m.group(1))
    contained = parse_contained(m.group(2))
    print(gen_rule(container,contained))

print("""

color_in(X,Y) :- in(X,Z), member(Y,Z).

:- table transitive_in/2.
transitive_in(X,Y) :- color_in(X,Y).
transitive_in(X,Y) :- transitive_in(X,Z), transitive_in(Z,Y).

expand([],[]).
expand([BAG|BAG_LIST],EXPANSION) :-
    expand(BAG_LIST,LIST_EXPANSION),
    in(BAG,CONTENTS),
    append(CONTENTS,LIST_EXPANSION,EXPANSION).

tracing_transitive_expand(X,[],[]) :- expand(X,[]).
tracing_transitive_expand(X,Y,TRACE) :-
    expand(X,Z),
    tracing_transitive_expand(Z,Y,TRACE1),
    append(Z,TRACE1,TRACE).

size(X,Z) :-
    tracing_transitive_expand(X,_,TRACE),
    length(TRACE,Z).
""")