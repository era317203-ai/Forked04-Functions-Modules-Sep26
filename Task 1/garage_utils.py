import re
from datetime import datetime
import itertools as it

""" Модуль для работы со списком клиентов СТО"""

def show_all(clients):
    """Выводит всех клиентов в удобном формате."""
    for client in clients:
                                                                            # for index in range(len(client)):
            print (client[1])
   
   
    # for client in clients:
    #       print(
    #         f"ID: {client[0]}, "
    #         f"Имя: {client[1]}, "
    #         f"Марка: {client[2]}, "
    #         f"Год выпуска: {client[3]}, "
    #         f"Стоимость обслуживания: {client[4]}"
    #     )


def filter_by_brand(clients, brand):
    """Возвращает список клиентов указанной марки автомобиля."""
    # pattern = re.compile(f"^{re.escape(brand)}$", re.IGNORECASE) не заработало при нижнем регистре, хотя и должно
    # return [
    #     client for client in clients
    #     if pattern.match(client[2])
    # ]
    pattern = re.compile(f"^{re.escape(brand.lower())}$")
    return [
        client for client in clients
        if pattern.match(client[2].lower())
    ]

def add_service_cost(clients, index, amount):
    """Добавляет сумму к стоимости обслуживания клиента по номеру в списке."""
    clients[index][4]+=amount

def delete_by_index(clients, index):
    """Удаляет клиента по номеру в списке."""
    del clients[index]
    

def get_most_expensive(clients):
    """Возвращает клиента с максимальной стоимостью обслуживания."""
    for client in clients:
         max_cost = max(client[4] for client in clients)
    for client in clients:
        if client[4] == max_cost:
             print (client)
    

def delete_older_than(clients, years):
    """Удаляет всех клиентов, чьи машины старше указанного количества лет."""
    older_years = datetime.now().year - years
        # for client in clients:
        #      if client[3] <= older_years:
        #           del client 
    for client in range(len(clients) - 1, -1, -1):
        if clients[client][3] <= older_years:
            del clients[client]

         
def group_by_brand(clients):
    """Группирует клиентов по марке с использованием itertools.groupby."""
    sorted_clients = sorted(clients, key=lambda client: client[2])
    # for key, group in it.groupby(sorted_clients, lambda client: client[2]):
    #     for sorted_clients in group:
    for brand, group in it.groupby(sorted_clients, lambda client: client[2]):
        names = [client[1] for client in group]
        print(f"{brand}: {names}")
            # print("A %s is a %s." % (sorted_clients[1], key))
      


