import eledata

def conversions():
    choice = input("Are you trying to solve for 1 substance or 2? (1/2): ")
    if choice == "1":
        print("g = grams, reppart = representative particles, mol = moles")
        ask = input("Input what you want to convert it to: (mol-g, g-mol, reppart-mol, mol-reppart, reppart-g, g-reppart): ")
        if ask == "mol-g":
            eask = input("What element do you want to choose? ")
            element = eledata.get_element(eask)
            if element:
                atomic_mass = element.atomic_mass
                moles = float(input("Enter the number of moles: "))
                grams = moles * atomic_mass
                print(f"{moles} moles of {eask} is equal to {grams} grams.")
            else:
                print("Element not found.")
        elif ask == "g-mol":
            eask = input("What element do you want to choose? ")
            element = eledata.get_element(eask)
            if element:
                atomic_mass = element.atomic_mass
                grams = float(input("Enter the number of grams: "))
                moles = grams / atomic_mass
                print(f"{grams} grams of {eask} is equal to {moles} moles.")
            else:
                print("Element not found.")
        elif ask == "reppart-mol":
            eask = input("What element do you want to choose? ")
            element = eledata.get_element(eask)
            if element:
                avogadro_number = 6.022e23
                reppart = float(input("Enter the number of representative particles: "))
                moles = reppart / avogadro_number
                print(f"{reppart} representative particles of {eask} is equal to {moles} moles.")
            else:
                print("Element not found.")
        elif ask == "mol-reppart":
            eask = input("What element do you want to choose? ")
            element = eledata.get_element(eask)
            if element:
                avogadro_number = 6.022e23
                moles = float(input("Enter the number of moles: "))
                reppart = moles * avogadro_number
                print(f"{moles} moles of {eask} is equal to {reppart} representative particles.")
            else:
                print("Element not found.")
        elif ask == "reppart-g":
            eask = input("What element do you want to choose? ")
            element = eledata.get_element(eask)
            if element:
                avogadro_number = 6.022e23
                atomic_mass = element.atomic_mass
                reppart = float(input("Enter the number of representative particles: "))
                moles = reppart / avogadro_number
                grams = moles * atomic_mass
                print(f"{reppart} representative particles of {eask} is equal to {grams} grams.")
            else:
                print("Element not found.")
        elif ask == "g-reppart":
            eask = input("What element do you want to choose? ")
            element = eledata.get_element(eask)
            if element:
                avogadro_number = 6.022e23
                atomic_mass = element.atomic_mass
                grams = float(input("Enter the number of grams: "))
                moles = grams / atomic_mass
                reppart = moles * avogadro_number
                print(f"{grams} grams of {eask} is equal to {reppart} representative particles.")
            else:
                print("Element not found.")
        else:
            print("Invalid conversion type.")

    elif choice == "2":
        print("g = grams, reppart = representative particles, mol = moles")
        ask = input("Input what you want to convert it to: (Amol-Bg, Ag-Bmol, Ag-Bg, Amol-Bmol): ")
        if ask == "Amol-Bg":
            eask1 = input("Choose element A: ")
            element1 = eledata.get_element(eask1)
            eask2 = input("Choose element B: ")
            element2 = eledata.get_element(eask2)
            if element1 and element2:
                atomic_mass = element2.atomic_mass
                moles = float(input("Enter the number of moles for substance A: "))
                coef = float(input("Enter the coefficients of the balanced chemical equation (molB/molA): "))
                grams = moles * coef *  atomic_mass
                print(f"{moles} moles of {eask1} can react with {grams} grams of {eask2} with no excess reagents.")
            else:
                print("Element not found.")
        elif ask == "Ag-Bmol":
            eask1 = input("Choose element A: ")
            element1 = eledata.get_element(eask1)
            eask2 = input("What element do you want to choose? ")
            element2 = eledata.get_element(eask2)
            if element1 and element2:
                atomic_mass = element2.atomic_mass
                grams = float(input("Enter the grams for substance A: "))
                coef = float(input("Enter the coefficients of the balanced chemical equation (molB/molA): "))
                moles = grams / atomic_mass * coef
                print(f"{grams} grams of {eask1} can react with {moles} moles of {eask2} with no excess reagents.")
            else:
                print("Element not found.")
        elif ask == "Ag-Bg":
            eask1 = input("Choose element A:  ")
            element1 = eledata.get_element(eask1)
            eask2 = input("Choose element B: ")
            element2 = eledata.get_element(eask2)
            if element1 and element2:
                atomic_mass1 = element1.atomic_mass
                atomic_mass2 = element2.atomic_mass
                gramsA = float(input("Enter the grams for substance A: "))
                coef = float(input("Enter the coefficients of the balanced chemical equation (molB/molA): "))
                gramsB = gramsA / atomic_mass1 * coef * atomic_mass2
                print(f"{gramsA} grams of {eask1} can react with {gramsB} grams of {eask2} with no excess reagents.")
        elif ask == "Amol-Bmol":
            eask1 = input("Choose element A:  ")
            element1 = eledata.get_element(eask1)
            eask2 = input("Choose element B: ")
            element2 = eledata.get_element(eask2)
            if element1 and element2:
                atomic_mass1 = element1.atomic_mass
                atomic_mass2 = element2.atomic_mass
                molesA = float(input("Enter the mol for substance A: "))
                coef = float(input("Enter the coefficients of the balanced chemical equation (molB/molA): "))
                molesB = molesA * coef
                print(f"{gramsA} moles of {eask1} can react with {molesB} moles of {eask2} with no excess reagents.")
        else:
            print("Invalid conversion type.")
    else:
        print("Invalid choice.")