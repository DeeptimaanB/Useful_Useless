import re
string = open('script.txt', 'r+', encoding="utf8").read()
new_str = re.sub("[^A-Za-z0-9]", " ", string)
new_str=new_str.lower()
open('script2.txt', 'w').write(new_str)

useless = []
useful = []

file = open('useless.txt','a+', encoding="utf8")
file.close()
file = open('useful.txt','a+', encoding="utf8") 
file.close()

with open('useless.txt','r+', encoding="utf8") as file:
      
    for line in file:
          
        for word in line.split():   

            useless.append(word)

file.close()

with open('useful.txt','r+', encoding="utf8") as file:
      
    for line in file:
          
        for word in line.split():   

            useful.append(word)

file.close()

print("0 for useless and 1 for useful and any other key to exit")


flag=0

with open('script2.txt','r', encoding="utf8") as file:
      
    for line in file:
          
        for word in line.split():   
            if(word in useful):
                continue
            if(word in useless):
                continue

            print(word)

            a=input("Is it necessarry : ")
            
            if(a=="0"):
                useless.append(word)
                with open('useless.txt','a', encoding="utf8") as file2:
                    file2.write(word+"\n")
                    file2.close()

            elif(a=="1"):
                useful.append(word)
                with open('useful.txt','a', encoding="utf8") as file2:
                    file2.write(word+"\n")
                    file2.close()
            
            else:
                exit()

input('Press ENTER to exit') 


