import csv
import uuid 
  
quantity = 101
# quantity = 10
with open('data/data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])    
    for i in range(1, quantity):
        # writer.writerow([i, "Linus Torvalds", "Linux Kernel"])
        writer.writerow([uuid.uuid1(), "Linus Torvalds", "Linux Kernel"])
