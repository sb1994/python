# String formating with variables
print("The Age of {0} is {1}".format('Sean',27))

#F- strings are a shorter way to embed variables inside a string 
value = 4*20
print(f"The value is {value}")

#can call functions when using F-string
import datetime

print(f"The current time is {datetime.datetime.now().isoformat()}")