bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #just print all list
print(bicycles[0]) #print one elem(by [index])
print(bicycles[-1]) #print last elem


#Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'#change
print(motorcycles)
motorcycles.append('ducati')#Adding to the end of list
print(motorcycles)
motorcycles.insert(0, 'ducati')#Adding a new element at any position in your list
print(motorcycles)
del motorcycles[0]#Removing by index
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()#Removing an Item Using the pop() Method(last elem)
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)#Popping Items from any Position in a List
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')#remove by value
print(motorcycles)


#You can also use the remove() method to work with a value that’s being
#removed from a list. Let’s remove the value 'ducati' and print a reason for
#removing it from the list:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")


#Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#reverse 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
#reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
