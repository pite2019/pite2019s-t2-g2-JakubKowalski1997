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


if __name__ == "__main__":
    main()