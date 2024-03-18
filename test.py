import os
import pytest
from main import init_database, fill_random_data, Clients, Orders


def test_init():
    init_database()
    assert os.path.exists("my_database.db")


def test_col_clients():
    assert 'name' in Clients._meta.fields
    assert 'city' in Clients._meta.fields
    assert 'address' in Clients._meta.fields


def test_col_orders():
    assert 'client' in Orders._meta.fields
    assert 'date' in Orders._meta.fields
    assert 'amount' in Orders._meta.fields
    assert 'description' in Orders._meta.fields


def test_rows():
    init_database()
    fill_random_data()
    assert Clients.select().count() >= 10
    assert Orders.select().count() >= 10

