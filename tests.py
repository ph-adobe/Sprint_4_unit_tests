import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_books_collector_init_data(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
        assert collector.genre_age_rating == ["Ужасы", "Детективы"]

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.books_genre) == 2

    def test_add_new_book_genre_is_empty(self):
        collector = BooksCollector()
        book = "Гордость и предубеждение"
        collector.add_new_book(book)
        assert collector.books_genre.get(book) == ""

    def test_add_new_book_if_book_in_book_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.add_new_book("Гордость и предубеждение и зомби")
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize(
        "book_name",
        ["", "a"*41 ]
    )
    def test_add_new_book_book_name_length_validation_negative(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize(
        "book_name",
        ["a", "a"*40 ]
    )
    def test_add_new_book_book_name_length_validation_positive(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1


    @pytest.mark.parametrize(
        "book_name, genre",
        [
            ["1984", "Фантастика"],
            ["12 стульев", "Комедии"],
            ["О новый дивный мир", "Фантастика"]
        ]
    )
    def test_set_book_genre_when_it_was_empty_or_change_value_positive(self, book_name, genre):
        collector = BooksCollector()
        collector.books_genre = {
            "1984": "",
            "12 стульев": "Ужасы",
            "О новый дивный мир": "Фантастика",
        }

        collector.set_book_genre(book_name, genre)

        assert collector.books_genre.get(book_name) == genre


    def test_set_book_genre_if_book_not_in_collection_return_none(self):
        collector = BooksCollector()
        collector.books_genre = {
            "1984": "Фантастика",
            "12 стульев": "Комедии"
        }
        book_not_in_collection = "О дивный новый мир"
        genre = "Фантастика"

        collector.set_book_genre(book_not_in_collection, genre)
        assert collector.books_genre.get(book_not_in_collection) is None

    def test_set_book_genre_if_genre_not_in_collection_return_empty_str(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Маскарад": ""
        }

        book = "Маскарад"
        genre_not_in_collection = "Драма"

        collector.set_book_genre(book, genre_not_in_collection)
        assert collector.books_genre.get(book) == ""

    def test_get_book_genre_return_detective(self):
        collector = BooksCollector()

        collector.books_genre = {
            "Шерлок Холмс": "Детектив",
            "12 стульев": "Комедии"
        }
        book = "Шерлок Холмс"
        genre = "Детектив"

        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_empty_books_genre_return_none(self):
        collector = BooksCollector()
        book = "Шерлок Холмс"

        assert collector.get_book_genre(book) is None

    def test_get_books_with_specific_genre_return_three_books(self, collector_with_test_data):
        genre_to_search = "Фантастика"

        assert len(collector_with_test_data.get_books_with_specific_genre(genre_to_search)) == 3

    def test_get_books_with_specific_genre_if_genre_not_in_collection_return_none(self, collector_with_test_data):
        genre_to_search = "Драма"

        assert collector_with_test_data.get_books_with_specific_genre(genre_to_search) == []

    def test_get_books_with_specific_genre_if_genre_not_in_books_genre_return_empty_list(self, collector_with_test_data):
        genre_to_search = "Мультфильмы"

        assert collector_with_test_data.get_books_with_specific_genre(genre_to_search) == []

    def test_get_books_for_children_does_not_contain_horror_detective(self, collector_with_test_data):
        books_for_children = collector_with_test_data.get_books_for_children()
        genres = []
        for book in books_for_children:
            genres.append(collector_with_test_data.books_genre.get(book))

        assert "Ужасы" and "Детектив" not in genres

    def test_get_books_for_children_book_genre_contain_only_horror_and_detective_empty_list(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Оно": "Ужасы",
            "Сияние": "Ужасы",
            "Шерлок Холмс": "Детектив"
        }
        books_for_children = collector.get_books_for_children()

        assert books_for_children == []

    def test_add_book_in_favorites_added_two_books(self, collector_with_test_data):
        collector_with_test_data.add_book_in_favorites("Шерлок Холмс")
        collector_with_test_data.add_book_in_favorites("Дюна")
        assert len(collector_with_test_data.favorites) == 2

    def test_add_book_in_favorites_book_already_in_favorites_not_added(self, collector_with_test_data):
        collector_with_test_data.add_book_in_favorites("Шерлок Холмс")
        collector_with_test_data.add_book_in_favorites("Дюна")
        collector_with_test_data.add_book_in_favorites("Шерлок Холмс")
        assert len(collector_with_test_data.favorites) == 2

    def test_add_book_in_favorites_book_not_in_books_genre_not_added(self, collector_with_test_data):
        collector_with_test_data.add_book_in_favorites("Гордость и предубеждение")
        assert len(collector_with_test_data.favorites) == 0

    def test_delete_book_from_favorites_deleted(self):
        collector = BooksCollector()
        collector.favorites = ["Шерлок Холмс", "Дюна"]

        book_to_delete = "Дюна"

        collector.delete_book_from_favorites(book_to_delete)
        assert book_to_delete not in collector.favorites

    def test_delete_book_from_favorites_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.favorites = ["Шерлок Холмс", "Дюна"]

        book_to_delete = "Гордость и предубеждение"

        collector.delete_book_from_favorites(book_to_delete)
        assert collector.favorites == ["Шерлок Холмс", "Дюна"]

    def test_get_list_of_favorites_books_not_empty(self):
        collector = BooksCollector()
        collector.favorites = ["Шерлок Холмс", "Дюна"]
        assert collector.get_list_of_favorites_books() == ["Шерлок Холмс", "Дюна"]
