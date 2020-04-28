## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]
avg_rating = avg_rating/5



## 8. Repetitive Processes ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

"""
ln = len(app_data_set)
sum = 0
for i in range(ln):
    sum += app_data_set[i][4]
avg = sum/ln
print(avg)
"""

for lis in app_data_set:
    print(lis)


