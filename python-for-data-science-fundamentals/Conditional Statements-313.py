## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

su = 0.0
cn = 0

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    #print(rating)
    # Complete the code from here
    price = float(row[4])
    if price == 0.0:
        su = su + rating
        cn = cn + 1
       
avg_rating_free = su/cn
print(avg_rating_free)




    
    
    

## 2. Booleans ##

a_price = 0

if a_price == 0:
    print('This is free')
if a_price == 1:
    print('This is not free')

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price == 0.0:
        free_apps_ratings.append(rating)
    if price != 0.0:
        non_free_apps_ratings .append(rating)
        
    
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)
avg_rating_non_free = sum(non_free_apps_ratings)/len(non_free_apps_ratings)

print(avg_rating_non_free)

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
non_games_ratings = []
ln = len(apps_data)

for i in range(1,ln):
    cn = cn + 1
    if apps_data[i][-5]!= 'Games':
        rating = float(apps_data[i][7])
        non_games_ratings.append(rating)
avg_rating_non_games = sum(non_games_ratings)/(len(non_games_ratings))
print(avg_rating_non_games)


        
        


## 5. Multiple Conditions ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if (price == 0.0 and genre == 'Games'):
        free_games_ratings.append(rating)
avg_rating_free_games = sum(free_games_ratings)/len(free_games_ratings)
print(avg_rating_free_games)


## 6. The or Operator ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

cn = 0
games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    
    if genre == "Social Networking" or genre == "Games":
        games_social_ratings.append(rating)


avg_games_social = sum(games_social_ratings)/len(games_social_ratings)

print(avg_games_social)


## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
        
avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Non-free apps (average)

nonfree_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        nonfree_games_social_ratings.append(rating)
        
avg_non_free = sum(nonfree_games_social_ratings)/len(nonfree_games_social_ratings)

print(avg_non_free)
    


## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
greater_nine = []

for row in apps_data[1:]:
    price = float(row[4])
    rating = float(row[7])
    if price > 9.0:
        greater_nine.append(rating)
        
avg_rating = sum(greater_nine)/len(greater_nine)
n_apps_more_9 = len(greater_nine)
n_apps_less_9 = (len(apps_data)-1)-n_apps_more_9
print(avg_rating)
print(n_apps_more_9)
print(n_apps_less_9)
        
        

