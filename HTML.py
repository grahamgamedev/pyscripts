time = 0
output = ""
number = int(input("number "))
coulor = input("colour ")
for time in range(number):
    line = '<h1 style= "color:' + coulor + '">' + str(time) + '</h1>'
    output += line

f = open("output.txt","w")
f.write(output)
f.close()

print("done")
input("Press enter to exit...")


    
    
