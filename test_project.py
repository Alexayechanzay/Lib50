import pytest

from classes import Book, Library, User
from project import ADMIN_PWD, display_menu, pwd_check


def test_pwd_check():
    assert pwd_check(ADMIN_PWD) is True
    assert pwd_check("wrong-password") is False


def test_check_availability():
    assert Book(1, "b", "a", 1).check_availability() is True
    assert Book(2, "p", "a", 0).check_availability() is False


def test_update_quantity():
    book = Book(1, "a", "b", 3)

    book.update_quantity(-1)

    assert book.quantity == 2

