values = [1, 2, "bharti", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0]) #1
print(values[3]) #4
print(values[2]) #bharti
print(values[-1])
print(values[1:3]) #[2, 'bharti']
values.insert(3, "Mahanta") #[1, 2, 'bharti', 'Mahanta', 4, 5]
print(values)
values.append("End") #[1, 2, 'bharti', 'Mahanta', 4, 5, 'End']
print(values)

values[2] = "Arti"  #[1, 2, 'Arti', 'Mahanta', 4, 5, 'End']
print(values)

del values[0]  #[2, 'Arti', 'Mahanta', 4, 5, 'End']
print(values)

#Tuple - same as list data type, but immutable

val = (1, 2, "Bharti", 4.5)
print(val) # (1, 2, 'Bharti', 4.5)


# Dictionary - Just remember that the string should be in double Quatation.

dic = {"a": 2 , 4: "b" , "c": "Hello World"}

print(dic["a"])  #2
print(dic["c"])  #Hello World
print(dic[4])    #b





