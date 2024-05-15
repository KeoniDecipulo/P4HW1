#Keoni Decipulo
#P4HW1
#4/28/24
# Program uses a loop. After displaying score average (after dropping lowest score) , the program is to display a letter grade for the calculated average.

# Ask the user for the number of scores they want to enter
num_scores = int(input("Enter the number of scores you would like to enter: "))

# Create an empty list to store the scores
scores = []

# Loop to collect the scores
i = 0
while i < num_scores:
    score = float(input(f"Enter score #{i+1}: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        print("Score must be between 0 and 100")
        score = float(input(f"Enter score #{i+1}: "))
    scores.append(score)
    i += 1

# Display the lowest score entered
print('-----------Results-----------')
lowest_score = min(scores)
print("Lowest score :", lowest_score)

# Create a copy of the scores list to drop the lowest score
modified_scores = scores.copy()
modified_scores.remove(lowest_score)

# Display the modified score list after dropping the lowest score
print("Modified list:", modified_scores)

# Calculate the average of scores in the modified list
average_score = sum(modified_scores) / len(modified_scores)
print("Scores average :", average_score)

# Determine the letter grade for the average score
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the letter grade to the user
print("Grade:", letter_grade)
print('----------------------------')


