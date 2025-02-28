from mendeleev import element

def get_oxidation_states(compound):
    el = element(compound)
    return el.oxidation_states()

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
        oxidation_states = get_oxidation_states(compound)
        if oxidation_states:
            charge = oxidation_states[0]
        else:
            charge = 0
    return charge