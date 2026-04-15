filename=r"M:\1st semester\python\student.txt"
def write_students():
    students={
        "111,prasad,90,85\n",
        "112,Divya,71,98\n",
        "113,sree,69,,92\n"
    }
    with open(filename,"w") as file:
        file.writelines(students)
    print("sample student data written to file.\n")


def read_students():
    print("\n student Records:")
    try:
        with open(filename,"r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please write data first.")


def append_student():
    roll=input("Enter Roll No: ")
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    marks=input("Enter Marks: ")

    with open(filename, "a") as file:
        file.write(f"{roll},{name},{age},{marks}\n")

    print("Student data appended successfully.\n")

while True:
    print("1.Write Sample Student Data")
    print("2. Read Student Data")
    print("3. Append New Student Data")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        write_students()
    elif choice=="2":
        read_students()
    elif choice=="3":
        append_student()
    elif choice=="4":
        print("Existing program.")
        break
    else:
        print("Invalid choice, try again")

        
