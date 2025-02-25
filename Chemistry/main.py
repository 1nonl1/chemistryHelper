import subprocess
from chempy import Substance

def main():
    print("Welcome to the element reference and calculator!")
    print("Please note that this program is still in development.\nAnd only works with elements.")
    c1 = input("Reference, conversions,  or structures? (r/c/e/s): ")
    if c1 == "r":
        subprocess.call(["python", "Chemistry/reference.py"])
    elif c1 == "c":
        from Chemistry.stoichiometry import conversions
        conversions()
    elif c1 == "e":
        balask = input("Do you want to balance the equation or predict products or both? (b/p/both): ")
        if balask == "b":
            subprocess.call(["python", "Chemistry/predict/balance.py"])
        elif balask == "p":
            subprocess.call(["python", "Chemistry/predict/predict.py"])
        elif balask == "both":
            print("This feature is not yet available.")
            print("If you have any sugestions please say so in the discussions tab in the github page.")
    elif c1 == "s":
        subprocess.call(["python", "Chemistry/compStruct.py"])
    else:
        print("Invalid input.")     

if __name__ == "__main__":
    main()