class Bank:
    def __init__(self, name, client):
        self.client = client

    def transfer_money(self, client_sending, client_reciving, money_amount):
        client_sending.money -= money_amount
        client_reciving.money += money_amount