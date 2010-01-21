#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_main():
    print ""
    print "================================================================================"
    print "Escolha a opção"
    print "================================================================================"
    print ""
    print "add <host> <modelo>          adiciona host"
    print ""
    print ">>",

def get_input():
    cmd = str.split(raw_input())
    return cmd if len(cmd) > 0 else 1

def main():
    host = "ae.local"
    port = 12345
    while True:
        print_main()
        cmd = get_input()
        if cmd == 1: # erro
            print "Entrada inválida"
        elif cmd[0] == 'add':
            comando = "ssh %s -p %d" % (host, port)
            print comando

if __name__ == '__main__':
    main()
