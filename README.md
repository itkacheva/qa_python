# qa_python
<h1 align="center">Описание тестовых методов для класса BooksCollector</a></h1>


<b style="color:green"> test_add_new_book_add_two_books()</b> - проверяет добавление двух разных книг в словарь books_genre

<p><b style="color:green">test_add_new_book_length_no_more_40_successful_creation()</b> - проверяет  добаление книг в словарь  books_genre с разными названиями, длина которых < = 40 символам</p>

<p><b style="color:green">test_add_new_book_length_more_40()</b> - проверяет добаление книги в словарь  books_genre с названием, длина которого превышает 40 символов</p>

<p><b style="color:green">test_add_new_book_add_exist_book()</b> - проверяет добаление уже сущетвующей книги в словарь  books_genre (повторное добавление одной и той же книги)</p>

<p><b style="color:green">test_set_book_genre_set_genre_successfull()</b> - проверяет  устанавку существующего жанра в genre для существующей в словаре books_genre книги</p>

<p><b style="color:green">test_set_book_genre_set_genre_fail()</b> - проверяет  устанавку жанра, при несоблюдении условия:  (жанр для книги устанавливается только втом случа, если книга есть в books_genre и её жанр входит в список genre.)
										проверят следующие случаи:
										<ul><p><li>книга есть в books_genre, ее жанр НЕ входит в список genre</li></p>
										<p><li>книги НЕТ в books_genre, ее жанр входит в список genre</li>
										<p><li>книги НЕТ в books_genre, ее жанр НЕ входит в список genre</li></p></ul>

<p><b style="color:green">test_get_book_genre_by_book_name_successfull()</b> - проверяет вывод жанра книги по её имени</p>

<p><b style="color:green">test_get_books_with_specific_genre_return_two_books()</b> - проверяет, что система выводит две книги из заданного списка книг с определённым жанром (в данном сучае 'Мультфильмы')</p>

<p><b style="color:green">test_get_books_genre_return_all_values()</b> - проверяет, что метод возвращает заданный ранее словарь значений (словарь books_genre)</p>

<p><b style="color:green">test_get_books_for_children_three_children_books()</b> - проверяет, что метод возвращает только книги с тремя допустимыми рейтингами для детей</p>

<p><b style="color:green">test_add_book_in_favorites_add_three_books()</b> - проверяет добавление трех книг в список избранных</p>

<p><b style="color:green">test_get_list_of_favorites_books_show_two_favorite_books(</b>) - проверяет вывод списка избранных книг, состоящий из двух книг</p>





