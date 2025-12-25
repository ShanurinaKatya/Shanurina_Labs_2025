from operator import itemgetter
import unittest
from main import (
    SyntaxConstruct,
    ProgrammingLanguage,
    ConstructLanguage,
    LanguageDataProcessor,
    create_test_data
)


class TestLanguageDataProcessor(unittest.TestCase):
    """Тесты для класса LanguageDataProcessor"""

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.langs, self.constructs, self.constructs_langs = create_test_data()
        self.processor = LanguageDataProcessor(
            self.langs,
            self.constructs,
            self.constructs_langs
        )

    def test_task_a1_structure_and_sorting(self):
        """Тест структуры и сортировки задания A1"""
        result = self.processor.task_a1()

        # Проверяем, что результат не пустой
        self.assertGreater(len(result), 0, "Результат задания A1 пуст")

        # Проверяем структуру каждой записи
        for item in result:
            self.assertEqual(len(item), 3, f"Неверная структура записи: {item}")
            self.assertIsInstance(item[0], str, f"Название конструкции должно быть строкой: {item[0]}")
            self.assertIsInstance(item[1], int, f"Сложность должна быть числом: {item[1]}")
            self.assertIsInstance(item[2], str, f"Название языка должно быть строкой: {item[2]}")

        # Проверяем сортировку по названию языка
        language_names = [item[2] for item in result]
        sorted_language_names = sorted(language_names)
        self.assertEqual(language_names, sorted_language_names,
                        "Результат не отсортирован по языкам")

    def test_task_a2_calculation_and_sorting(self):
        """Тест расчетов и сортировки задания A2"""
        result = self.processor.task_a2()

        # Проверяем, что результат не пустой
        self.assertGreater(len(result), 0, "Результат задания A2 пуст")

        # Проверяем структуру каждой записи
        for item in result:
            self.assertEqual(len(item), 2, f"Неверная структура записи: {item}")
            self.assertIsInstance(item[0], str, f"Название языка должно быть строкой: {item[0]}")
            self.assertIsInstance(item[1], int, f"Суммарная сложность должна быть числом: {item[1]}")

        # Проверяем правильность расчетов
        one_to_many = self.processor.get_one_to_many()
        for lang_name, total_complexity in result:
            # Находим все конструкции для данного языка
            lang_constructs = [item for item in one_to_many if item[2] == lang_name]

            # Вычисляем суммарную сложность
            calculated_sum = sum(item[1] for item in lang_constructs)

            # Проверяем совпадение
            self.assertEqual(total_complexity, calculated_sum,
                            f"Неверный расчет для языка {lang_name}: "
                            f"ожидалось {calculated_sum}, получено {total_complexity}")

        # Проверяем сортировку по убыванию сложности
        complexities = [item[1] for item in result]
        for i in range(len(complexities) - 1):
            self.assertGreaterEqual(complexities[i], complexities[i + 1],
                                   "Результат не отсортирован по убыванию сложности")

    def test_task_a3_filtering(self):
        """Тест фильтрации задания A3"""
        result = self.processor.task_a3()

        # Проверяем структуру каждой записи
        for item in result:
            self.assertEqual(len(item), 2, f"Неверная структура записи: {item}")
            lang_name, construct_name = item

            # Проверяем, что название языка содержит "Java"
            self.assertIn('Java', lang_name,
                         f"Язык {lang_name} не содержит 'Java'")

            self.assertIsInstance(lang_name, str, "Название языка должно быть строкой")
            self.assertIsInstance(construct_name, str, "Название конструкции должно быть строкой")

        # Проверяем, что для каждого языка с "Java" есть конструкции
        java_languages = [lang for lang in self.langs if 'Java' in lang.name]
        for java_lang in java_languages:
            # Ищем конструкции для этого языка в результате
            lang_constructs = [item[1] for item in result if item[0] == java_lang.name]
            self.assertGreater(len(lang_constructs), 0,
                              f"Для языка {java_lang.name} не найдено конструкций")

    def test_one_to_many_relationship_integrity(self):
        """Тест целостности связи один-ко-многим"""
        one_to_many = self.processor.get_one_to_many()

        for construct_name, complexity, lang_name in one_to_many:
            # Находим соответствующий язык
            lang = next((l for l in self.langs if l.name == lang_name), None)
            self.assertIsNotNone(lang, f"Язык {lang_name} не найден")

            # Находим соответствующую конструкцию
            construct = next((c for c in self.constructs
                             if c.name == construct_name and c.complexity == complexity), None)
            self.assertIsNotNone(construct, f"Конструкция {construct_name} не найдена")

            # Проверяем связь
            self.assertEqual(construct.lang_id, lang.id,
                            f"Несоответствие связи: конструкция {construct_name} "
                            f"должна принадлежать языку {lang_name}")

    def test_many_to_many_relationship_integrity(self):
        """Тест целостности связи многие-ко-многим"""
        many_to_many = self.processor.get_many_to_many()

        for construct_name, complexity, lang_name in many_to_many:
            # Находим соответствующий язык
            lang = next((l for l in self.langs if l.name == lang_name), None)
            self.assertIsNotNone(lang, f"Язык {lang_name} не найден")

            # Находим соответствующую конструкцию
            construct = next((c for c in self.constructs
                             if c.name == construct_name and c.complexity == complexity), None)
            self.assertIsNotNone(construct, f"Конструкция {construct_name} не найдена")

            # Проверяем связь в таблице constructs_langs
            connection = next((cl for cl in self.constructs_langs
                              if cl.lang_id == lang.id and cl.construct_id == construct.id), None)
            self.assertIsNotNone(connection,
                                f"Отсутствует связь между языком {lang_name} "
                                f"и конструкцией {construct_name}")


