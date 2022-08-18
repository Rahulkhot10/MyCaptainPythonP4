import importlib
import csv

def  Write_into_csv(split_info_list):
    with open("studentData.csv",'a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["NAME","CLASS","ROLLNO","CONTACT"])
            
        
        writer.writerow(split_info_list)


if __name__=='__main__':
    condition=True
    while(condition==True):

        
        student_info=input("Enter the student info in following order (Name Class rollNo phoneNumber)\n")
        student_info_split=student_info.split(" ")
        print("Entered Info of student is\n 1.Name:{}\n 2.Class:{}\n 3.RollNo:{}\n 4.Contact Number:{}\n".format(student_info_split[0],student_info_split[1],student_info_split[2],student_info_split[3]))

        print("check if info entered correctly\n")

        info_check=input("write this to file (yes/no):")
        if 'yes' in info_check:
            Write_into_csv(student_info_split)
        
        condition_check=input("Enter more student info?(yes/no)")
        if condition_check=='yes':
            condition=True
        else:
            condition=False

        

