#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:42:50 2021

@author: natalijakovljevic
"""



class Flervalgsprsml:
    def __init__(self, sporsmaal, svaralternativ, verdi):
        self.sporsmaal = sporsmaal
        self.svaralternativ = svaralternativ        
        self.verdi = verdi

    def __str__(self):
        return f"{[self.svaralternativ]}: {self.verdi}"

    def sjekk_svar(self, sjekk):
        if self.verdi == sjekk:
            return f"Alternativ {sjekk} er riktig svar"
        else:
            return f"Alternativ {sjekk} er ikke korrekt"

if __name__ == "__main__":
    sporsmaal = "Hvor mange bein har en hund?"
    print(f"\nSpørsmål 1: {sporsmaal} \n")
    liste1 = ["1", "2", "3", "4"]
    print(f"Alternativ 1: {liste1[0]} \n")
    print(f"Alternativ 2: {liste1[1]} \n")
    print(f"Alternativ 3: {liste1[2]} \n")
    print(f"Alternativ 4: {liste1[3]} \n")
    svar1=Flervalgsprsml(sporsmaal, liste1, "4")
    svar = input("svar: ")
    print(svar1.sjekk_svar(svar))

    sporsmaal = "Hva er hovedstaden i Spania?"
    print(f"\nSpørsmål 1: {sporsmaal} \n")
    liste1 = ["London", "Madrid", "Berlin", "Paris"]
    print(f"Alternativ 1: {liste1[0]} \n")
    print(f"Alternativ 2: {liste1[1]} \n")
    print(f"Alternativ 3: {liste1[2]} \n")
    print(f"Alternativ 4: {liste1[3]} \n")
    svar1=Flervalgsprsml(sporsmaal, liste1, "2")
    svar = input("svar: ")
    print(svar1.sjekk_svar(svar))
