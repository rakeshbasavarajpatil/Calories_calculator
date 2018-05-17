#This is progran designed to give an average calorie count for an individual burnt based on the distance the person ran or jogged
#The user provides input and gets back the calories burnt on a average
print("Number of kms run/jogged today?")
kms = input()
miles = float(kms)/1.621371
miles = round(miles,2)
print("Time taken for the run in minutes")
time_for_run = input()
time_for_run = float(time_for_run)
print(f"Your {kms} run today in miles is {miles}mi in {time_for_run}min.")
print("What is your weight in kgs?")
weight = input()
weight_in_pounds = float(weight)/0.453592
weight_in_pounds=round(weight_in_pounds,2)
print("Please provide your age")
age = input()
age = float(age)
print("Heart rate in bpm")
hr = input()
hr = float(hr)
#the calories burnt formula is used from http://fitnowtraining.com
#calories_burnt = round(miles * 100,2)
calories_burnt = ((age * 0.2017) - (weight_in_pounds * 0.09036) + (hr * 0.6309) - 55.0969) * time_for_run/4.184
print(f"Average calories burnt by an individual is {calories_burnt}") 