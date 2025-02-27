import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry
from mendeleev import element
from mendeleev.ion import Ion

def extract_elements(compound):
    return re.findall(r'[A-Z][a-z]*', compound)

product = []
product_compound = input("Please enter the product symbol or compound: ")
product.append(product_compound)
reacnames = extract_elements(product_compound)

for i, n in enumerate(reacnames):
    if n == 'H':
        reacnames[i] = 'H2'
    elif n == 'O':
        reacnames[i] = 'O2'
    elif n == 'N':
        reacnames[i] = 'N2'
    elif n == 'F':
        reacnames[i] = 'F2'
    elif n == 'Cl':
        reacnames[i] = 'Cl2'
    elif n == 'Br':
        reacnames[i] = 'Br2'
    elif n == 'I':
        reacnames[i] = 'I2'
print("Extracted elements from product:", reacnames)

reac, prod = balance_stoichiometry(set(reacnames), set(product))
reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
products_str = "".join(f"{v}{k}" for k, v in prod.items())
print(f"Balanced Equation: {reactants_str} -> {products_str}")