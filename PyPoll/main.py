import os
import csv

csv_path=os.path.join('Resources','election_data.csv')

ind=0
total=0
candidates=[]


with open(csv_path,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        if ind!=0:
            cnt=0
            for name in candidates:
                if name!=row[2]:
                    cnt=cnt+1
            if cnt==len(candidates):
                candidates.append(row[2])
        ind=ind+1
              
ind=0
votes=[0]*len(candidates)
with open(csv_path,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        if ind!=0:
            pos=candidates.index(row[2])
            votes[pos]=votes[pos]+1
        ind=ind+1

total=sum(votes)
max_votes=max(votes)
w_ind=votes.index(max_votes)
winner=candidates[w_ind]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {total}")

print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {round(100*votes[i]/total,3)}% ({votes[i]})")


print("--------------------------")
print(f"Winner: {winner} ")

print("--------------------------")