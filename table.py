# Python Packages
print("| Pokemon Name | Type |")
print("_______________________")

from prettytable import  PrettyTable

table = PrettyTable()

# Showing table by reading doc.
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

# Changing table style
table.align = "l"
print(table.align)
print(table)

