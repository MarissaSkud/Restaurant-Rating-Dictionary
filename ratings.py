"""Restaurant rating lister."""
def get_restaurant_rating(file_path):

    file = open(file_path)


    ratings_dictionary = {}

    for line in file:
        line = line.rstrip()
        data = line.split(":")

        restaurant = data[0]
        rating = data[1]

        ratings_dictionary[restaurant] = rating

    while True:
        user_selection = input("What do you want to do? S: See the rating; A: Add a rating; Q: Quit: ")

        if user_selection == 'S':
                sorted_restaurant = sorted(ratings_dictionary)

                for restaurant in sorted_restaurant:
                    print(f"{restaurant} is rated at {ratings_dictionary[restaurant]}.")


        if user_selection == "A":
            possible_ratings = ["1", "2", "3", "4", "5"]

            new_restaurant = input("Add another restaurant ")

            new_rating = "0"

            while new_rating not in possible_ratings:
                new_rating = input("How do you rate that restaurant on a scale of 1 to 5? ")

            ratings_dictionary[new_restaurant] = new_rating


        if user_selection == "Q":
            return

get_restaurant_rating("scores.txt")
