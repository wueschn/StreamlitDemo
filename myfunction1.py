import streamlit as st   

st.title("Mario Wüschner")


"""
# es gibt immer einen Funktionsnamen und werte als Übergabe
def func(wert1, wert2):
     mache was mit wert1  // wert1 wird verarbeitet
     mache was mit wert2 // wert2 wird verarbeitet
     x = ergebnis der Bearbeitung
     return x  // es wird ein Ergebnis rausgeworfen

# eine Funktion, die keine Werte bekommt
def func1():
    print("nur eine Ausgabe") # es wird etwas am Bildschirm gezeigt
    # es gibt kein Return

"""

# ich mache daraus eine Funktion
def addieren(z1,z2):
    sum = z1 + z2
    return sum

# Verwenden
print(addieren(200,900))

##klassisch
myName = "Mario Wüschner"
print(myName)

## eine Funktion machen
def ausgeben(na, adress, tel):
    return na, adress, tel

print(ausgeben("Hakan", "Kirchstrasse", "05577/1234567"))

zahl = 10
quadrat = zahl * zahl # quadrat = zahl ** 2
print(quadrat)

def quad(z1):
    erg = z1 ** 2
    return erg

print(quad(4))