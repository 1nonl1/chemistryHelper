from mendeleev import element
from mendeleev.ion import Ion


while True:
    atomic_number = int(input("Please enter the atomic number: "))

    if 0 < atomic_number < 119:
        break
    else:
        print("Please enter a valid atomic number!")

e = element(atomic_number)

charges = [_.charge for _ in e.ionic_radii]

print(f'''
Information about the element that has atomic number {atomic_number} is below:
\tName:         {e.name}
\tSymbol:       {e.symbol}
\tIonic Charge: {Ion(atomic_number)} {charges}
''')
print(charges[0])