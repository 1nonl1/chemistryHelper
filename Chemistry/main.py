import subprocess
from chempy import Substance

def main():
    print("Welcome to the element reference and calculator!")
    print("Please note that this program is still in development.\nAnd only works with elements.")
    c1 = input("Reference, conversions or equation? (r/c/e): ")
    if c1 == "r":
        ask = input("What element or compuound do you want to choose (Should look like this [Al2O3])? ")
        element = Substance.from_formula(ask)
        if element:
            print("Molecular Weight:", element.mass) 
            print("Composition:", element.composition) 
            print("Unicode Name:", element.unicode_name) 
        else:
            print("Element not found.")
    elif c1 == "c":
        from equations import conversions
        conversions()
    elif c1 == "e":
        balask = input("Do you want to balance the equation or predict products or both? (b/p/both): ")
        if balask == "b":
            subprocess.call(["python", "Chemistry/balance.py"])
        elif balask == "p":
            print("This feature is not yet available.")
            print("If you have any sugestions please say so in the discussions tab in the github page.")
        elif balask == "both":
            print("This feature is not yet available.")
            print("If you have any sugestions please say so in the discussions tab in the github page.")
    else:
        print("Invalid input.")     

if __name__ == "__main__":
    main()