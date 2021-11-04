#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:09:40 2021

@author: natalijakovljevic
"""

from oving8bc import Sporsmaal

def les_sporsmaal():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as tekstfil:
        liste_sporsmaal = list()
        for linje in tekstfil:
            oppdeltlinje = linje.split(":")
            alternativer = oppdeltlinje[2].strip("[]\n ")
            alternativer = alternativer.split(", ")
            liste_sporsmaal.append(Sporsmaal(oppdeltlinje[0], alternativer, oppdeltlinje[1]))
    return liste_sporsmaal
