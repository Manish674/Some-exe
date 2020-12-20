# Modules used
#   csv
#   datetime

import csv
import datetime

loop = True
now = datetime.datetime.now()
print("Health Management System\n")
print("Press 1 to enter your excercise")
print("Press 2 to see your excercises")
print("Press 3 to enter what you ate")
print("Press 4 to see your diet.")
print("Press 0 to exit.\n")

while (loop): 
  try:
    choice = int(input("Enter: "))
    if choice == 1:
      with open('excercise.csv','a') as csv_file:
          fieldsname = ['month', 'day', 'date', 'time', 'excercise'] 
          writer = csv.DictWriter(csv_file, fieldnames=fieldsname)
          month = now.strftime("%b")
          day = now.strftime("%A") 
          date = now.strftime("%d")
          time = now.strftime("%X")
          excercise = str(input("Enter your excercise: "))
          print("")
          writer.writerow({'month': month, 'day': day, 'date':date, 'time': time, 'excercise':excercise})


    elif choice == 2:
      with open('excercise.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        for row in csv_reader:
          if count == 0:
            count += 1
            pass        
          print(f'\t {row["month"]}  {row["day"]}  {row["date"]}  {row["time"]} {row["excercise"]}')
        print("")
        
    if choice == 3:
      with open('diet.csv','a') as csv_file:
          fieldsname = ['month', 'day', 'date', 'time', 'food'] 
          writer = csv.DictWriter(csv_file, fieldnames=fieldsname)
          month = now.strftime("%b")
          day = now.strftime("%A") 
          date = now.strftime("%d")
          time = now.strftime("%X")
          food = input("Enter what you ate: ")
          print("")
          writer.writerow({'month': month, 'day': day, 'date':date, 'time': time, 'food':food})

    elif choice == 4:
      with open('diet.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        for row in csv_reader:
          if count == 0:
            count += 1
            pass        
          print(f'\t {row["month"]}  {row["day"]}  {row["date"]}  {row["time"]} {row["food"]}')
        print("")
       
    elif choice == 0: 
      loop = False 

  except:
    print("Sorry something went wrong") 