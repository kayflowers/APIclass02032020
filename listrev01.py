#!/usr/bin/python3

def main():
    ##create an empty list
    emptylist = []

    emptylist.extend('192.168.102.55')
    print(emptylist)

    myotherlist = []
    myotherlist.append ('192.168.102.55')
    print(myotherlist)

    anotheremptylist = []
    anotheremptylist.extend('10.0.0.1', 'retro_game_server')
    print(anotheremptylist)
# get more focus on how extend works

    networklist = ["cisco","juniper"]
    emptylist.extend(networklist)
    print(emptylist)

if __name__ == "__main__":
    main()

    


