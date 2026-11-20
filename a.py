pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
burrito = ("Veg Burrito", "Mexican", 45, "Hard")
all_recipes = (pasta, burrito)
print("Recips 1:", pasta)

print("Name:", pasta[0], "| Level:", pasta[-1])
print("Burrito time:", all_recipes[1][2])
print("Cuisine and minutes:", pasta[1:3])

print("Pasta card:")
for detail in pasta:
    print(" -", detail)

pasta_list = ["tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"]
burrito_items = {"rice", "oregano", "garlic", "onion", "tomato", "spices"}
pasta_items = set(pasta_list)
print("pasta items:", len(pasta_items), sorted(pasta_items))

extra = input("Add one ingredient to the pasta: ")
pasta_items.add(extra)
pasta_items.discard("chilli")
pasta_items.discard("basil")
print("updated pasta items:", sorted(pasta_items))

every_item = pasta_items.union(burrito_items)
shared = pasta_items.intersection(burrito_items)
only_pasta = pasta_items.difference(burrito_items)
not_shared = pasta_items.symmetric_difference(burrito_items)
print("Every item:", sorted(every_item))
print("shared:", sorted(shared))
print("only pasta:", sorted(only_pasta))
print("not shared:", sorted(not_shared))