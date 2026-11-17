import mysql.connector
import pickle
from datetime import datetime

db = mysql.connector.MySQLConnection(
    host="localhost",
    user="root",
    password="advaymysql123",
    database="test"
)

cursor = db.cursor()
'''
cursor.execute("create table attempts(id int Primary Key not null, quiz_name varchar(50) not null, username varchar(50) not null, score int not null, total int not null, detailed_attempt blob, date varchar(20));")
db.commit()
cursor.execute("create table quizzes(name varchar(50) not null, content blob);")
db.commit()
cursor.execute("create table accounts(username varchar(50) not null, pass varchar(30) not null);")
db.commit()

quiz1 = pickle.dumps({1:["What is 9+10?","19"],2:["Divide 50 by 5?","10"],3:["Square root of 49?","7"],4:["Give value of 5!","120"]})
cursor.execute("INSERT INTO quizzes VALUES('Math Test by Advay', %s)", (quiz1,))
db.commit()
quiz2 = pickle.dumps({1:["What is the capital of France?","Paris"],2:["How many days are in a leap year?","366"],3:["Which planet is known as the Red Planet?","Mars"],4:["What is H2O commonly known as?","Water"],5:["How many continents are there on Earth?","7"]})
cursor.execute("INSERT INTO quizzes VALUES('Basic Knowledge by User', %s)", (quiz2,))
db.commit()
quiz3 = pickle.dumps({1:["What is 12+8?","20"],2:["What is 15-6?","9"],3:["What is 9x9?","81"],4:["What is 100/25?","4"],5:["What is the cube of 3?","27"]})
cursor.execute("INSERT INTO quizzes VALUES('Basic Math by New', %s)", (quiz3,))
db.commit()
quiz4 = pickle.dumps({1:["What gas do humans need to breathe?","Oxygen"],2:["Which part of the plant makes food?","Leaf"],3:["What is the boiling point of water in Celsius?","100"],4:["Which organ pumps blood in the body?","Heart"],5:["What force pulls objects toward Earth?","Gravity"]})
cursor.execute("INSERT INTO quizzes VALUES('Basic Science by User', %s)", (quiz4,))
db.commit()

cursor.execute("insert into accounts values('Advay','123');")
db.commit()
cursor.execute("insert into accounts values('Test','456');")
db.commit()
cursor.execute("insert into accounts values('User','abcd');")

att1 = pickle.dumps({1:["What is 9+10?","19","19",1],2:["Divide 50 by 5?","10","10",1],3:["Square root of 49?","7","6",0],4:["Give value of 5!","120","119",0]})
cursor.execute("INSERT INTO attempts VALUES(1,'Math Test by Advay','Advay',2,4,%s,'2025-09-10');", (att1,))
db.commit()
att2 = pickle.dumps({1:["What is the capital of France?","Paris","Paris",1],2:["How many days are in a leap year?","366","365",0],3:["Which planet is known as the Red Planet?","Mars","Mars",1],4:["What is H2O commonly known as?","Water","Water",1],5:["How many continents are there on Earth?","7","6",0]})
cursor.execute("INSERT INTO attempts VALUES(2,'Basic Knowledge by User','User',3,5,%s,'2025-09-11');", (att2,))
db.commit()
att3 = pickle.dumps({1:["What is 12+8?","20","20",1],2:["What is 15-6?","9","8",0],3:["What is 9x9?","81","81",1],4:["What is 100/25?","4","4",1],5:["What is the cube of 3?","27","26",0]})
cursor.execute("INSERT INTO attempts VALUES(3,'Basic Math by New','Test',3,5,%s,'2025-09-12');", (att3,))
db.commit()
att4 = pickle.dumps({1:["What gas do humans need to breathe?","Oxygen","Oxygen",1],2:["Which part of the plant makes food?","Leaf","Stem",0],3:["What is the boiling point of water in Celsius?","100","100",1],4:["Which organ pumps blood in the body?","Heart","Heart",1],5:["What force pulls objects toward Earth?","Gravity","Gravitation",0]})
cursor.execute("INSERT INTO attempts VALUES(4,'Basic Science by User','User',3,5,%s,'2025-09-13');", (att4,))
db.commit()
att5 = pickle.dumps({1:["What is 9+10?","19","20",0],2:["Divide 50 by 5?","10","9",0],3:["Square root of 49?","7","7",1],4:["Give value of 5!","120","120",1]})
cursor.execute("INSERT INTO attempts VALUES(5,'Math Test by Advay','Test',2,4,%s,'2025-09-14');", (att5,))
db.commit()
att6 = pickle.dumps({1:["What is the capital of France?","Paris","Lyon",0],2:["How many days are in a leap year?","366","366",1],3:["Which planet is known as the Red Planet?","Mars","Jupiter",0],4:["What is H2O commonly known as?","Water","Water",1],5:["How many continents are there on Earth?","7","7",1]})
cursor.execute("INSERT INTO attempts VALUES(6,'Basic Knowledge by User','Advay',3,5,%s,'2025-09-15');", (att6,))
db.commit()
'''

