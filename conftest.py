
import pytest
from main import BooksCollector


@pytest.fixture()
def collector_with_test_data():
    collector = BooksCollector()
    collector.books_genre = {
            "Оно": "Ужасы",
            "Дюна": "Фантастика",
            "12 стульев":  "Комедии",
            "Сияние": "Ужасы",
            "1984": "Фантастика",
            "Задача трех тел": "Фантастика",
            "Шерлок Холмс": "Детектив"
        }
    return collector

