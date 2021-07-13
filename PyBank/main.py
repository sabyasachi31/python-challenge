import os
import csv
from statistics import mean

csv_path=os.path.join('Resources','budget_data.csv')
total_months=0
net_profit=0
ind=0
p_l=0
change=0
total=0
pl_change=[]
max_change=0
min_change=0

with open (csv_path,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)

    for row in csvreader:
        
        total_months+=1
        p_l=int(row[1])
        total=total+p_l
            
        if ind==0:
            ind=1
        else:
            change=p_l-change
            pl_change.append(change)
            
        if(change>max_change):
            max_change=change
            max_month=row[0]
        if(change<min_change):
            min_change=change
            min_month=row[0]
        
        change=p_l

avg_change=round(mean(pl_change),2)


print("Financial Analysis")
print("--------------------------")
   
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")

print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")
