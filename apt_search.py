import pandas as pd
import os

data = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\thai_cert_apt_info.csv', sep=',', quotechar='"', encoding='utf8', na_values=[''])

def data_by_column(data):
    single_column = []
    for i in data:
        single_column.append(i)
    return single_column

def de_dupe_data(nested_list_to_de_dupe):
    simple_list = []
    for sublist in nested_list_to_de_dupe:
        for item in sublist:
            simple_list.append(item)
    return list(dict.fromkeys(simple_list))

def data_match(data,search_field):
    print "Type string to search for and hit return: \n"
    search = raw_input()
    print data[data[search_field].str.contains(search)]
    return

apt = [x.upper() for x in list(dict.fromkeys(data_by_column(data['apt'])))]
sector = [x.upper() for x in de_dupe_data(data_by_column(data['sector'].str.split(',')))]
technique = [x.upper() for x in de_dupe_data(data_by_column(data['techniques'].str.split(',')))]

def print_menu():

    print "\n1: Print all apts"
    print "2: Print all sectors"
    print "3: Print all techniques"
    print "4: Search all by apt name"
    print "5: Search all by technique"
    print "6: Search all by sector"
    print "7: Exit"

def search_string():
    print "What do you want to search for: \n"
    return

def a():
    return apt
def b():
    return sector
def c():
    return technique
def d():
    return data_match(data,  "apt")
def e():
    data_match(data, "techniques")
    return
def f():
    data_match(data, "sector")
    return
def g():
    exit()

def menu_choice():
    print_menu()
    choice = input()
    switch = {
        1: a,
        2: b,
        3: c,
        4: d,
        5: e,
        6: f,
        7: g,
    }
    func = switch.get(choice, lambda: "Not a choice")
    print func()

while True:
    menu_choice()
