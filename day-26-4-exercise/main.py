sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
words = sentence.split()
result = {key: len(key) for key in words}
print(result)
