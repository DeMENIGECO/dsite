'''
= INDICE DEI SERVIZI DSITE =

Non modificate questo file, eccetto se si è
sviluppatore di DSite o se volete contribu-
ire al codice. Se siete utenti normali, NON
modificate questo file.
'''

INDEX = []

TH_SRVCS = []
SRVCS = []

def add_to_index(servc, third=False):
    if third:
        TH_SRVCS.append(servc)
    else:
        SRVCS.append(servc)

def update_index():
    global INDEX
    INDEX = TH_SRVCS + SRVCS
