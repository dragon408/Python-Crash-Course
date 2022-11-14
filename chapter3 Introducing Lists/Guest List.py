#If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.

guests = ['Symonenko', 'Schildt', 'Nietzsche']

def Guest(L):
    for i in range(len(L)):
        print("\nHello " + L[i] + " I invite you to dinner!")
    print('\n')
Guest(guests)

#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•	 Start with your program from Exercise 3-4. Add a print statement at the
#end of your program stating the name of the guest who can’t make it.
#•	 Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#•	 Print a second set of invitation messages, one for each person who is still
#in your list.
import random

who_cant_make_the_dinner = random.randint(0, 1)
guests.pop(who_cant_make_the_dinner)
print(guests[who_cant_make_the_dinner] + " cant make the dinner\n")
Guest(guests)
