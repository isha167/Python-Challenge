import os
import csv
import operator
from collections import Counter
total_vote =0
candidate_list =[]
votes_percandidate =[]


csvpath = os.path.join("Resources","election_data.csv")
with open (csvpath) as csvfile:
 csvreader = csv.reader(csvfile,delimiter=",")

#skip header
 next(csvreader, None) 
 #calculate total votes cast
 for row in (csvreader):
      total_vote= total_vote + 1
      candidate_list.append(row[2])
#print the results
print("Election Results")
print("-----------------------------") 
print ("Total Votes : "+ str(total_vote))
print("-----------------------------")
# print number of votes for each candidates
counts=Counter(candidate_list)
for i in counts:
 print(i,":",'%.3f' % int(int(counts[i])*100/total_vote),"%",'(%s)' % counts[i])

#find and print the winner name 
 winner_key = max(counts.items(), key=operator.itemgetter(1))[0]
print("-----------------------------") 
print(" Winner:" + str(winner_key))
print("-----------------------------") 

#write in a text file 
textfile = os.path.join("Analysis","Election_results.txt")
with open (textfile,"w") as outfile:
 outfile.write("Election Results"+ "\n")
 outfile.write("-----------------------------"+"\n") 
 outfile.write("Total Votes : "+ str(total_vote)+"\n")
 outfile.write("-----------------------------"+"\n")
 counts=Counter(candidate_list)
 for i in counts:
  outfile.write(i)
  outfile.write(":")
  outfile.write('%.3f' % int(int(counts[i])*100/total_vote) )
  outfile.write("%" )
  outfile.write( '(%s)' % counts[i]+"\n")
 outfile.write("-----------------------------"+"\n") 
 outfile.write(" Winner:" + str(winner_key)+"\n")
 outfile.write("-----------------------------"+"\n") 
