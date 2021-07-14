#Dependencies
import os
import csv
import sys

#Filepath
csv_path=os.path.join('Resources','election_data.csv')

#Declaring empty dictionary
candidates={}

with open(csv_path,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skipping over the header row
    csvheader=next(csvreader)
    
    for row in csvreader:
        #Assigning the names of candidates as unique dictionary keys 
        #and the number of votes as their values     

        if row[2] in candidates:
            candidates[row[2]]+=1
        else:
            candidates[row[2]]=1

#Finding total votes cast
total=sum(candidates.values())
#Finding maximum votes cast for the winning candidate
max_votes=max(candidates.values())

# Output to Terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total}")

print("--------------------------")

for name, votes in candidates.items():
    #Finding the winner with maximum votes
    if votes==max_votes:
        winner=name
    print(f"{name}: {round(100*votes/total,3)}% ({votes})")

print("--------------------------")
print(f"Winner: {winner} ")

print("--------------------------")

#Export to File
file=open("analysis/poll.txt",'w')
sys.stdout=file

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total}")

print("--------------------------")

for name, votes in candidates.items():
            
    if votes==max_votes:
        winner=name
    print(f"{name}: {round(100*votes/total,3)}% ({votes})")

print("--------------------------")
print(f"Winner: {winner} ")

print("--------------------------")

file.close()

