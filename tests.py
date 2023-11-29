import pytest
from test_data import dict_books


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', [' ', '~', 'A', 'Lorem ipsum dolor sit amet, consectetur!'])
    def test_add_new_book_length_no_more_40_successful_creation(self, book_name, collector):
        collector.add_new_book(name=book_name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_length_more_40(self, collector):
        collector.add_new_book('Как управлять Вселенной, не привлекая внимания санитаров')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_exist_book(self, collector):
        collector.add_new_book(name='Дом у озера')
        collector.add_new_book(name='Дом у озера')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name, book_genre', [('Слон', 'Ужасы')])
    def test_set_book_genre_set_genre_successfull(self, book_name, book_genre, collector):
        collector.add_new_book(name=book_name)
        collector.set_book_genre(name=book_name, genre=book_genre)
        assert (collector.get_books_genre()[book_name]) == book_genre

    @pytest.mark.parametrize('book_name, book_genre', [('Тверская улица', 'Хоррор'), ('Полет на луну', 'Мультфильмы'),
        ('Пустошь', 'Вестерн')])
    def test_set_book_genre_set_genre_fail(self, collector, book_name, book_genre):
        collector.add_new_book(name='Дом у озера')
        collector.set_book_genre(name=book_name, genre=book_genre)
        assert len(collector.get_books_genre()) == 1 and (collector.get_books_genre()['Дом у озера']) == ''

    @pytest.mark.parametrize('book_name, book_genre', [('Star Trek', 'Фантастика')])
    def test_get_book_genre_by_book_name_successfull(self, collector, book_name, book_genre):
        collector.add_new_book(name=book_name)
        collector.set_book_genre(name=book_name, genre=book_genre)
        assert collector.get_book_genre(name=book_name) == book_genre

    def test_get_books_with_specific_genre_return_two_books(self, collector):
        for db_name, db_genre in dict_books.items():
            collector.add_new_book(name=db_name)
            collector.set_book_genre(name=db_name, genre=db_genre)
        assert sorted(collector.get_books_with_specific_genre('Мультфильмы')) == sorted(['Незнайка на луне', 'Лунтик'])

    def test_get_books_genre_return_all_values(self, collector):
        for db_name, db_genre in dict_books.items():
            collector.add_new_book(name=db_name)
            collector.set_book_genre(name=db_name, genre=db_genre)
        assert collector.get_books_genre() == dict_books

    def test_get_books_for_children_three_children_books(self, collector):
        for db_name, db_genre in dict_books.items():
            collector.add_new_book(name=db_name)
            collector.set_book_genre(name=db_name, genre=db_genre)
        assert sorted(collector.get_books_for_children()) == sorted(
            ['Доллар по 32', 'Незнайка на луне', 'Лунтик', 'Женитьба Бальзаминова'])

    def test_add_book_in_favorites_add_three_books(self, collector):
        for db_name, db_genre in dict_books.items():
            collector.add_new_book(name=db_name)
            collector.set_book_genre(name=db_name, genre=db_genre)
        collector.add_book_in_favorites('Загадай число')
        collector.add_book_in_favorites('Лунтик')
        collector.add_book_in_favorites('Женитьба Бальзаминова')
        assert sorted(collector.get_list_of_favorites_books()) == sorted(
            ['Загадай число', 'Лунтик', 'Женитьба Бальзаминова'])

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        for db_name, db_genre in dict_books.items():
            collector.add_new_book(name=db_name)
            collector.set_book_genre(name=db_name, genre=db_genre)
        collector.add_book_in_favorites('Загадай число')
        collector.add_book_in_favorites('Лунтик')
        collector.delete_book_from_favorites('Лунтик')
        assert collector.get_list_of_favorites_books() == ['Загадай число']

    def test_get_list_of_favorites_books_show_two_favorite_books(self, collector):
        for db_name, db_genre in dict_books.items():
            collector.add_new_book(name=db_name)
            collector.set_book_genre(name=db_name, genre=db_genre)
        collector.add_book_in_favorites('Тихое место')
        collector.add_book_in_favorites('Доллар по 32')
        assert sorted(collector.get_list_of_favorites_books()) == sorted(['Тихое место', 'Доллар по 32'])

