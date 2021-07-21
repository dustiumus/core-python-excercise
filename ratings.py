"""Restaurant rating lister."""

# put your code here
ratings = {}

with open('scores.txt') as s:
    ratings = s.readlines()
    ratings.sort()

print(ratings)

# I looked over the solutions to help understand what was wanted and make sure I understood the concepts and the code
def read_ratings():
    ratings = {}
    scores_txt = open('scores.txt')

    for line in scores_txt: 
        line = line.rstrip()
        place, rating = line.split(":")
        ratings[place] = int(rating)

    return ratings

print(read_ratings())

def sorted_ratings(ratings):
    for place, rating in sorted(ratings.items()):
        print(f"{place} is rated at {rating}. Deal with it.")
#  Learned that "f" is a formatting tool. 

def add_restaurant(ratings):
    ratings = {}
    
    print("Enter Your Favorite Place and Your Rating, Oh Yeah!!")
    restaurant = input("Restaurant Name:"),
    rating = int(input("Restaurant Rating:"))

    ratings[restaurant] = rating
    print(ratings)

add_restaurant(ratings)