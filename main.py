
from operator import itemgetter


class SyntaxConstruct:
    """Синтаксическая конструкция"""
    def __init__(self, id, name, complexity, lang_id):
        self.id = id
        self.name = name
        self.complexity = complexity
        self.lang_id = lang_id


class ProgrammingLanguage:
    """Язык программирования"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ConstructLanguage:
    """Синтаксические конструкции языков программирования (для связи многие-ко-многим)"""
    def __init__(self, lang_id, construct_id):
        self.lang_id = lang_id
        self.construct_id = construct_id


class LanguageDataProcessor:
    """Класс для обработки данных о языках программирования и синтаксических конструкциях"""

    def __init__(self, langs, constructs, constructs_langs):
        self.langs = langs
        self.constructs = constructs
        self.constructs_langs = constructs_langs

    def get_one_to_many(self):
        """Получение связи один-ко-многим (язык → конструкции)"""
        return [(c.name, c.complexity, l.name)
                for l in self.langs
                for c in self.constructs
                if c.lang_id == l.id]

    def get_many_to_many(self):
        """Получение связи многие-ко-многим"""

        many_to_many_temp = [(l.name, cl.lang_id, cl.construct_id)
                             for l in self.langs
                             for cl in self.constructs_langs
                             if l.id == cl.lang_id]


        return [(c.name, c.complexity, lang_name)
                for lang_name, lang_id, construct_id in many_to_many_temp
                for c in self.constructs
                if c.id == construct_id]

    def task_a1(self):
        """Задание A1: Список всех связанных конструкций и языков, отсортированный по языкам"""
        one_to_many = self.get_one_to_many()
        return sorted(one_to_many, key=itemgetter(2))

    def task_a2(self):
        """Задание A2: Список языков с суммарной сложностью конструкций, отсортированный по сложности"""
        one_to_many = self.get_one_to_many()
        result = []

        for lang in self.langs:

            lang_constructs = list(filter(lambda item: item[2] == lang.name, one_to_many))

            if len(lang_constructs) > 0:

                complexities = [complexity for _, complexity, _ in lang_constructs]

                total_complexity = sum(complexities)
                result.append((lang.name, total_complexity))


        return sorted(result, key=itemgetter(1), reverse=True)

    def task_a3(self):
        """Задание A3: Языки со словом 'Java' и их конструкции"""
        many_to_many = self.get_many_to_many()
        result = []

        for lang in self.langs:
            if 'Java' in lang.name:

                lang_constructs = list(filter(lambda item: item[2] == lang.name, many_to_many))

                construct_names = [name for name, _, _ in lang_constructs]

                for construct_name in construct_names:
                    result.append((lang.name, construct_name))

        return result

    def get_language_by_name(self, name):
        """Получить язык программирования по имени"""
        for lang in self.langs:
            if lang.name == name:
                return lang
        return None

    def get_construct_by_name(self, name):
        """Получить синтаксическую конструкцию по имени"""
        for construct in self.constructs:
            if construct.name == name:
                return construct
        return None


def create_test_data():
    """Создание тестовых данных"""

    langs = [
        ProgrammingLanguage(1, 'Python'),
        ProgrammingLanguage(2, 'JavaScript'),
        ProgrammingLanguage(3, 'C++'),
        ProgrammingLanguage(11, 'Java'),
        ProgrammingLanguage(22, 'Go'),
    ]


    constructs = [
        SyntaxConstruct(1, 'List comprehension', 7, 1),
        SyntaxConstruct(2, 'Arrow function', 5, 2),
        SyntaxConstruct(3, 'Template', 8, 3),
        SyntaxConstruct(4, 'Lambda expression', 6, 2),
        SyntaxConstruct(5, 'Decorator', 9, 1),
    ]


    constructs_langs = [
        ConstructLanguage(1, 1),
        ConstructLanguage(2, 2),
        ConstructLanguage(3, 3),
        ConstructLanguage(2, 4),
        ConstructLanguage(1, 5),
        ConstructLanguage(11, 4),
        ConstructLanguage(22, 2),
    ]

    return langs, constructs, constructs_langs


def print_table(headers, data):
    """Функция для форматированного вывода таблицы"""
    if not data:
        print("Нет данных для отображения")
        return


    col_widths = []
    for i in range(len(headers)):
        max_len = len(headers[i])
        for row in data:
            cell_len = len(str(row[i]))
            if cell_len > max_len:
                max_len = cell_len
        col_widths.append(max_len)


    header_str = "  ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    print(header_str)


    separator = "  ".join("-" * col_widths[i] for i in range(len(headers)))
    print(separator)


    for row in data:
        row_str = "  ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row)))
        print(row_str)

    print()


def main():
    """Основная функция программы"""

    langs, constructs, constructs_langs = create_test_data()


    processor = LanguageDataProcessor(langs, constructs, constructs_langs)

    print('=' * 60)
    print('РУБЕЖНЫЙ КОНТРОЛЬ №1')
    print('Предметная область: Синтаксическая конструкция - Язык программирования')
    print('=' * 60)
    print()


    print('Задание А1:')
    print('Список всех связанных конструкций и языков, отсортированный по языкам')
    result_a1 = processor.task_a1()
    print_table(['Конструкция', 'Сложность', 'Язык'], result_a1)


    print('Задание А2:')
    print('Языки с суммарной сложностью конструкций (сортировка по убыванию)')
    result_a2 = processor.task_a2()
    print_table(['Язык', 'Суммарная сложность'], result_a2)

    # Выполнение задания A3
    print('Задание А3:')
    print('Языки со словом "Java" и их конструкции')
    result_a3 = processor.task_a3()
    print_table(['Язык', 'Конструкция'], result_a3)

    print('=' * 60)
    print('ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ')
    print('=' * 60)


if __name__ == '__main__':
    main()
