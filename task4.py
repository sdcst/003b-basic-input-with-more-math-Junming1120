#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""
N = input("Enter a person's name: ")
A = input("Enter an adjective: ")
B = input("Enter a food: ")
C = input("Enter another adjective: ")
D = input("Enter a noun: ")
E = input("Enter the name of a place: ")
F = input("Enter a verb: ")
G = input("Enter an adverb: ")
H = input("Enter another food: ")
I = input("Enter a thing: ")
print(f"Today we picked apple from {N}'s Orchard. I had no idea there were so many different varieties of apples. I ate {A} apples straight off the tree that tasted like {B}. Then there was a {C} apple that looked like a {D}.  When our bag was full, we went on a free hay ride to {E} and back. It ended at a hay pile where we got to {F} {G}. I can hardly wait to get home and cook with the apples. We are going to make apple {H} and {I} pies!")

