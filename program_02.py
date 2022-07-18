letter = '''Dear <|NAME|>,
Greetings from Sopra Steria. I am happy to tell you about you application for job.
Congratulations, You are selected for software engineer role in sopra steria.
Have a great professional journey with us!

Thanks & Regards
Harsh Joshi

Date: <|DATE|>
'''

name = input("Enter the Name\n")
date = input("Enter the Date\n")
letter = letter.replace('<|NAME|>', name)
letter = letter.replace('<|DATE|>', date)
print(letter)