# list_question = ["Name", "Age", "DOB"]
# list_ans = ["Nahid", "21", "27"]
# Amount = 0
# for i in range(len(list_question)):
#     print("What is your ",list_question[i],"?")
#     user_input = input()
#     if(user_input == list_ans[i]):
#         print("Ans is valid")
#         Amount = Amount + 10000
#     else:
#         print("Ans is invalid")

# print(Amount)

Game_amount = ["1000", "2000", "3000", "5000", "10,000"]
questions = [
    ["What is my name ?", "Nahid", "Rasel", "Imran", "Rakibul", 1],
    ["What is my age ?", 21, 22, 23, 24, 1],
    ["What is my univercity ?", "DU", "AIUB", "DIU", "JU", 3],
    ["Who is my crush ?", "Tisha ma'am", "Porshi", "Instagram model", "None", 1],
    ["My current laptop brand ?", "DELL", "HP", "TOSHIBA", "WALTON", 2]
    ]
amount = "Null"
for i in range(len(questions)):
    question = questions[i]
    print(f"{question[0]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    Ans = int(input("Give the input: "))
    
    if(Ans == question[5]):
        print("Ans is valid")
        amount = Game_amount[i]

    else:
        print("Ans is invaid")

    print(f"Win amount is {amount}")