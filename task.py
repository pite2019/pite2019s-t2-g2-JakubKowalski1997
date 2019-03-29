#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

from Bank import Bank, Client

def main():
    print("Welcome to banking world")
    client1 = Client(100, "Jakub Kowalski")
    client2 = Client(200, "Jan Nowak")
    bank = Bank("Alior")
    bank.add_client(client1)
    bank.add_client(client2)
    print("First client money: {}".format(client1.money))
    print("Second client money: {}".format(client2.money))
    bank.transfer_money(client1, client2, 100)
    print("First client money: {}".format(client1.money))
    print("Second client money: {}".format(client2.money))
    
    print("First client money: {}".format(client1.money))
    bank.input_cash(client1, 100)
    print("First client money: {}".format(client1.money))

    print("Second client money: {}".format(client2.money))
    bank.withdraw_cash(client2, 100)
    print("Second client money: {}".format(client2.money))

    bank.print_report_to_json()


if __name__ == "__main__":
    main()