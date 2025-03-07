from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt
import pubchempy as pcp
import time
plt.switch_backend('Agg')

def get_smiles_from_input(input_str):
    try:
        compound = pcp.get_compounds(input_str, 'name')
        if not compound:
            compound = pcp.get_compounds(input_str, 'formula')
        if compound:
            return compound[0].canonical_smiles
        else:
            raise ValueError("Compound not found")
    except Exception as e:
        print(f"Error: {e}")
        return None

input_str = input("Compound name or formula: ")
input_smiles = get_smiles_from_input(input_str)
print(f"SMILES string: {input_smiles}")
time.sleep(1)
mol = Chem.MolFromSmiles(input_smiles)
dos = Draw.MolDrawOptions()
dos.addAtomIndices=True
plt.imshow(Draw.MolToImage(mol, options= dos))
plt.axis('off')
plt.savefig('molecule.png')
print("Molecule image saved as molecule.png")