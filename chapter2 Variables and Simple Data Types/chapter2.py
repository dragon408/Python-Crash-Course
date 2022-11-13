#just variable
message = "Hello world"
print(message)


#Some string methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


#Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
#print(full_name.title())
#print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)


#Adding Whitespace to Strings with Tabs or Newlines
print("Languages:\nPython\nC++\nJavaScript\n")
print("Languages:\n\tPython\n\tC++\n\tJavaScript")

#Stripping Whitespace
message = " hello world "
print((message.rstrip()) + "!")
print((message.lstrip()) + "!")
print((message.strip()) + "!")
