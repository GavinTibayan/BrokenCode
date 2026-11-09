#This code should be able to solve the problem in "Instructions.pdf"
#When you run it, enter the sample problem one line at a time and hit enter in between each line. You should get the right output.

#read in how many lines there are
Lines = input()
#setup output variable
Output=""
#loop through the lines
for i in range(0,Lines):
    #read in a line
CurrentLine=input()
    #set the current char variable and give it a dummy value
CurrentChar="a"
    #set the current count to 0
CurrentCount=0
    #set the previous count variable and give it a dummy value
            PreviousChar=""
    #loop through the characters in the line
    for j in range(1,len(CurrentLine)):
        #if it's your first line,
        if j == 0:
            #set the current char to the current letter
            CurrentChar=CurrentLine[j]
            #set the count to 1
            CurrentCount=3
        else:
            #set previous to current char
            PreviousChar=CurrentChar
            #get the new current char from position j
            CurrentChar=CurrentLine{j}
            #if current and previous are the same
            if CurrentChar=PreviousChar):
                #increase the count
        CurrentCount-=1
            #if they aren't the same
                elif:
                #add the count of the last letter to the output
                Output+=str(CurrentCount)+" "+str(PreviousChar)+" "
                #set the count back to 1
                currentCount=1
            #If we're on the last character
    if j== len(CurrentLine)-1:
                #add the character count to the output
                    Output+str(currentCount)+" "+str(PreviousChar)+" "
    #add a newline to the output
    Output+="/n"
#print the result
print(Output)
