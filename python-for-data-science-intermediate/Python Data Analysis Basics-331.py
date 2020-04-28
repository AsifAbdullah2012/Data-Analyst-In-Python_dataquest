## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for lop in moma:
    date = lop[6]
    if date!="":
        date = int(date)
    lop[6] = date
    


## 2. Calculating Artist Ages ##

ages = []
for lop in moma:
    date = lop[6]
    birth = lop[3]
    x_int = type(birth)
    if x_int is int:
        age = date - birth
    else:
        age = 0
    ages.append(age)
final_ages = []

for lop in ages:
    if lop>20:
        final_age = lop
        final_ages.append(final_age)
    else:
        final_age = "Unknown"
        final_ages.append(final_age)
    

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen
decades = []
for lop in final_ages:
    if lop == "Unknown":
        decade = "Unknown"
    else:
        decade = str(lop)
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for lop in decades:
    if lop not in decade_frequency:
        decade_frequency[lop] = 1
    else:
        decade_frequency[lop] = decade_frequency[lop] + 1

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for lop in moma:
    artist = lop[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] = artist_freq[artist] + 1

## 7. Creating an Artist Summary Function ##

def artist_summary(strn):
    num = artist_freq[strn]
    print("There are {} artworks by {} in the data set".format(num,strn))
    
artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for lop in pop_millions:
    name = lop[0]
    popu = lop[1]
    strn = "The population of {} is {:,.2f} million"
    print(strn.format(name,popu))
    


## 9. Challenge: Summarizing Artwork Gender Data ##

from csv import reader
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)

gender_freq = {}

for lop in moma:
    if lop[5] not in gender_freq:
        gender_freq[lop[5]] = 1
    else:
        gender_freq[lop[5]] = gender_freq[lop[5]] + 1
strn = "There are {:,} artworks by {} artists"

gender = gender_freq.keys()
fre = gender_freq.items()

for lop in gender:
    print(strn.format(gender_freq[lop],lop))
    
    
    