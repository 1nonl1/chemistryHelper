from chempy import Substance

def conversions():
    choice = input("Are you trying to solve for 1 substance or 2 or more? (1/2): ")
    if choice == "1":
        print("g = grams, reppart = representative particles, mol = moles")
        ask = input("Input what you want to convert it to: (mol-g, g-mol, reppart-mol, mol-reppart, reppart-g, g-reppart): ")
        if ask == "mol-g":
            eask = input("What element or compound do you want to choose? ")
            element = Substance.from_formula(eask)
            if element:
                atomic_mass = '%.3f' % element.mass
                moles = float(input("Enter the number of moles: "))
                grams = moles * atomic_mass
                print(f"{moles} moles of {eask} is equal to {grams} grams.")
            else:
                print("Element not found.")
        elif ask == "g-mol":
            eask = input("What element do you want to choose? ")
            element = Substance.from_formula(eask)
            if element:
                atomic_mass = '%.3f' % element.mass
                grams = float(input("Enter the number of grams: "))
                moles = grams / atomic_mass
                print(f"{grams} grams of {eask} is equal to {moles} moles.")
            else:
                print("Element not found.")
        elif ask == "reppart-mol":
            eask = input("What element do you want to choose? ")
            element = Substance.from_formula(eask)
            if element:
                avogadro_number = 6.022e23
                reppart = float(input("Enter the number of representative particles: "))
                moles = reppart / avogadro_number
                print(f"{reppart} representative particles of {eask} is equal to {moles} moles.")
            else:
                print("Element not found.")
        elif ask == "mol-reppart":
            eask = input("What element do you want to choose? ")
            element = Substance.from_formula(eask)
            if element:
                avogadro_number = 6.022e23
                moles = float(input("Enter the number of moles: "))
                reppart = moles * avogadro_number
                print(f"{moles} moles of {eask} is equal to {reppart} representative particles.")
            else:
                print("Element not found.")
        elif ask == "reppart-g":
            eask = input("What element or compound do you want to choose? ")
            element = Substance.from_formula(eask)
            if element:
                avogadro_number = 6.022e23
                atomic_mass = '%.3f' % element.mass
                reppart = float(input("Enter the number of representative particles: "))
                moles = reppart / avogadro_number
                grams = moles * atomic_mass
                print(f"{reppart} representative particles of {eask} is equal to {grams} grams.")
            else:
                print("Element not found.")
        elif ask == "g-reppart":
            eask = input("What element do you want to choose? ")
            element = Substance.from_formula(eask)
            if element:
                avogadro_number = 6.022e23
                atomic_mass = '%.3f' % element.mass
                grams = float(input("Enter the number of grams: "))
                moles = grams / atomic_mass
                reppart = moles * avogadro_number
                print(f"{grams} grams of {eask} is equal to {reppart} representative particles.")
            else:
                print("Element not found.")
        else:
            print("Invalid conversion type.")

    elif choice == "2":
        num_reactants = int(input("How many reactants are there? "))
        num_products = int(input("How many products are there? "))
        
        reactants = []
        products = []
        
        for i in range(num_reactants):
            reactant = input(f"Enter reactant {i+1}: ")
            reactants.append(Substance.from_formula(reactant))
        
        for i in range(num_products):
            product = input(f"Enter product {i+1}: ")
            products.append(Substance.from_formula(product))
        
        if all(reactants) and all(products):
            reactant_masses = [float(input(f"Enter the mass (grams) of {reactant.name}: ")) for reactant in reactants]
            reactant_moles = [mass / reactant.mass for mass, reactant in zip(reactant_masses, reactants)]
            
            coefficients = [float(input(f"Enter the coefficient for {reactant.name} in the balanced equation: ")) for reactant in reactants]
            limiting_reagent_ratios = [reactant_moles[i] / coefficients[i] for i in range(num_reactants)]
            limiting_reagent_index = limiting_reagent_ratios.index(min(limiting_reagent_ratios))
            
            limiting_reagent = reactants[limiting_reagent_index]
            limiting_moles = reactant_moles[limiting_reagent_index]
            
            excess_reagents = [(reactant.name, reactant_moles[i] - limiting_moles * coefficients[i]) for i, reactant in enumerate(reactants) if i != limiting_reagent_index]
            
            print(f"The limiting reagent is {limiting_reagent.name}.")
            for reagent, excess in excess_reagents:
                excess_mass = excess * reactants[reactants.index(Substance.from_formula(reagent))].mass
                print(f"{excess} moles ({excess_mass} grams) of {reagent} is left over.")
            
            product_moles = [limiting_moles * float(input(f"Enter the coefficient for {product.name} in the balanced equation: ")) for product in products]
            product_masses = [moles * product.mass for moles, product in zip(product_moles, products)]
            
            for product, mass in zip(products, product_masses):
                print(f"{mass} grams of {product.name} will be produced.")
        else:
            print("One or more elements not found.")
    else:
        print("Invalid choice.")

conversions()