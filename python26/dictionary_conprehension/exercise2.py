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
# s240-1-1-1 遍历weather_c的每一项，将weather_c改为weather_f
weather_f = {d:(t*5/9)+32 for (d,t) in weather_c.items()}
# Write your code 👇 below:



print(weather_f)