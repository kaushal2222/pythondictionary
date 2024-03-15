currency={"india":"Rupee","USA":"Dollar","Russia":"Ruble","japan":"yen","Germany":"Euro"}

def main():
    print("List of countries")
    for key in currency.keys():
        print(key)
    print("list of currencies in differnet countries")
    for value in currency.values():
        print(value)
    for key,value in currency.items():
        print(f" '{key}' has a currency of type '{value}'")

if __name__ == "__main__":
    main()
