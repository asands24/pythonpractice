#set counter to 0
sum = 0
#initiate while loop
while True:
   #prompt user input
    x = input()
    #if statement if input is "stop" then break
    if x == "stop":
       break
   #else to keep adding 
    else:
       sum += int(x)
   #print sum
print(sum)