import os
import builder as b
import general_methods as gms
import showcase_nft as show_off
import config as c

def grab_wallet():
    erc721_address = 'Enter Ethereum Address'
    art_wallet = b.buildIt(c.owner_addr)
    return art_wallet

def show_rando(wallet):
    rando = gms.random_art(wallet)
    show_off.show_art(rando)
    return ''

def do():
    wallet = grab_wallet()
    show_off.showcase(wallet)

def cleanup():
    exists = os.path.isfile('tmp.gif')
    if exists:
        os.remove('tmp.gif')
        print('Files cleaned up!')
