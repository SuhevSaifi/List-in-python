# List-in-python
# to Display the name of students whose marks in english is greator than 50 

list1 = [
    ["stdid", 'stdname', "standard", "age", "Hindi", "English", "Science", "Computer", "total"],
    ['std01','Aashish Kumar', '10th', 15, 67, 89, 87, 89, 90, 422],
    ['std02',"Abhishek Kumar", "10th", 14, 85, 45, 48, 90, 45, 313],
    ['std03',"Aman", '10th', 15, 23, 56, 78, 78, 67, 302],
    ['std04',"Rahul", "10th", 14, 45, 67, 58, 49, 39, 230],
    ["std05","Suhev","10th", 19,49,68,56,78,91,361],
    ["std06","Nikhil","10th",20,48,58,69,80,84,359]
]
for i in list1:
    print(i)

# Iterate over the student data starting from the second row (index 1)
for student in list1[1:]: #we can use range(1,len(list1)) also 
    # student[5] corresponds to the "English" marks
    if student[5] > 50:
        print(student[1])  # student[0] corresponds to the "stdname"

        

#Display the name of students and age of top four scorer

# Extracting student data (excluding headers)
students = list1[1:]

# Sorting students based on total scores (last element in each list)
top_students = sorted(students, key=lambda x: x[-1], reverse=True)[:4]

# Printing top 4 scorers and their ages
for student in top_students:
    stdid, stdname, standard, age, *scores, total = student
    print(f"Student ID: {stdid}, Name: {stdname}, Age: {age}, Total Score: {total}")           


#Display Name,id,age of students who are bottom three scorer in computer # Extracting student data (excluding headers)
students = list1[1:]

# Sorting students based on science score (last element in each list)
bottom_students = sorted(students, key=lambda x: x[-1])[:3]

# Printing bottom 3 scorers with their id ,name , age
for student in bottom_students:
    stdid, stdname, standard, age,*scores, total = student 
    print(f"Student ID: {stdid}, Name: {stdname}, Age: {age}")
       
