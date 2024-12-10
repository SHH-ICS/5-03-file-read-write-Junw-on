# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.
with open("questions.txt", "w") as questiont:
    while True:
        print("Enter a multiple choice question. Enter stop to leave.")
        if input() == "stop":
            break
        else:
            question = input()
            print("Enter the choices.")
            A = input("A: ")
            B = input("B: ")
            C = input("C: ")
            D = input("D: ")
            print("Enter the letter of the answer.")
            answer = input()
            questiont.write(question + "\n")
            questiont.write("A: " + A + "\n")
            questiont.write("B: " + B + "\n")
            questiont.write("C: " + C + "\n")
            questiont.write("D: " + D + "\n")
            questiont.write(answer + "\n")

questiont.close()
