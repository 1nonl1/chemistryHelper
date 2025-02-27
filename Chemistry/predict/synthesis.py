import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry
from mendeleev import element
from mendeleev.ion import Ion

def extract_elements(compound):
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

if len(reactant_elements) < 2:
    print("Please enter at least two elements.")
else:
    e1 = element(reactant_elements[0])
    e2 = element(reactant_elements[1])

    charges1 = [_.charge for _ in e1.ionic_radii]
    charges2 = [_.charge for _ in e2.ionic_radii]

    if charges1[0] == charges2[0]:
        elements = sorted([e1.symbol, e2.symbol])
        elements_with_charges = []
        if elements[0] == e1.symbol:
            elements_with_charges.append(elements[0])
            elements_with_charges.append(str(abs(charges2[0])))
            elements_with_charges.append(elements[1])
            elements_with_charges.append(str(abs(charges1[0])))
        else:
            elements_with_charges.append(elements[0])
            elements_with_charges.append(str(abs(charges1[0])))
            elements_with_charges.append(elements[1])
            elements_with_charges.append(str(abs(charges2[0])))
        elements_with_charges = [item for item in elements_with_charges if item != '1']
        
        sorted_elements = ''.join(elements_with_charges)
        
    else:
        elements = sorted([e1.symbol, e2.symbol])
        elements_with_charges = []
        if elements[0] == e1.symbol:
            elements_with_charges.append(elements[0])
            elements_with_charges.append(str(abs(charges2[0])))
            elements_with_charges.append(elements[1])
            elements_with_charges.append(str(abs(charges1[0])))
        else:
            elements_with_charges.append(elements[0])
            elements_with_charges.append(str(abs(charges1[0])))
            elements_with_charges.append(elements[1])
            elements_with_charges.append(str(abs(charges2[0])))
        elements_with_charges = [item for item in elements_with_charges if item != '1']
        sorted_elements = ''.join(elements_with_charges)
        

reac, prod = balance_stoichiometry(set(reacnames), set([sorted_elements]))
reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
products_str = "".join(f"{v}{k}" for k, v in prod.items())
print(f"Balanced Equation: {reactants_str} -> {products_str}")