import os 
import csv
net_profitloss = 0
total_month = 0
change_list =[]
rows=[]
months=[]
sum_of_change = 0
#find the csvfile
csvpath = os.path.join("Resources","budget_data.csv")
#Read from the csvfile 
with open (csvpath) as csvfile:
   csvreader = csv.reader(csvfile,delimiter=",")

    #skip header
   next(csvreader, None) 
#for total month 
   for row in csvreader:
    total_month = total_month + 1
    net_profitloss = net_profitloss + int(row[1])
    #append value of rows[1]from csvfile to rows[]
    rows.append(int(row[1]))
    #append vlaues of row[0] from csvsfile to months
    months.append(row[0])

#find the change in profit/loss over the entire period
   for i in range(0,(len(rows)-1)):
    change = rows[i+1] - rows[i]
    #append the values in the list change_list
    change_list.append(change)
    #find the average change of profit/loss over the entitre period
   for i in change_list:
       sum_of_change+= i
       average = sum_of_change/(len(change_list))
# find the greatest increase and greatest decrease in change in profit/loss 
for i in change_list:
    max_change =max(change_list)
    min_change =min(change_list)

#find the index  with greatest change in profit/loss
for i in change_list:
    max_change_index =change_list.index(max_change)
    min_change_index =change_list.index(min_change) 

#find the month with greatest increase and decrease in change in profit/loss
print("Financial Analysis")
print("----------------------")
print("Total Months:", total_month)
print("Total:", net_profitloss)
print("Average Change:","$",('%.3f') % average)
print ("Greatest increase in profit: " ,months[int(max_change_index+1)],'(%s)'% ("$ "+str(max_change)))
print ("Greatest decrease in profit: " ,months[int(min_change_index+1)], '(%s)'% ("$ "+  str(min_change)))


file = os.path.join("Analysis","Financial_Analysis.txt")
with open (file,"w") as outfile:
 outfile.write("Financial Analysis"+"\n")
 outfile.write("----------------------"+"\n")
 outfile.write("Total Months:"+ str(total_month) +"\n")
 outfile.write("Total:" +"$"+ str(net_profitloss)+"\n")
 outfile.write("Average Change:")
 outfile.write("$"+str(('%.3f') % average) +"\n")
 outfile.write("Greatest increase in profit: "+str(months[int(max_change_index+1)])+'(%s)'% ("$ "+  str(max_change))+"\n")
 outfile.write("Greatest decrease in profit: "+ str(months[int(min_change_index+1)])+ '(%s)'% ("$ "+  str(min_change))+"\n")
