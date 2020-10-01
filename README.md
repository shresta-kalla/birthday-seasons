# birthday-seasons

**Description:** We will prompt the user for their name and birthday and then using that input we will find what season their birthday falls in. Then we will display their name, birthday and season. 

**Group members**
- Shresta Kalla
- Shreya Kalla

**This snippet of code is to allow the user to interact with the question given, and enter whatever is applicable to them.(You are free to enter whatever name & birthday as you wish!).**

```python
name = input("Enter your name:")
month = input("What month were you born(enter as number 1-12):")
```

**This snippet of code creates a decision structure that will allow the user's input to fall within one of these four months. For instance, if the user inputs June(i.e the number 6), then the output will return 'Summer".**
```python
if(6 <= month <=8):
  season = "Summer"
elif(9 <=month <= 11):
  season = "Fall"
elif(3 <= month <= 5):
  season = "Spring"
else:
  season = "Winter"
  ```
  
![alt-text](https://media.giphy.com/media/RlZouK6QqVVHNIxp6I/giphy.gif)
