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

sp1 = 0
sp2 = 0


with open("sporsmaalsfil.txt", "r", encoding="UTF8") as fil:
    for l in fil:
        l = l.replace("[","")
        l = l.replace("]","")
        l = l.split(":")
        svaralt = l[2]
        svaralt = svaralt.split(",")
        n=1
        print(f"{l[0]}")
        for s in svaralt:
            print(f"{n}:{s}")
            n += 1        
        if __name__ == "__main__":
            spm = Sporsmaal(l[0], svaralt, int(l[1]))
            svar = int(input("Spiller 1: "))-1
            svar2 = int(input("Spiller 2: "))-1
            print(f"Korrekt svar er: {svaralt[int(int(l[1]))]}")
            if spm.sjekk_svar(svar)==True:
                print("\nSpiller 1: rett svar \n")
                sp1 = sp1 +1
            else:
                print("\nSpiller 1: Galt svar \n")
            if spm.sjekk_svar(svar2)==True:
                print("\nSpiller 2: rett svar \n")
                sp2 = sp2+1
            else:
                print("\nSpiller 2: Galt svar \n")
            print(f"Spiller 1 score: {sp1}")
            print(f"\nSpiller 2 score: {sp2}")
            
    print(f"\ntotal score for spiller 1: {sp1}")
    print(f"total score for spiller 2: {sp2}")
        
    