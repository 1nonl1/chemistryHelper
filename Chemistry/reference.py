from chempy import Substance
import pubchempy as pcp

ask = input("What element or compound do you want to choose (Should look like this [Al2O3])? ")
element = Substance.from_formula(ask)
c = pcp.get_compounds(ask, 'formula')

if element:
    print("Molecular Weight:", element.mass) 
    print("Composition:", element.composition) 
    print("Unicode Name:", element.unicode_name) 
    print("Charge: ", element.charge)
    if c:
        compound = c[0]
        smiles = compound.isomeric_smiles
        compound_from_smiles = pcp.get_compounds(smiles, 'smiles')
        if compound_from_smiles:
            compound_number = compound_from_smiles[0].cid
            compound_name = pcp.Compound.from_cid(compound_number).iupac_name
            synonyms = pcp.Compound.from_cid(compound_number).synonyms
            common_name = synonyms[0] if synonyms else "No common name found"
            print(f"SMILES formula: {smiles}\nCompound Number: {compound_number}\nName: {compound_name}\nCommon Name: {common_name}")
        else:
            print(f"SMILES: {smiles}, Compound not found.")
    else:
        print("Compound not found.")
else:
    print("Element not found.")