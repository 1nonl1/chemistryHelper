import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry
from mendeleev import element
from mendeleev.ion import Ion

def extract_elements(compound):
    # Regular expression to match element symbols
    return re.findall(r'[A-Z][a-z]*', compound)

while True:
    try:
        num_reactants = int(input("How many reactants are there? "))
        if num_reactants > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

reactant_elements = []
reacnames = []
for i in range(num_reactants):
    compound = input(f"Please enter symbol or compound for reactant {i + 1}: ")
    reacnames.append(compound)
    reactant_elements.extend(extract_elements(compound))
print(reacnames)
print("Extracted elements:", reactant_elements)
reactant_elements[1], reactant_elements[3] = reactant_elements[3], reactant_elements[1]
print("Reordered elements:", reactant_elements)
merge = [(0,2),(2,4)]
products = [''.join(reactant_elements[start:end]) for start, end in merge]
print(products)

if len(reactant_elements) < 2:
    print("Please enter at least two elements.")
else:
    e1 = element(reactant_elements[0])
    e2 = element(reactant_elements[1])
    e3 = element(reactant_elements[2])
    e4 = element(reactant_elements[3])

    charges1 = [_.charge for _ in e1.ionic_radii]
    charges2 = [_.charge for _ in e2.ionic_radii]
    charges3 = [_.charge for _ in e3.ionic_radii]
    charges4 = [_.charge for _ in e4.ionic_radii]
    print(charges1[0], " + ", charges2[0], " + ", charges3[0], " + ", charges4[0])
products = [reactant_elements[0], str(abs(charges2[0])), reactant_elements[1], str(abs(charges1[0])), reactant_elements[2], str(abs(charges4[0])), reactant_elements[3], str(abs(charges3[0]))]
merge2 = [(0,4),(4,8)]
products = [''.join(products[start:end]) for start, end in merge2]
print(products)
reac, prod = balance_stoichiometry(set(reacnames), set(products))
reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
products_str = " + ".join(f"{v}{k}" for k, v in prod.items())
print(f"Balanced Equation: {reactants_str} -> {products_str}")