def log_in():
    print("--------- LOG IN WINDOW ---------")
    user = input("Enter your username: ")
    passwd = input("Enter your password: ")

    cursor.execute("select username from accounts")
    nm = cursor.fetchall()
    for x in nm:
        if x[0] == user:
            cursor.execute("select pass from accounts where username = '{}'".format(user))
            pass_corr = (cursor.fetchall())[0][0]
            if pass_corr == passwd:
                return(user)
            else:
                print("Incorrect Password!")
                break
    else:
        print("No username found!")

def sign_in():
    print("--------- SIGN IN WINDOW ---------")
    user = input("Enter New Username: ")
    passwd = input("Enter your Password: ")

    cursor.execute("select username from accounts")
    nm = cursor.fetchall()

    for x in nm:
        if x[0] == user:
            print("Username already taken!")
            break
    else:
        cursor.execute("insert into accounts values('{}','{}');".format(user, passwd))
        db.commit()
        print("Account Created!")

def take_quiz(username):
    # List available quizzes
    cursor.execute("SELECT name FROM quizzes")
    nm = cursor.fetchall()
    quizzes = []
    for x in nm:
        quizzes.append(x)

    if quizzes:
        print("----------------------------------")
        print("        AVAILABLE QUIZZES")
        print("----------------------------------")
        for i in quizzes:
            print(quizzes.index(i)+1,"-",i[0])
        print("----------------------------------")
        while True:
            try:
                quiz_no = int(input("** Enter quiz number:"))-1
                break
            except:
                print("Invalid")
        cursor.execute("SELECT content FROM quizzes WHERE name = %s", (quizzes[quiz_no][0],))
        quiz_name = quizzes[quiz_no][0]
        q = cursor.fetchone()[0]
        quiz = pickle.loads(q)
    else:
        print("* No Quizzes Found!")

    print("\n----------------------------------")
    print(" "*((34-len(quiz_name))//2) + quiz_name.upper() + " "*((34-len(quiz_name))//2))
    print("----------------------------------")

    # Take quiz
    score = 0
    attempt = {}

    for i in list(quiz):
        question = quiz[i][0]
        corr_ans = quiz[i][1]
        print("# QUESTION",i)
        print(question)
        ans = input("\n> Enter answer: ")
        if ans == corr_ans:
            score += 1
            attempt[i] = [question,corr_ans,ans,1]
        else:
            attempt[i] = [question,corr_ans,ans,0]
        print()

    total = len(quiz)
    percentage = (score / total) * 100

    a = pickle.dumps(attempt)

    current_datetime = datetime.now()
    d = current_datetime.date()

    # Save attempt to database
    cursor.execute("INSERT INTO attempts (quiz_name, username, score, total,detailed_attempt,date) VALUES (%s, %s, %s, %s,%s,%s)",(quiz_name, username, score, total,a,d))
    db.commit()

    print("------------- RESULT -------------")
    print(f"* Score: {score}/{total}\nPercentage: ({percentage}%)")
    print("-"*34)


def view_attempts(username,c):
    cursor.execute("SELECT quiz_name, score,total,detailed_attempt,date FROM attempts WHERE username = %s",(username,))
    attempts = cursor.fetchall()

    if attempts:
        print("\n" + "-"*34)
        print("     YOUR PREVIOUS ATTEMPTS")
        print("-"*34)
        for x in attempts:
            quiz_name = x[0]
            score = x[1]
            total = x[2]
            attempt = pickle.loads(x[3])
            d = x[4]
            percentage = (score / total) * 100
            print(f"\n## Quiz: {quiz_name}")
            print("## Attempted on:",d)
            print(f"## Score: {score}/{total} Percentage: {percentage}%")

            if c == 2:
                print("--------DETAILED ANALYSIS---------")
                for i in range(1,len(attempt)+1):
                    q = attempt[i][0]
                    corr_a = attempt[i][1]
                    a = attempt[i][2]
                    y = attempt[i][3]
                    if y == 1:
                        corr = "✔"
                    else:
                        corr = "✗"
                    print("Q",i,q)
                    print("Correct Ans:",corr_a)
                    print("Your Ans:",a)
                    print("Correct:",corr)
                    print()
                print("------------------------------")
    else:
        print("* No attempts found!")

def create_new_quiz():
    print("\n" + "-"*34)
    print("        CREATE A NEW QUIZ")
    print("-"*34 + "\n")

    while True:
        quiz_name = input(">> Enter Your Quiz Name: ").title() + " by " + username
        if quiz_name not in quizzes:
            break
        else:
            print("* There's already a quiz with this name!")
    questions = {}

    n = int(input(">> No of questions: "))
    for i in range(1,n+1):
        print("# QUESTION",i)
        q = input(">> Question: ")
        a = input(">> Answer: ")
        questions[i] = [q,a]
        print()

    ques = pickle.dumps(questions)

    cursor.execute("INSERT INTO quizzes VALUES (%s, %s)",(quiz_name, ques))
    db.commit()
    print("## Saved",quiz_name, "with", len(questions) ,"questions")
    print("-"*34)

def modify_quiz():
    while True:

        print("\n" + "-" * 34)
        print("        MODIFY YOUR QUIZ")
        print("-" * 34 + "\n")

        print("1. View your Quizzes")
        print("2. Delete your Quiz")
        print("3. Exit")

        ch = int(input("Choice: "))

        if ch == 1:
            print()
            if user_quizzes:
                print("---------- Your Quizzes ----------")
                for x in user_quizzes:
                    print(user_quizzes.index(x) + 1, "-", x)
                print("-"*34)
            else:
                print("* You have not made any quizzes yet!")

        elif ch == 2:
            if user_quizzes:

                print("---------- Your Quizzes ----------")
                for x in user_quizzes:
                    print(user_quizzes.index(x) + 1, "-", x)
                print("-" * 34)

                q = int(input("** Enter index of quiz to delete (0 for exit): "))
                if q != 0:
                    quizdel = user_quizzes[q - 1]
                    cursor.execute("DELETE FROM QUIZZES where name = {}".format(quizdel))
                    db.commit()
                    print("## Successfully deleted", quizdel)
            else:
                print("* You have not made any quizzes!")
            print("-" * 34)
        elif ch == 3:
            break
        else:
            print("Invalid")

# MAIN
while True:
    print("\n------------------------------")
    print("      WELCOME TO QUIZ APP     ")
    print("------------------------------")
    print("1. Log In")
    print("2. Sign In")
    print("3. Exit")
    print("------------------------------")

    while True:
        try:
            q = int(input("** Enter: "))
            break
        except:
            print("Invalid")
    print()

    if q == 1:
        username = log_in()
        if username:
            print("\n* Log In Successful!")
            print("---------------------------------\n")
        else:
            continue

        while True:

            cursor.execute("SELECT name from quizzes")
            nm = cursor.fetchall()
            quizzes = []
            user_quizzes = []
            # Create two lists -> 1) All Quizzes in database 2) Quizzes made by user
            for x in nm:
                a = x[0].partition(" by ")
                quizzes.append(x[0])  # 1)
                if a[2] == username:
                    user_quizzes.append(x[0])  # 2)

            print("\n" + "-"*34)
            print("            MENU")
            print("-"*34)
            print("\nWelcome",username)
            print("1. Attempt a quiz")
            print("2. View your previous attempts")
            print("3. Create Quiz")
            print("4. Modify your Quizzes")
            print("5. Sign Out")
            print("-"*34)

            choice = int(input("** Enter your choice: "))

            if choice == 1:
                take_quiz(username)

            elif choice == 2:
                print("What type of overview do you want?")
                print("1. General Overview")
                print("2. Detailed Analysis")
                c2 = int(input("Choice: "))
                view_attempts(username,c2)

            elif choice == 3:
                create_new_quiz()

            elif choice == 4:
                modify_quiz()

            elif choice == 5:
                break

            else:
                print("Invalid")

    elif q == 2:
        sign_in()

    elif q == 3:
        print("* Thank You For Using The Quiz App!")
        break

db.close()