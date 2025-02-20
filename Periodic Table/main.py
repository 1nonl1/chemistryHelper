import eledata

def main():
    print("Welcome to the element reference and calculator!")
    print("Please note that this program is still in development.\nAnd only works with elements.")
    c1 = input("Reference, conversions or equation? (r/c/e): ")
    if c1 == "r":
        ask = input("What element do you want to choose? ")
        element = eledata.get_element(ask)
        if element:
            print(element)
        else:
            print("Element not found.")
    elif c1 == "c":
        from equations import conversions
        conversions()
    elif c1 == "e":
        print("This feature is not yet available.")
        print("If you have any sugestions please say so in the discussions tab.")
    else:
        print("Invalid input.")     

if __name__ == "__main__":
    main()