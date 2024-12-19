def identify_mushroom():
    # Dictionary to store mushroom properties
    mushrooms = {
        "Agaric Jaunissant": {"gills": True, "forest": False, "ring": True, "convex_cup": True},
        "Cepe de Bordeaux": {"gills": False, "forest": True, "ring": False, "convex_cup": False},
        "Amanite Tue-Mouche": {"gills": True, "forest": True, "ring": True, "convex_cup": True},
        "Coprin Chevelu": {"gills": True, "forest": False, "ring": True, "convex_cup": False},
        "Girolle": {"gills": True, "forest": True, "ring": False, "convex_cup": False},
        "Pied Bleu": {"gills": True, "forest": True, "ring": False, "convex_cup": True}
    }

    # Ask the user the questions
    print("Answer the following questions with 'yes' or 'no'.\n")

    # Question 1: Does your mushroom have gills?
    gills = input("Does your mushroom have gills? ").strip().lower() == "yes"

    # Question 2: Does your mushroom grow in a forest?
    forest = input("Does your mushroom grow in a forest? ").strip().lower() == "yes"

    # Question 3: Does your mushroom have a ring?
    ring = input("Does your mushroom have a ring? ").strip().lower() == "yes"

    # Question 4: Does your mushroom have a convex cup?
    convex_cup = input("Does your mushroom have a convex cup? ").strip().lower() == "yes"

    # Filter the possible mushrooms based on answers
    possible_mushrooms = []

    for mushroom, properties in mushrooms.items():
        if properties["gills"] == gills and properties["forest"] == forest and \
           properties["ring"] == ring and properties["convex_cup"] == convex_cup:
            possible_mushrooms.append(mushroom)

    # Determine the mushroom
    if len(possible_mushrooms) == 1:
        print(f"The mushroom is: {possible_mushrooms[0]}")
    else:
        print("Sorry, I could not determine the mushroom with the given answers.")

# Call the function to run the program
identify_mushroom()
