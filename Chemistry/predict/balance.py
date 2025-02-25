from chempy import Substance
from chempy.chemistry import balance_stoichiometry

def compounds(num_compounds, role):
    compounds = []
    for i in range(num_compounds):
        compound = input(f"Enter the {role} {i + 1}: ")
        compounds.append(Substance.from_formula(compound))
    return compounds

def balance():
    reacnum = int(input("How many reactants are there? "))
    prodnum = int(input("How many products are there? "))
    reactants = compounds(reacnum, "reactant")
    products = compounds(prodnum, "product")

    reactant_names = [reactant.name for reactant in reactants]
    product_names = [product.name for product in products]
    print(reactant_names, " + ", product_names)

    try:
        reac, prod = balance_stoichiometry(set(reactant_names), set(product_names))
        reactants_str = " + ".join(f"{v}{k}" for k, v in reac.items())
        products_str = " + ".join(f"{v}{k}" for k, v in prod.items())
        print(f"Balanced Equation: {reactants_str} -> {products_str}")
        
        # Print product names below the formula
    except ValueError as e:
        print(f"Error balancing equation: {e}") 

balance()