
Unit тесты для класса BookCollector

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

_ _init_ _

`test_books_collector_init_data` - проверяет значение атрибутов класса при инициализации

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

*add_new_book*

`test_add_new_book_add_two_books` - добавляется две книги и проверяется, что книг в коллекции действительно 2.

`test_add_new_book_if_book_in_book_genre_not_added` - проверяется, что книга не добавляется, если такое название уже есть в коллекции.

`test_add_new_book_book_name_length_validation_negative` - проверяются граничные значения: книга не добавляется, если длина названия 0, 41. 

`test_add_new_book_book_name_length_validation_positive` - проверяются граничные значения: книга добавляется, если длина названия 1, 40.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

*set_book_genre*

`test_set_book_genre_when_it_was_empty_or_change_value_positive`

Тест проверяет добавление жанра:
1) значение не было установлено до этого (пустая строка)
2) значение было установлено, в результате добавления значение меняется
3) значение было установлено, в результате добавления значение не меняется

`test_set_book_genre_if_book_not_in_collection_return_none`  - проверяется, что при попытке добавить жанр книге, не находящейся в коллекции books_genre, книга не добавляется в коллекцию.

`test_set_book_genre_if_genre_not_in_collection_return_empty_str` - проверяется, что при попытке установить книге жанр, не находящийся в коллекции genre, значение жанра книги в коллекции books_genre не меняется. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
*get_books_genre*

`test_get_books_genre_not_empty_returns_collection` - проверяет, что метод возвращает ожидаемую коллекцию.

`test_get_books_genre_empty_returns_empty_dict` - проверяет, что если коллекция пустая, метод возвращает пустой словарь.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

*get_book_genre*
 
 `test_get_book_genre_return_detective` - проверяется, что метод возвращает значение жанра, соответствующее книге в коллекции books_genre (В данном случае "Детектив" для "Шерлок Холмс")
 
 `test_get_book_genre_empty_books_genre_return_none` - проверяется, что метод возвращает None, при обращении к пустой коллекции books_genre.

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------

 *get_books_with_specific_genre*
 
 `test_get_books_with_specific_genre_return_three_books` - проверяется, что возвращается заданное количество книг с запрашиваемым жанром
 
 `test_get_books_with_specific_genre_if_genre_not_in_books_genre_return_empty_list` - првоеряется, что метод возвращает пустой список, если книг с запрашиваемым жанром в коллекции нет

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------

 *get_books_for_children*
 
 `test_get_books_for_children_does_not_contain_horror_detective` - проверяется, что метод возвращает список книг, среди кторых нет ужасов и детективов
 
 `test_get_books_for_children_book_genre_contain_only_horror_and_detective_empty_list` - проверяется, что метод возвращает пустой список, если в коллекции только ужасы и детективы

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 *add_book_in_favorites*
 
 `test_add_book_in_favorites_added_two_books` - проверяется, что добавлены две книги в коллекцию favorites
 
 `test_add_book_in_favorites_book_already_in_favorites_not_added` - проверяется, что книга не добавляется, если название уже есть в коллекции favorites
 
`test_add_book_in_favorites_book_not_in_books_genre_not_added` - проверяется, что книга не добавляется, если книга отсутствует в коллекции books_genre

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 *delete_book_from_favorites*
 
 `test_delete_book_from_favorites_deleted` - проверяется, что метод удаляет книгу из коллекции favorites
 
 `test_delete_book_from_favorites_book_not_in_favorites` - проверяется, что при удалении из коллекции favorites отсутствуюшей книги, не возникает ошибок, сама коллекция остается без изменений.

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 *get_list_of_favorites_books*
 
 `test_get_list_of_favorites_books_not_empty` - проверяется, что метод возвращает коллекцию favorites

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
