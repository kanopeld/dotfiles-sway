#!/usr/bin/env python3
import os
import re
import sys
import nmcli

DONE_OPTION = "done"
NM_SHOW_OPTION = "nm: show"
NM_WG_OPTION = "nm: show: wireguard"
NM_CON_OPTION = "con:"
NM_CON_DOWN_OPTION = "nmc: down:"
NM_CON_UP_OPTION = "nmc: up:"


NM_VPN_OPT = "vpn"
NM_WIFI_OPT = "wifi"


NO_DEVICE = "--"


def find_uuid_in_option(option):
    uuid = re.findall('(([0-9a-z]{4,12}-?){5})', option)
    if len(uuid) < 1:
        print("error: no match found by option '{}'".format(option))
        exit(1)
    return uuid[0][0]


def print_main_menu():
    print(NM_VPN_OPT)
    print(NM_WIFI_OPT)


def print_list_connections(connections, opt):
    for connection in connections:
        line = "{}({}) '{}'".format(connection.name, connection.conn_type, connection.uuid)
        if connection.device != NO_DEVICE:
            line += " interface: {}".format(connection.device)
        print("{}: {}".format(opt, line))


def is_active(connection) -> bool:
    return 'GENERAL.STATE' in connection and connection['GENERAL.STATE'] == 'activated'


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print_main_menu()
    else:
        option = sys.argv[1]
        if option == DONE_OPTION:
            sys.exit(0)

        if option == NM_VPN_OPT:
            print_list_connections([con for con in nmcli.connection() if con.conn_type == "wireguard"], NM_VPN_OPT) 
        elif re.match("^{}:\s".format(NM_VPN_OPT), option) is not None:
            print("!!!")


