import csv
def write_into_csv(info_list):
    with open("student1_info_csv","a+") as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact_num", "E-mail id"])
        writer.writerow(info_list)


if __name__=='__main__':
    condition=True
    student_num=1
    while (condition):
        student_info = input("Enter the school information for student #"+str(student_num)+" in the following format (Name Age Contact_Num E-mail): ")
        student_info_list= student_info.split(" ")
        print("The Entered information is")
        print("Name: "+student_info_list[0]+"\nAge: "+str(student_info_list[1])+"\nContact_Number"+str(student_info_list[2])+"\nEmail id "+str(student_info_list[3]))
        choice_check=input("is the entered information is correct ? (yes/no): ")
        if choice_check=="yes":
            write_into_csv(student_info_list)
            condition_check = input("Enter (yes/no) if you wants to entered information for the order student: ")

            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check=="no":
            print("please re-enter the values")







