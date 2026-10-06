import garage_utils as gu

clients = [
    [1, "Иван Петров", "Toyota", 2015, 250],
    [2, "Анна Смирнова", "BMW", 2018, 480],
    [3, "Сергей Ковалев", "Audi", 2012, 390],
    [4, "Мария Иванова", "Volkswagen", 2010, 210],
    [5, "Дмитрий Орлов", "Mercedes", 2019, 520],
    [6, "Ольга Сидорова", "Toyota", 2016, 300],
    [7, "Алексей Жуков", "Ford", 2013, 180],
    [8, "Елена Кравцова", "Kia", 2020, 260],
    [9, "Павел Лебедев", "Hyundai", 2017, 240],
    [10, "Ирина Фролова", "BMW", 2014, 450],
    [11, "Николай Громов", "Renault", 2011, 170],
    [12, "Татьяна Белова", "Audi", 2019, 510]
]

def show_menu():
    print("""
1 — вывести всех клиентов
2 — вывести клиентов заданной марки
3 — изменить сумму обслуживания
4 — удалить клиента
5 — найти самую дорогую машину
6 — удалить машины старше n лет
7 — сгруппировать клиентов по марке
0 — выход
""")

#  print(f"Удалено клиентов за сессию: {get_count()}")
#                   break    
    
def main():

    while True:
        choice = input("Выберите пункт: ")

        match choice:
          case "1":
            print("\nВсе клиенты:")
            gu.show_all(clients)
          case "2":
            print("\nВывести клиентов заданной марки: ")
            brand = (input("Введите марку машины: "))
            result = gu.filter_by_brand(clients,brand)
            print(result)

          case "3":
              print("\nИзменить сумму обслуживания:")
              nomer = int(input("\nВведите номер клиента: "))
              summa = int(input("\nВведите сумму обслуживания: "))
              gu.add_service_cost(clients,nomer,summa)

          case "4":
              print("\nУдалить клиента:")
              nomer = int(input("\nВведите номер клиента: "))
              gu.delete_by_index(clients,nomer)

          case "5":
            print("\nНайти самую дорогую машину:")
            gu.get_most_expensive(clients)

          case "6":
            print("\nУдалить машины старше N лет:")
            years = int(input("\nВведите N лет: "))
            gu.delete_older_than(clients,years)


          case "7":
            print("\nГруппирует клиентов по марке с использованием itertools.groupby.:")
            gu.group_by_brand(clients)
        
          case "0":
            print("\nПрограмма завершена.")
            break
            
  
#    gu.show_all(clients)
#    gu.add_service_cost(clients,10,30)
#    print (clients[10])
#    gu.delete_by_index(clients,5)
#    gu.show_all(clients)
#    gu.get_most_expensive(clients)

if __name__ == "__main__":
    main()