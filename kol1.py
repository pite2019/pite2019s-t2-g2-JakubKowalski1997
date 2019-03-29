from Bank import Bank, Client

def main():
    print("Welcome to banking world")
    client1 = Client(100)
    client2 = Client(200)
    bank = Bank("Alior")
    bank.add_client(client1)
    bank.add_client(client2)
    print(client1.money)
    bank.transfer_money(client1, client2, 100)
    print(client1.money)

if __name__ == "__main__":
    main()