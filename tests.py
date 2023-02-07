from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Test_1-Проверка books_rating в конструкторе класса
    def test_init_empty_dict(self, new_collector):
        assert new_collector.books_rating == {}
    # Test_2-Проверка favorites в конструкторе класса
    def test_init_empty_list(self,new_collector):
        assert new_collector.favorites== []

    # Test_3-Проверка добавление книги
    def test_add_new_book(self, new_collector):
        new_collector.add_new_book('Властелин колец')
        assert 'Властелин колец' in new_collector.get_books_rating()

    # Test_4- Проверка невозможности добавления одной и тойже книги дважды
    def test_cant_add_same_book_twice(self, new_collector):
        new_collector.add_new_book('Преступление и наказание')
        new_collector.add_new_book('Преступление и наказание')
        assert len(new_collector.get_books_rating()) == 1

    # Test_5- Проверка невозможности  выставления рейтинга меньше 1
    def test_cant_create_raiting_less_one(self,new_collector):
        new_collector.add_new_book('Задача трех тел')
        new_collector.set_book_rating('Задача трех тел',0)
        assert new_collector.get_book_rating('Задача трех тел')==1

    # Test_6- Проверка невозможности  выставления рейтинга больше 10
    def test_cant_create_rating_more_ten(self,new_collector):
        new_collector.add_new_book('Задача трех тел')
        new_collector.set_book_rating('Задача трех тел',11)
        assert new_collector.get_book_rating('Задача трех тел')==1

    # Test_7 - Проверка отсутсвия возможности высталения рейтинга книге которой нет в списке
    def test_cant_add_rating_epmty_book(self,new_collector):
        new_collector.set_book_rating('Убейте Дракона',9)
        assert new_collector.get_book_rating('Убейте Дракона') is None


    # Test_8 - У не добавленной книги нет рейтинга
    def test_check_rating_empty_book(self,new_collector):
        assert new_collector.get_book_rating('Проектирование виртуальных миров') is None










