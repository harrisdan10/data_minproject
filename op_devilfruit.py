#!/usr/bin/env python3

import pandas as pd

def search(file, criteria, count):
    info = pd.read_csv(file, index_col=0)
    if "All" not in criteria:
        info.drop(info.columns.difference(criteria), 1, inplace=True)
    print(info.head(count))

    refine = []
    specify = ''
    while specify == '' and specify not in ["yes", "y"]:
        specify = input("Would you care to refine your search?\n").lower()
        if specify == "yes" or specify == "y":
            for c in criteria:
                refined = input(f'What {c} would you like to look up?\n').title()
                refine.append(refined)
        else:
            sys.exit()

    specific(file, criteria, refine)

def specific(file, criteria, refine):
    info = pd.read_csv(file, index_col=0)
    info.drop(info.columns.difference(criteria), 1, inplace=True)
    for c in criteria:
        for r in refine:
            refined = info.loc[info[c] == r]
    count = int(input("How many results would you like to see?\n"))
    print(refined.head(count))

def main():
    file = 'onepiecefruits.txt'
    print("Use me to look up data on devil fruits, their users, types, and states, and more...\n"
    "Information can be filtered by the following:\n\n"
    "[Devil Fruit] - a column containing the name of the fruit,\n"
    "[Class] - a column specifying the devil fruit class,\n"
    "[Subclass] - a column specifying an subclasses the fruit may have,\n"
    "[Awakened] - column informing whether the fruit is awakened or has awakening potential,\n"
    "[Status] - a column informing whether the fruit as ever been consumed]\n"
    "[All] - utilize no criteria, return all info\n\n"
    "Each request returns Characters associated with the fruit by default. \n")

    find=''
    count=''

    while len(find) == 0:
        find = input("What would you like to search by?\n" ).strip().title()
        criteria = [x.strip() for x in find.split(',')]
        print(criteria)
        
    while count == '' or count == 0:
        count = int(input("How many results would you like to get back? [1-179]:\n"))
        
    search(file, criteria, count)

if __name__ == "__main__":
    main()