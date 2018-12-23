inv = {"gold coin" : 42, "rope" : 1, "torch" : 6, "dagger": 1, "arrow" : 12}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
def displayInventory(inv):
    print("Inventory:")
    items = 0
    for k , v in inv.items():
        print(str(v) + " " + k)
        items += v
    print("Tota; numver of items: " + str(items))
def addToInventroty(inv, addedItems):
    for item in dragonLoot:
        inv.setdefault(item,0)
        inv[item] = inv[item]+1
addToInventroty(inv,dragonLoot)
displayInventory(inv)