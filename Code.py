name = input("Enter your name:")
month = input("What month were you born(enter as number 1-12):")
day = input("What day were you born:")
month = int(month)
day = int(day)
String season = ""
if(12 <= month <= 2)
  season = "Winter Baby"
if(3 <= month <= 5)
  season = "Spring Baby"
if(6 <= month <=8)
  season = "Summer Baby"
if(9 <= 11)
  season = "Fall Baby"
print("Hi " , name , ", you are born on " , month, " ", day, "! You are a ", season, "!")
