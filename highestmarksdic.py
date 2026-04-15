students={
    "alice":85,
    "bob":92,
    "charlie":78,
    "kavid":90
}

highest_marks=max(students.values())

top_students=[name for  name , marks in students.items() if
              marks==highest_marks]
print("highest_marks:",highest_marks)
print("top students(s):", ", ".join(top_students))
              
