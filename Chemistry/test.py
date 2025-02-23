import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry


def compound(num_compounds, role):
    compounds = []
    for i in range(num_compounds):
        compound = input(f"Enter the {role} {i + 1}: ")
        compounds.append(Substance.from_formula(compound))
        
    return compounds

def balance():
    ask = input("decomposition, synthesis, or double displacement, single displacement? (d/s/dd/sd): ")
    if ask == "s":
        reacnum = int(input("How many reactants are there? "))
        reactants = compound(reacnum, "reactant")
        reactant_names = [reactant.name for reactant in reactants]
        print("Reactants: ", reactant_names)
        prods = [reactant.name for reactant in reactants]
        product = sorted(prods)
        produc = ''.join(product)
        print("Products: ", produc)

    try:
        reac, prod = balance_stoichiometry(set(reactant_names), set(produc))
        reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
        products_str = "".join(f"{v}{k}" for k, v in prod.items())
        print(f"Balanced Equation: {reactants_str} -> {products_str}")

    except ValueError as e:
        print(f"Error balancing equation: {e}") 
balance()