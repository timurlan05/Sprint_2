import pytest
from main import BooksCollector

class TestBooksCollector:
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book(self, collector):
        collector.add_new_book("Book 1")
        assert collector.books_rating == {"Book 1": 1}

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 1")
        assert collector.books_rating == {"Book 1": 1}

    def test_set_book_rating(self, collector):
        collector.add_new_book("Book 1")
        collector.set_book_rating("Book 1", 5)
        assert collector.books_rating == {"Book 1": 5}

    def test_set_book_rating_invalid_rating(self, collector):
        collector.add_new_book("Book 1")
        collector.set_book_rating("Book 1", 15)
        assert collector.books_rating == {"Book 1": 1}

    def test_get_book_rating(self, collector):
        collector.add_new_book("Book 1")
        collector.set_book_rating("Book 1", 5)
        assert collector.get_book_rating("Book 1") == 5

    def test_get_books_with_specific_rating(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.add_new_book("Book 3")
        collector.set_book_rating("Book 1", 5)
        collector.set_book_rating("Book 2", 3)
        collector.set_book_rating("Book 3", 5)
        assert collector.get_books_with_specific_rating(5) == ["Book 1", "Book 3"]

    def test_get_books_rating(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.add_new_book("Book 3")
        collector.set_book_rating("Book 1", 5)
        collector.set_book_rating("Book 2", 3)
        collector.set_book_rating("Book 3", 5)
        assert collector.get_books_rating() == {"Book 1": 5, "Book 2": 3, "Book 3": 5}

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        assert collector.favorites == ["Book 1"]

    def test_add_book_in_favorites_invalid_book(self, collector):
        collector.add_book_in_favorites("Book 1")
        assert collector.favorites == []

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.delete_book_from_favorites("Book 1")
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.add_book_in_favorites("Book 1")
        collector.add_book_in_favorites("Book 2")
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["Book 1", "Book 2"]
