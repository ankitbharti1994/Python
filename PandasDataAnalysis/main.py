import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
gray_squirrel = data[fur_color == "Gray"]
cinnamon_squirrel = data[fur_color == "Cinnamon"]
black_squirrel = data[fur_color == "Black"]

squirrel_dict = {
    "fur_color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [len(gray_squirrel), len(cinnamon_squirrel), len(black_squirrel)],
}

newDataframe = pandas.DataFrame(squirrel_dict)
newDataframe.to_csv('squirrel_count.csv')
