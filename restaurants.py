def most_varied_visitor(visits):
    # Write your solution here!
    # pass

    # create dictionary callled persons, persons:count
    # loop through the persons list in the visits
        # if it is not in the dictionary, initialize it
        # if it is in the dictionary, add 1 to the count

    # loop through the persons, find the person with max count
    
    person_counts = {}
    for persons in visits.values():
        for person in set(persons):
            if person in person_counts:
                person_counts[person] += 1
            else:
                person_counts[person] = 1
    
    # print(person_counts)

    most_person = None
    max_count = 0
    for person, count in person_counts.items():
        if count > max_count:
            most_person = person
            max_count = count
    
    return most_person


visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")