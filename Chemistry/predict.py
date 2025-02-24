import re
from chempy import Substance
from chempy.chemistry import balance_stoichiometry
from mendeleev import element


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
        
        # Split items on every number and uppercase letter
        prodstuff = [re.split(r'(?=[A-Z0-9])', name) for name in prods]
        # Flatten the list of lists into a single list and remove numbers and empty strings
        produc = [item for sublist in prodstuff for item in sublist if item and not item.isdigit()]
        produc = ''.join(produc)
        print("Formatted Products: ", produc)
        
        # Create elements and print oxidation states
        for item in produc:
            elem = element(item)
            print(f"Oxidation states for {item}: {elem.oxidation_states()}")

    try:
        reac, prod = balance_stoichiometry(set(reactant_names), set(produc))
        reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
        products_str = "".join(f"{v}{k}" for k, v in prod.items())
        
        # Remove 'x' characters from the products_str
        products_str = products_str.replace('x', '')
        
        print(f"Balanced Equation: {reactants_str} -> {products_str}")

    except ValueError as e:
        print(f"Error balancing equation: {e}") 
balance()