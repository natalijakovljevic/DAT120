#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:08:56 2021

@author: natalijakovljevic
"""


class Sporsmaal:
    def __init__(self, spørsmål, alternativ, tall=0):
        self.sporsmaal = spørsmål
        self.alternativ = alternativ
        self.tall = tall
        

    def sjekk_svar(self, svaret):
        if int(svaret) == int(self.tall):
            return True
        else:
            return False
        
#e

    def korrekt_svar_tekst(self, svaret):
        if svaret == self.tall:
            print(svaret)

        
        


#d og e




with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fil:
    for l in fil:
        l = l.replace("[","")
        l = l.replace("]","")
        l = l.split(":")
        svaralt = l[2]
        svaralt = svaralt.split(",")
        n=1
        print(f"{l[0]}")
        print(int(l[1])+1) # Slett
        for s in svaralt:
            print(f"{n}:{s}")
            n += 1        
        if __name__ == "__main__":
            spm = Sporsmaal(l[0], svaralt, int(l[1]))
            svar = int(input("Velg svaralternativet: "))-1            
            if spm.sjekk_svar(svar)==True:
                print("\n rett svar \n")
            else:
                print("\n Galt svar \n")
    