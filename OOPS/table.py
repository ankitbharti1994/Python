from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City Name", ["Adelaide", "Mumbai", "London", "New York"])
table.add_column("Country", ["Australia", "India", "United Kingdom", "United States"])
table.align["City Name"] = 'c'
table.align["Country"] = 'l'
print(table.align)
print(table)

