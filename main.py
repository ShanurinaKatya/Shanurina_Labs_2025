from operator import itemgetter


class SyntaxConstruct:
    """Синтаксическая конструкция"""
    def __init__(self, id, name, complexity, lang_id):
        self.id = id
        self.name = name
        self.complexity = complexity  # сложность использования (1-10)
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


# Языки программирования
langs = [
    ProgrammingLanguage(1, 'Python'),
    ProgrammingLanguage(2, 'JavaScript'),
    ProgrammingLanguage(3, 'C++'),
    ProgrammingLanguage(11, 'Java'),
    ProgrammingLanguage(22, 'Go'),
]

# Синтаксические конструкции
constructs = [
    SyntaxConstruct(1, 'List comprehension', 7, 1),
    SyntaxConstruct(2, 'Arrow function', 5, 2),
    SyntaxConstruct(3, 'Template', 8, 3),
    SyntaxConstruct(4, 'Lambda expression', 6, 2),
    SyntaxConstruct(5, 'Decorator', 9, 1),
]

# Связь многие-ко-многим
constructs_langs = [
    ConstructLanguage(1, 1),
    ConstructLanguage(2, 2),
    ConstructLanguage(3, 3),
    ConstructLanguage(2, 4),
    ConstructLanguage(1, 5),
    ConstructLanguage(11, 4),
    ConstructLanguage(22, 2),
]


def main():
    # Запрос 1: Список всех связанных синтаксических конструкций и языков,
    # отсортированный по языкам
    one_to_many = [(c.name, c.complexity, l.name)
                   for l in langs
                   for c in constructs
                   if c.lang_id == l.id]

    print('Задание А1: Список конструкций и языков, отсортированный по языкам')
    res_a1 = sorted(one_to_many, key=itemgetter(2))
    print(res_a1)

    # Запрос 2: Список языков с суммарной сложностью конструкций,
    # отсортированный по суммарной сложности
    print('\nЗадание А2: Языки с суммарной сложностью конструкций')
    res_a2_unsorted = []

    for l in langs:
        # Конструкции данного языка
        l_constructs = list(filter(lambda i: i[2] == l.name, one_to_many))

        if len(l_constructs) > 0:
            # Сложности конструкций данного языка
            l_complexities = [complexity for _, complexity, _ in l_constructs]
            # Суммарная сложность
            l_complexities_sum = sum(l_complexities)
            res_a2_unsorted.append((l.name, l_complexities_sum))

    res_a2 = sorted(res_a2_unsorted, key=itemgetter(1), reverse=True)
    print(res_a2)

    # Запрос 3: Список всех языков, у которых в названии есть слово "Java",
    # и список используемых в них конструкций
    print('\nЗадание А3: Языки со словом "Java" и их конструкции')

    # Сначала создаем связь многие-ко-многим
    many_to_many_temp = [(l.name, cl.lang_id, cl.construct_id)
                         for l in langs
                         for cl in constructs_langs
                         if l.id == cl.lang_id]

    many_to_many = [(c.name, c.complexity, lang_name)
                    for lang_name, lang_id, construct_id in many_to_many_temp
                    for c in constructs
                    if c.id == construct_id]

    res_a3 = {}
    for l in langs:
        if 'Java' in l.name:
            # Конструкции данного языка
            l_constructs = list(filter(lambda i: i[2] == l.name, many_to_many))
            # Имена конструкций
            l_constructs_names = [x for x, _, _ in l_constructs]
            res_a3[l.name] = l_constructs_names

    print(res_a3)


if __name__ == '__main__':
    main()
