#Q write a program to count the occurence of word "INDIA" in atext file india.txt
file_path = 'india.txt'
word = 'INDIA'
word_lower = word.lower()
count = 0
with open(file_path, 'r') as file:
    for line in file:
        line_lower = line.lower()
        words = line_lower.split()
        print(words)
        for w in words:
            if w == word_lower:
                count += 1

print(f"The word '{word}' occurs {count} times in the file '{file_path}'.")




#Q write a program to count the number of vowels and constants in a file "Myfile.txt"
filename = 'Myfile.txt'

vowels = 'AEIOUaeiou'
vowel_count = 0
consonant_count = 0

try:
    with open(filename, 'r') as file:
        text = file.read()
        for char in text:
            if char.isalpha():  # Check if the character is an alphabet
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
    
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")





#Qwrite a program to count and display number of words starting with "i" in file Word.txt
filename = 'Word.txt'

file = open(filename, 'r')
text = file.read()
file.close()

words = text.split()
count = 0

for word in words:
    if word.lower().startswith('i'):
        count += 1

print(f"Number of words starting with 'i': {count}")





#Q write a program to display the lines having more than five words in a file Notes.txt
filename = 'notes.txt'

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        word_count = len(line.split())
        if word_count > 5:
            print(line.strip())
            


#Q write a program to create a binary file "Stu.dat" and Enter students rollno.,name and marks till the user wants.         
import pickle

filename = 'Stu.dat'

students = []

while True:
    rollno = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    
    student = {
        'rollno': rollno,
        'name': name,
        'marks': marks
    }
    
    students.append(student)
    
    cont = input("Do you want to add another student? (yes/no): ").strip().lower()
    if cont != 'yes':
        break

with open(filename, 'wb') as file:
    pickle.dump(students, file)

print("Student data has been written to Stu.dat")







#Q write a program to read a binary file "stu.dat" and display the record of students having marks greater than 81
import pickle

filename = 'Stu.dat'

with open(filename, 'rb') as file:
    students = pickle.load(file)

print("Students with marks greater than 81:")
for student in students:
    if student['marks'] > 81:
        print(f"Roll Number: {student['rollno']}, Name: {student['name']}, Marks: {student['marks']}")