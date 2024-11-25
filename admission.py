from csv import DictWriter
from csv import DictReader

while True:
    print(" **** WELCOME TO ADMISSION PORTAL OF NARAYANA ENGINEERING COLLEGE,NELLORE ****")
    print('1.For the details of the college click a')
    print('2.For registering into b tech stream click b')
    print('3.For the details of students already registered click c')
    print("4.To exit from the portal click d”)    #prints the portal interface
    n=input()      #takes the input to perform above operations
    if n=="a":
        print('''   NARAYANA EDUCATIONAL INSTITUTIONS are one of the best education providers in 
        India from the pre-primary to professional post graduation, have been successful in an 
        uninterrupted and dedicated task. We proudly accept that ocean of parents dreams came 
        into reality by our uncompromising education system, which is taken up for the cause of 
        educating young minds.
        streams offered >> Computer Science and Engineering
                        >> Electronics and Communication Engineering
                        >> Electrical and Electonical engineering
                        >> Mechanical Engineering
                        >> Civil Engineering
         ''')   #prints info about the college

    elif n=="b":
        first_name=input('Please enter your first name: ')     
        last_name=input('Please enter your last name: ')
        Date_of_Birth=input('Please enter your Date of Birth: ')
        Class_12_percentage=input('Please enter your class 12 percentage: ')
        Interested_stream=input('Please enter your Interested stream please check details for streams offered: ')
        Mobile_num=input('Please enter your Mobile num: ')
        Email=input('Please enter your Email: ')
        Address=input('Please enter your Address: ')  #collecting user info for registration
        name=first_name+last_name
        print("To submit please click y")
        print('To stop please click n’)  #asking user for the confirmation
        q=input() #taking input for the confirmation
        if q=="n":
            break      #stops the program if user thinks he/she  entered the wrong data
        if q=="y":
            with open(‘file2.csv’,’a’) as f:
             csv_writer=DictWriter(f,fieldnames=['Name_of_the_Student',"stream_chosen","email"])
             csv_writer.writeheader()
             csv_writer.writerow({
             "Name_of_the_Student":name,
             "stream_chosen":Interested_stream,
             "email":Email
             })         #appends the important details (name, stream, email)of user to a csv file
    elif n=="c": 
            with open(‘file2.csv','r') as s:
             csv_reader=DictReader(s)
             for row in csv_reader:
                print(row["Name_of_the_Student"])
                print(row["stream_chosen"])
                print(row["email"])     #displays the details append to the csv file
    elif n=="d":
      break  #exits the program or the admisision portal
