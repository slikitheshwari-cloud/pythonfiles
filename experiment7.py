try:
    source=input("Enter source file name:")
    destination=input("Enter destinatin filename:")
    f1=open(source,"r")
    data=f1.read()
    f2=open(destination,"w")
    f2.write(data)
    f1.close()
    f2.close()
    print("File copied successfully!")
except FileNotFoundError:
    print("Error:Source file not found")
except Exception as e:
    print("Unexcepted error occured:",e)
    
