# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
inFile = open("questions.txt", 'r')
correctan = 0
contents = inFile.readlines()

for i in range(0, len(contents), 6):
     print(contents[i].strip('\n')) 
     print(contents[i+1].strip('\n'))  
     print(contents[i+2].strip('\n'))  
     print(contents[i+3].strip('\n'))  
     print(contents[i+4].strip('\n'))  
     correctanswer = contents[i+5].strip('\n')
     ipans = input("Answer: ").strip().upper() 
     if ipans == correctanswer.upper():
          print("Correct")
          correctan += 1
     else:
          print("Wrong")
     
     print(f"Correct answers: {correctan}\n")

inFile.close()
