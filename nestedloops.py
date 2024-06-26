# nested loops


rows = int(input("How many rows you want?: "))
columns = int(input("How many columns you want?: "))
symbol = input("Type your symbol you want to use?: ")


for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
