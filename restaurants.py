def most_varied_visitor(visits):
    # frequency dictionary:
    #   key will be person, value will be how many 
    #   restaurants they visited
    unique_visit_count = {}
    
    for visitors in visits.values():
        # remove duplicates
        # we only want to count a person once per restaurant
        unique_visitors = set(visitors)
        
        for visitor in unique_visitors:
            if visitor not in unique_visit_count:
                unique_visit_count[visitor] = 1
            else:
                unique_visit_count[visitor] += 1

    best_visitor = None
    most_visits = None
    for visitor, count in unique_visit_count.items():
        # update the most varied visitor if we find one with more visits
        if most_visits is None or count > most_visits:
            most_visits = count
            best_visitor = visitor

    return best_visitor


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

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if there is a tie?
A: You can assume there will not be a tie.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What should If there are no visitors in the input?
A: You can assume that at least one person will visit at least one restaurant.

Q: Does capitalization matter?
A: Yes, you the input is case-sensitive. You code should treat "Auberon" and "AUBERON" as two different people.

Q: Are these restaurants any good?
A: Yes, they're all excellent. In particular, definitely go to La Especial Norte if you're ever in San Diego.

--------------------------------------------------



---------Hints for struggling candidates----------

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

- If your candidate's code is returning "Xinting" for the second test case, remind them that a person may visit a restaurant multiple times, but we're interested in the number of *different* restaurants a person visits. (Xinting only visits two different restaurants, Auberon visits three)

-------------------------------------------------

"""