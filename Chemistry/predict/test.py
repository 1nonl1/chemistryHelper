import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry
from mendeleev import element
from mendeleev.ion import Ion

polypresent = False

def extract_elements(compound):
    elements = re.findall(r'[A-Z][a-z]*', compound)
    return elements

def extract_polyions(compound, polyions):
    extracted_polyions = []
    for polyion in polyions:
        if polyion in compound:
            extracted_polyions.append(polyion)
            compound = compound.replace(polyion, '')
    return extracted_polyions, compound

def get_charge(compound, polyions):
    charge = 0
    if compound in polyions:
        if compound == "NH4":
            charge = 1
        elif compound == "OH":
            charge = -1
        elif compound == "NO3":
            charge = -1
        elif compound == "SO4":
            charge = -2
        elif compound == "CO3":
            charge = -2
        elif compound == "PO4":
            charge = -3
        elif compound == "HSO4":
            charge = -1
        elif compound == "H2PO4":
            charge = -1
        elif compound == "HPO4":
            charge = -2
        elif compound == "HSO3":
            charge = -1
        elif compound == "HCO3":
            charge = -1
        elif compound == "HNO2":
            charge = -1
        elif compound == "H2O2":
            charge = 0
        elif compound == "O2":
            charge = 0
        elif compound == "CN":
            charge = -1
        elif compound == "SCN":
            charge = -1
        elif compound == "MnO4":
            charge = -1
        elif compound == "Cr2O7":
            charge = -2
        elif compound == "CrO4":
            charge = -2
        elif compound == "AsO4":
            charge = -3
        elif compound == "AsO3":
            charge = -3
        elif compound == "VO3":
            charge = -1
        elif compound == "VO4":
            charge = -3
        elif compound == "SeO4":
            charge = -2
        elif compound == "SeO3":
            charge = -2
        elif compound == "TeO4":
            charge = -2
        elif compound == "TeO3":
            charge = -2
        elif compound == "ClO":
            charge = -1
        elif compound == "ClO2":
            charge = -1
        elif compound == "ClO3":
            charge = -1
        elif compound == "ClO4":
            charge = -1
        elif compound == "BrO":
            charge = -1
        elif compound == "BrO2":
            charge = -1
        elif compound == "BrO3":
            charge = -1
        elif compound == "BrO4":
            charge = -1
        elif compound == "IO":
            charge = -1
        elif compound == "IO2":
            charge = -1
        elif compound == "IO3":
            charge = -1
        elif compound == "IO4":
            charge = -1
    else:
        el = element(compound)
        charge = el.en_pauling
    return charge

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
    polyions, compound = extract_polyions(compound, poly)
    reacnames.append(compound)
    reactant_elements.extend(extract_elements(compound))
    reactant_elements.extend(polyions)

print(reacnames)
print("Extracted elements and polyions:", reactant_elements)
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
