# (Challenge) I am going to switch it up a bit and allow you to be the teacher of your own class.
#Create three dictionaries: lloyd, alice, and tyler.
#Create three dictionaries: lloyd, alice, and tyler.
#Give each dictionary the keys "name", "homework", "quizzes", and "tests".
#Have the "name" key be the name of the student (that is, lloyd's name should be "Lloyd")and the other keys should be an empty list.
#myCode
lloyd = {"name": "Lloyd","homework": [],"quizzes": [],"tests": []}
alice = {"name": "Alice","homework": [],"quizzes" : [],"tests": []}
tyler ={"name": "Tyler","homework": [],"quizzes": [],"tests":[]}

#What's the Score?
#Now fill out your lloyd dictionary with the appropriate scores. To save you some time, we've filled out the rest for you.
#myCode
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#Put It Together
#create a list called students that contains lloyd, alice, and tyler.
#myCode
students = [lloyd,alice,tyler]

#For the Record
#print the student's name
#print the student's homework
#print the student's quizzes
#print the student's tests
#myCode
for x in students:
    print x["name"]
    print x["homework"]
    print x["quizzes"]
    print x["tests"]

#It's Okay to be Average
#Define a function called average that has one argument, numbers.
#Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
#Like the example above, use float() to convert total and store the result in total.
#Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
#Return that result.
#myCode
def average(numbers):
    total = sum(numbers) 
    total = float(total) / len(numbers)
    return total

#Just Weight and See
#Define a function called get_average that takes one argument called student.
#Make a variable homework that stores the average() of student["homework"].
#Repeat step 2 for "quizzes" and "tests".
#Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.
#myCode
def get_average(student):
    return  0.10 * average(student["homework"]) + 0.30 * average(student["quizzes"]) + 0.60 * average(student["tests"])
#another way
#myCode
def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    return ((homework * 0.10) +(quizzes * 0.30) +(tests * 0.60))

#Sending a Letter
#Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.
#Inside your function, test score using a chain of if: / elif: / else: statements, like so:
#If score is 90 or above: return "A"
#Else if score is 80 or above: return "B"
#Else if score is 70 or above: return "C"
#Else if score is 60 or above: return "D"
#Otherwise: return "F"
#Finally, test your function! Call your get_letter_grade function with the result of get_average(lloyd). Print the resulting letter grade.
#myCode
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print get_letter_grade(get_average(lloyd))

#Part of the Whole
#Define a function called get_class_average that has one argument students. You can expect students to be a list containing your three students.
#First, make an empty list called results.
#For each student item in the class list, calculate get_average(student) and then call results.append() with that result.
#Finally, return the result of calling average() with results.
#myCode
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

#Finally, print out the result of calling get_class_average with your students list. Your students should be [lloyd, alice, tyler]. 
#Then, print the result of get_letter_grade for the class's average.
#myCode
classList = [lloyd, alice, tyler]

print get_class_average(classList) 
print get_letter_grade(get_class_average(classList))


