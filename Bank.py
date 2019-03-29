class Bank:
    def __init__(self, name):
        self.name = name
        self.list_of_clients = []

    def transfer_money(self, client_sending, client_reciving, money_amount):
        self.check_if_client_exists(client_sending,client_reciving)
        client_sending.money -= money_amount
        client_reciving.money += money_amount

    def add_client(self, client):
        self.list_of_clients.append(client)

    def check_if_client_exists(self, *clients_to_check):
        for client in clients_to_check:
            if client in self.list_of_clients:
                return
            else:
                raise Exception("This client dont exists in bank")
    
    

class Client:
    def __init__(self, money):
        self.money = money