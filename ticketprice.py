total = 0
#declare ticket current ticket price value
p = 1
#initate while loop that counts to 5
while p <= 5:
    #prompt for user input
    age = input()
    #if statement to test if kids are older or equal to 3
    if int(age) >= 3:
        #set total variable to 100
        total += 100
        #set counter to increment by 1
        p += 1
        #if statement to test if kids are younger than 3
    if int(age) < 3:
        #set total to 0
        total += 0
        #set counter to increment by 1
        p += 1
        #continue to loop
print(total)

