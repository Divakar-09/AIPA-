import csv

# with open("AI_MicroDegree.csv",mode="w",newline='') as csvfile:
#     add_csv=csv.writer(csvfile)
#     add_csv.writerow(['Name','Address','Trade'])
#     add_csv.writerow(['Divakar','Hyderabad','AI'])
#     add_csv.writerow(['varun','charminar','bichaldev_trade'])
#     add_csv.writerow(['venkatesh','golconda','errhuk_trade'])
# print("CSV creaded successfully.")

with open("AI_MicroDegree.csv",newline='') as csvfile:
    csv1=csv.reader(csvfile)
    for row in csv1:
        print(row)

