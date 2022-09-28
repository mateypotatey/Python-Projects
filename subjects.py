class subjects:
    def __init__(self, name, score, credits):
        self.name = name
        self.score = score
        self.credits = credits

course = []

number_of_majors = int(input("How many majors did you do this semester? "))

# manually add each subject, the exam score for that subject, and the weighting of that subject. Then add it to a list for that particular student

for i in range(number_of_majors):
    n = input("Name of the subject: ")
    s = input("Exam score of the subject: ")
    c = int(input("How many credit points was this subject worth: "))
    unit = subjects(n, s, c)
    course.append(unit) #I want to put the created major into the list

for unit in course:
    print("Unit Name: ", unit.name, "Exam Score: ", unit.score, "Unit Credits: ", unit.credits)
