weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def degree_f(degree_c):
    return (degree_c * 9 / 5) + 32


weather_f = {day: degree_f(degree_c) for (day, degree_c) in weather_c.items()}
print(weather_f)


