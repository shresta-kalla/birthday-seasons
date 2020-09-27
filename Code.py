name = input("Enter your name:")
month = input("What month were you born(enter as number 1-12):")
day = input("What day were you born:")
month = int(month)
day = int(day)
String season = ""

if(6 <= month <=8)
  season = "Summer Baby"
if(9 <=month <= 11)
  season = "Fall Baby"
print("Hi " , name , ", you are born on " , month, " ", day, "! You are a ", season, "!")
