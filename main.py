import plotly.express as px
import pandas as pd

df = pd.read_csv("savings_data.csv")
fig = px.scatter(df, y = "quant_saved", color = "wealthy")
fig.show()

import csv

with open('savings_data.csv', newline = "") as f:
    reader = csv.reader(f)
    saving_data = list(reader)

saving_data.pop(0)  

total_entries = len(saving_data)
total_people_given_remainder = 0
for data in saving_data:
    if int(data[3]) == 1:
        total_people_given_remainder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x = ["remainded", "Not remainded"], y = [total_people_given_remainder, (total_entries - total_people_given_remainder)]))
fig.show()

#Mean , Median , Mode of savings
remainded_savings = []
not_remainded_savings = []
for data in saving_data:
    if int(data[3]) == 1:
        remainded_savings.append(float(data[0]))
    else:
        not_remainded_savings.append(float(data[0]))

import statistics
all_saving = []
for data in saving_data:
    all_saving.append(float(data[0]))
    
print(f"Mean of savings - {statistics.mean(all_saving)}") 
print(f"Median of savings - {statistics.median(all_saving)}") 
print(f"Mode of savings - {statistics.mode(all_saving)}") 

remainded_savings_mean = statistics.mean(remainded_savings)  
remainded_savings_median = statistics.median(remainded_savings) 
remainded_savings_mode = statistics.mode(remainded_savings)

print("Results for people who were remainded")
print("Mean of remainded savings : ", remainded_savings_mean)
print("Median of remainded savings : ", remainded_savings_median)
print("Mode of remainded savings : ", remainded_savings_mode)

not_remainded_savings_mean = statistics.mean(not_remainded_savings)
not_remainded_savings_median = statistics.median(not_remainded_savings)
not_remainded_savings_mode = statistics.mode(not_remainded_savings)

print("Results for people who were not remainded")
print("Mean of not remainded savings : ", not_remainded_savings_mean)
print("Median of not reamded savings : ", not_remainded_savings_median)
print("Mode of not remainded savings : ", not_remainded_savings_mode)

#standard deviation of savings
all_savings_std_deviation = statistics.stdev(all_saving)
remainded_savings_std_deviation = statistics.stdev(remainded_savings)
not_remainded_savings_std_deviation = statistics.stdev(not_remainded_savings)

print("standard deviation of total savings : ", all_savings_std_deviation)
print("standard deviation of remainded savings : ", remainded_savings_std_deviation)
print("standard deviation of not remainded savings : ", not_remainded_savings_std_deviation)