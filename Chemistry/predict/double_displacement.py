import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry
from mendeleev import element
from mendeleev.ion import Ion
from utils import get_charge  # Import the get_charge function

polypresent = False

def extract_elements(compound):
    # Regular expression to match element symbols and parentheses
    elements = re.findall(r'[A-Z][a-z]*|\([A-Za-z0-9]+\)', compound)
    return elements

def extract_polyions(compound, polyions):
    extracted_polyions = []
    for polyion in polyions:
        if polyion in compound:
            extracted_polyions.append(polyion)
            compound = compound.replace(polyion, '')
    return extracted_polyions, compound

while True:
    try:
        num_reactants = int(input("How many reactants are there? "))
        if num_reactants > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

reactant_elements = []
poly = ["OH", "NO3", "SO4", "CO3", "PO4", "NH4", "H3O", "HSO4", "H2PO4", "HPO4", "HSO3", "HCO3", "HNO2", "H2O2", "O2", "CN", "SCN", "MnO4", "Cr2O7", "CrO4", "AsO4", "AsO3", "VO3", "VO4", "SeO4", "SeO3", "TeO4", "TeO3", "ClO", "ClO2", "ClO3", "ClO4", "BrO", "BrO2", "BrO3", "BrO4", "IO", "IO2", "IO3", "IO4"]
reacnames = []
for i in range(num_reactants):
    compound = input(f"Please enter symbol or compound for reactant {i + 1}: ")
    reacnames.append(compound)
    polyions, compound = extract_polyions(compound, poly)
    reactant_elements.extend(extract_elements(compound))
    reactant_elements.extend(polyions)

print(reacnames)
print("Extracted elements and polyions:", reactant_elements)

# Calculate charges for the elements
charges = []
for elem in reactant_elements:
    charges.append(get_charge(elem, poly))

print("Charges before reordering:", charges)

# Reorder elements and charges
reactant_elements[1], reactant_elements[3] = reactant_elements[3], reactant_elements[1]
charges[1], charges[3] = charges[3], charges[1]
charges[0], charges[1], charges[2], charges[3] = charges[1], charges[0], charges[3], charges[2]

print("Reordered elements:", reactant_elements)
print("Reordered charges:", charges)

merge = [(0,2),(2,4)]
products = [''.join(reactant_elements[start:end]) for start, end in merge]
print(products)

if len(reactant_elements) < 2:
    print("Please enter at least two elements.")
else:
    products = []
    for i in range(0, len(reactant_elements), 2):
        element = reactant_elements[i]
        charge = abs(charges[i + 1])
        polyion = reactant_elements[i + 1]
        element_charge = abs(charges[i])
        if polyion in poly and charge > 1 and charge != element_charge:
            products.append(f"{element}({polyion}){charge}")
        elif polyion in poly and charge == element_charge:
            products.append(f"{element}{polyion}")
        else:
            products.append(f"{element}{polyion}{charge}")

    print(products)
    reac, prod = balance_stoichiometry(set(reacnames), set(products))
    reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
    products_str = " + ".join(f"{v}{k}" for k, v in prod.items())
    print(f"Balanced Equation: {reactants_str} -> {products_str}")