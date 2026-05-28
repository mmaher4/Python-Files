#Mya Maher
#Hacker
import pandas as pd

data = pd.read_csv('hacker.csv')

log = data['Log_ID'].tolist()
address = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
time = data['Time'].tolist()
summary = data['Description'].tolist()
info = data['Data_KB'].tolist()
filter = []
filter1 = []
filter2 = []

def failed(word):
    for i in range(len(log)):
        if word in summary[i]:
            filter.append(log[i])
    print(filter)
    filter.clear()
failed("Failed")
print(data.loc[[196,197,198]])

def locate():
    for i in range(len(log)):
        if info[i]>1500:
            filter1.append(log[i])
    print(f"The Log_ID with the most data stolen is, {filter1}! The file is a, {summary[i]}")
    filter1.clear()
locate()

def reset(word):
    for i in range(len(log)):
        if word in summary[i]:
            filter2.append(log[i])
    print(f"The 11 users who were forced to reset their passwords have the Log_ID of, {filter2}.")
    filter2.clear()
reset("Reset")

