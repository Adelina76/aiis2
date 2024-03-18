from peewee import *

db = SqliteDatabase('my_database.db')


class Clients(Model):
    name = CharField()
    city = CharField()
    address = CharField()

    class Meta:
        database = db


class Orders(Model):
    client = ForeignKeyField(Clients, backref='orders')
    date = DateField()
    amount = IntegerField()
    description = CharField()

    class Meta:
        database = db


def create_tables():
    # Создание таблиц
    with db:
        db.create_tables([Clients, Orders])


def drop_tables():
    # Удаление таблиц
    with db:
        db.drop_tables([Clients, Orders])


def init_database():
    drop_tables()
    create_tables()


def fill_random_data():
    from random import randint, choice

    client_names = ['John', 'Alice', 'Bob', 'Megan']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
    addresses = ['123 Main St', '456 Elm St', '789 Oak St']

    with db.atomic():
        for _ in range(10):
            client = Clients.create(name=choice(client_names),
                                    city=choice(cities),
                                    address=choice(addresses))

            Orders.create(client=client,
                            date='2022-01-01',
                            amount=randint(10, 100),
                            description='Test order')


def show_table(table_name):
    if table_name == 'clients':
        rows = Clients.select()
        for row in rows:
            print(f'{row.name}\t{row.city}\t{row.address}')
    elif table_name == 'orders':
        rows = Orders.select()
        for row in rows:
            print(f'{row.client}\t{row.date}\t{row.amount}\t{row.description}')
    else:
        print('Table not found')
        return




def show_help():
    print('Usage:')
    print('\tWithout parameters - show help')
    print('\tinit - create database')
    print('\tfill - fill tables with random data')
    print('\tshow [tablename] - show contents of a specific table')


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        show_help()
    elif sys.argv[1] == 'init':
        init_database()
    elif sys.argv[1] == 'fill':
        fill_random_data()
    elif sys.argv[1] == 'show':
        if len(sys.argv) != 3:
            print('Please provide table name')
        else:
            show_table(sys.argv[2])
    else:
        show_help()