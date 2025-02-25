import subprocess

def balance():
    ask = input("decomposition, synthesis, or double displacement, single displacement? (d/s/dd/sd): ")
    if ask == "s":
        subprocess.call(["python3", "Chemistry/predict/synthesis.py"])
    elif ask == "d":
        subprocess.call(["python3", "Chemistry/predict/decomposition.py"])
    elif ask == "dd":
        subprocess.call(["python3", "Chemistry/predict/double_displacement.py"])
balance()