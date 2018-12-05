#!/usr/bin/env python3
message = 'You will receive the following letter grade: '
print('What is your overall your current score for this class?')
score = float(input())
if score <= 100 and score >= 90:
    message = message + 'A. Great job!'
elif score <= 89 and score >= 80:
    message = message + 'B. Solid work!'
elif score <= 79 and score >= 70:
    message = message + 'C. Very Average.'
elif score <= 69 and score >= 60:
    message = message + 'D. Bit of a disappointment.'
elif score <= 59 and score >= 0:
    message = message + 'F. Epic failure.'
else:
    message = message + 'Please enter a valid course score.'
print(message)