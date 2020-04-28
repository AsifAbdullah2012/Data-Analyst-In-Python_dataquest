## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]
sum_manual = 0 
for i in a_list:
    sum_manual += i
    
print(sum_manual, ' is equal to ', sum(a_list))



## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for app in ratings:
    if app not in content_ratings:
        content_ratings[app] = 1
    else:
        content_ratings[app] += 1
print(content_ratings)



## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

def freq_table(genres):
    daten = {}
    for i in genres:
        if i not in daten:
            daten[i] = 1
        else:
            daten[i] += 1
    return daten

genres = extract(11)
genres_ft = freq_table(genres)