class TestDataClasses(unittest.TestCase):
    """Тесты для классов данных"""

    def test_syntax_construct_creation(self):
        """Тест создания объекта SyntaxConstruct"""
        construct = SyntaxConstruct(1, 'Lambda expression', 6, 2)

        self.assertEqual(construct.id, 1)
        self.assertEqual(construct.name, 'Lambda expression')
        self.assertEqual(construct.complexity, 6)
        self.assertEqual(construct.lang_id, 2)

        # Проверяем граничные значения сложности
        construct_low = SyntaxConstruct(2, 'Simple construct', 1, 1)
        construct_high = SyntaxConstruct(3, 'Complex construct', 10, 1)

        self.assertEqual(construct_low.complexity, 1)
        self.assertEqual(construct_high.complexity, 10)

    def test_programming_language_creation(self):
        """Тест создания объекта ProgrammingLanguage"""
        language = ProgrammingLanguage(1, 'Python')

        self.assertEqual(language.id, 1)
        self.assertEqual(language.name, 'Python')

        # Проверяем создание языка с пробелами в названии
        language_with_spaces = ProgrammingLanguage(2, 'C Sharp')
        self.assertEqual(language_with_spaces.name, 'C Sharp')

    def test_construct_language_creation(self):
        """Тест создания объекта ConstructLanguage"""
        connection = ConstructLanguage(1, 2)

        self.assertEqual(connection.lang_id, 1)
        self.assertEqual(connection.construct_id, 2)

        # Проверяем обратную связь
        reverse_connection = ConstructLanguage(2, 1)
        self.assertEqual(reverse_connection.lang_id, 2)
        self.assertEqual(reverse_connection.construct_id, 1)


class TestHelperMethods(unittest.TestCase):
    """Тесты вспомогательных методов"""

    def setUp(self):
        """Подготовка тестовых данных"""
        self.langs, self.constructs, self.constructs_langs = create_test_data()
        self.processor = LanguageDataProcessor(
            self.langs,
            self.constructs,
            self.constructs_langs
        )

    def test_get_language_by_name(self):
        """Тест метода get_language_by_name"""
        # Существующий язык
        python_lang = self.processor.get_language_by_name('Python')
        self.assertIsNotNone(python_lang)
        self.assertEqual(python_lang.name, 'Python')
        self.assertEqual(python_lang.id, 1)

        # Несуществующий язык
        nonexistent_lang = self.processor.get_language_by_name('Ruby')
        self.assertIsNone(nonexistent_lang)

    def test_get_construct_by_name(self):
        """Тест метода get_construct_by_name"""
        # Существующая конструкция
        lambda_construct = self.processor.get_construct_by_name('Lambda expression')
        self.assertIsNotNone(lambda_construct)
        self.assertEqual(lambda_construct.name, 'Lambda expression')
        self.assertEqual(lambda_construct.complexity, 6)

        # Несуществующая конструкция
        nonexistent_construct = self.processor.get_construct_by_name('Magic function')
        self.assertIsNone(nonexistent_construct)


def run_all_tests():
    """Запуск всех тестов с подробным выводом"""
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Добавляем тестовые классы
    suite.addTests(loader.loadTestsFromTestCase(TestLanguageDataProcessor))
    suite.addTests(loader.loadTestsFromTestCase(TestDataClasses))
    suite.addTests(loader.loadTestsFromTestCase(TestHelperMethods))

    # Запускаем тесты с подробным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == '__main__':
    # Запуск тестов при прямом вызове файла
    run_all_tests()
