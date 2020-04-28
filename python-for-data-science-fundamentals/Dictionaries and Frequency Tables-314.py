## 1. Storing Data ##

from csv import reader
fil = open('AppleStore.csv')
red = reader(fil)
app_data_store = list(red)

cn4 = cn9 = cn12 = cn17 = 0

for app in app_data_store[1:]:
    if app[10] == '4+':
        cn4 = cn4 + 1
    elif app[10] == '9+':
        cn9 = cn9 + 1
    elif app[10] == '12+':
        cn12 = cn12 + 1
    else:
        cn17 = cn17 + 1

content_ratings = ['4+', '9+', '12+', '17+']
numbers = [cn4, cn9, cn12, cn17]
content_rating_numbers = [content_ratings, numbers]
print(content_rating_numbers)






## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_9 = content_ratings['9+']
over_17 = content_ratings['17+']
print(over_9)
print(over_17)

## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

#print('9+' in content_ratings)
#print(987 in content_ratings)

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = "It exists"
print(is_in_dictionary_1)
print(is_in_dictionary_2)
print(result)




## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


content_ratings = {}

for app in apps_data[1:]:
    c_rating = str(app[10])
    if c_rating not in content_ratings: # checking if the key is present or absent
        content_ratings[c_rating] = 1
    else:
        content_ratings[c_rating] = content_ratings[c_rating] + 1
        
    
print(content_ratings)

    
    


## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}

for app in apps_data[1:]:
    genre = str(app[11])
    if genre not in genre_counting: # checking if the key is present or absent
        genre_counting [genre] = 1
    else:
        genre_counting [genre] = genre_counting[genre] + 1
        
    
maxi = 0
res = ''
lis = genre_counting.keys()

for app in lis:
    if genre_counting[app] > maxi:
        maxi = genre_counting[app]
        res = app

print(res)