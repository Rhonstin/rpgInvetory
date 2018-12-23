inv = {"gold coin" : 42, "rope" : 1, "torch" : 6, "dagger": 1, "arrow" : 12}
def displayInventory(inv):
    print("Inventory:")
    items = 0
    for k , v in inv.items():
        print(str(v) + " " + k)
        items += v
    print("Tota; numver of items: " + str(items))
displayInventory(inv)