fruit="mango"
mangolen= len(fruit)
print(mangolen)
print(fruit[0:4]) #including 0 but not 4
print(fruit[:4])
print(fruit[1:4])
print(fruit[:])

#negative slicing

print(fruit[0:-3]) #pyhton do this line as print(fruit[0:len(fruit)-3])
print(fruit[-1:-3]) #this is 5-1->4 & 5-3->2 i.e from [4:2] which does not make any sense but..
print(fruit[-3:-1]) #gives ng becoz 5-3&5-1 i.e [2:4]
 
x="abcde"
for i in x:
    print(i)
print("\n")    

# question

nm="ayush"
print(nm[-4:-2])
print("\n")

#answer-> yu

# converting strings
#strings  are immutable
#but can be changed by making a copy

#upper():
n="ayush"
print(n.upper()) 
c=n.upper()
print(c)
print(n)
print("\n")

#lower():
m="SINGH"
print(m.lower())
print(m)
print("\n")

#rstrip():
v="ayush!!!"
t="!!ayush!!!!!"
j="@yush@@"
k="!@yu$h!! !@"
print(v.rstrip("!"))
print(t.rstrip("!"))
print(j.rstrip("@"))
print(k.rstrip("!")) #can take only one argument
print("\n")

#replace():
a="!!aditya is the best!!aditya is good!!"
print(a.replace("aditya","ayush"))
print("\n")

#split():converts string into list 
w="!!aditya is the best!!aditya is good!!"
print(w.split(" ")) #splitting with space
print("\n")

#capitalize():
e="i am doinG coDing"
print(e.capitalize())
print("\n")

#centre():
p="welcome to my world"
print(len(p))
print(p.center(50))
print(len(p.center(50)))
print('\n')

#count(): return the count of the char/string whichever user wants
print(w.count("aditya"))
print(w.count(' ')) #counting spaces
print(w.count('i'))
print('\n')

#endwith():check if string ends with given value,if yes returns true else false and can even check value in between string by providing start
#and end index positions
print(t.endswith('!!'))
print(t.endswith('sh',1,7))
print('\n') 
