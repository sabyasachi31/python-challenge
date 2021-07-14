#Dependencies
import os
import csv
import sys
from statistics import mean

#Filepath
csv_path=os.path.join('Resources','budget_data.csv')

#Declaring variables
total_months=0
net_profit=0
flag=0
p_l=0
change=0
total=0
max_change=0
min_change=0

#Decalring Empty List
pl_change=[]

with open (csv_path,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skipping header row
    csvheader=next(csvreader)

    for row in csvreader:
        #Calculating total months
        total_months+=1
        #Calculating total amount
        p_l=int(row[1])
        total=total+p_l
        
        #Calculating change and storing in list
        if flag==0:
            flag=1
        else:
            change=p_l-change
            pl_change.append(change)
        
        #Calculating maximum increase and decrease in profits
        if(change>max_change):
            max_change=change
            max_month=row[0]
        if(change<min_change):
            min_change=change
            min_month=row[0]
        
        change=p_l

#Finding average change
avg_change=round(mean(pl_change),2)

#Print to Terminal

print("Financial Analysis")
print("---------------------------")
   
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")

print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

#Export to File
file=open("analysis/bank.txt",'w')
sys.stdout=file

print("Financial Analysis")
print("--------------------------")
   
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")

print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

file.close()