# Write a python program that accepts seconds as input of type integer. The
# program should convert seconds in hours, minutes and seconds. Output
# should like this :
# Enter seconds: 12200
# Hours: 3
# Minutes: 23
# Seconds: 20

inp = int(input("Enter seconds: "))

hrs = inp // (60 ** 2)
mins = (inp % (60 ** 2)) // 60
secs = (inp % (60 ** 2)) % 60

print(f"Hours: {hrs}")
print(f"Minutes: {mins}")
print(f"Seconds: {secs}")
