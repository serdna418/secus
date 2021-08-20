import csv, random
from os import read


def test(term_and_defs):
    seen_td = {}
    while len(seen_td.keys()) != len(term_and_defs):
        td_index = random.randint(0,len(term_and_defs) - 1)
        if term_and_defs[td_index][0] in seen_td:
            seen_td[term_and_defs[td_index][0]] += 1
            print(term_and_defs[td_index][0], "has been used.")
        else:
           seen_td[term_and_defs[td_index][0]] = 1
    print(len(seen_td.keys()),seen_td)


def main():
    sec_notes = [term_def_list for term_def_list in csv.reader(open('/Users/serdna/Documents/pythonStuff/misc/sec_plus_test/test_sec_notes.txt', 'r'), delimiter=':')]
    test(sec_notes)
    
main()