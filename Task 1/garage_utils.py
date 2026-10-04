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
    


def add_service_cost(clients, index, amount):
    """Добавляет сумму к стоимости обслуживания клиента по номеру в списке."""
    clients[index][4]+=amount


def delete_by_index(clients, index):
    """Удаляет клиента по номеру в списке."""
    del clients[index]
    # print(f"Удалено клиентов за сессию: {get_count()}")
    #         break


def get_most_expensive(clients):
    """Возвращает клиента с максимальной стоимостью обслуживания."""
    for client in clients:
         max_cost = max(client[4] for client in clients)
    for client in clients:
        if client[4] == max_cost:
             print (client)
    


def delete_older_than(clients, years):
    """Удаляет всех клиентов, чьи машины старше указанного количества лет."""
    pass


def group_by_brand(clients):
    """Группирует клиентов по марке с использованием itertools.groupby."""
    pass

