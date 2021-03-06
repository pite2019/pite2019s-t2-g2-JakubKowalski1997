import json

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

    def input_cash(self, client, money):
        self.check_if_client_exists(client)
        client.money += money

    def withdraw_cash(self, client, money):
        self.check_if_client_exists(client)
        client.money -= money 

    def check_if_client_exists(self, *clients_to_check):
        for client in clients_to_check:
            if client in self.list_of_clients:
                return True
            else:
                raise Exception("This client dont exists in bank")
    def print_report_to_json(self):
        self.data = ""
        self.data += "["
        for client in self.list_of_clients:
            self.data += "{Name: " + client.name + " "
            self.data += ",Money: " + str(client.money) + "}," 
        self.data +="]"
        with open('data.txt', 'w') as outfile:  
            json.dump(self.data, outfile)
    

class Client:
    def __init__(self, money, name):
        self.money = money
        self.name = name