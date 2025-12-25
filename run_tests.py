"""
Демонстрационный файл для запуска модульных тестов
"""
import unittest
from test_main import run_all_tests


def main():
    """Основная функция запуска тестов"""
    print("=" * 70)
    print("РУБЕЖНЫЙ КОНТРОЛЬ №2 - МОДУЛЬНОЕ ТЕСТИРОВАНИЕ")
    print("Предметная область: Синтаксическая конструкция - Язык программирования")
    print("=" * 70)
    print()

    print("ЗАПУСК ТЕСТОВ...")
    print()

    # Запуск всех тестов
    test_result = run_all_tests()

    print()
    print("=" * 70)
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print("-" * 70)
    print(f"Всего тестов выполнено: {test_result.testsRun}")

    if test_result.failures:
        print(f"ПРОВАЛЕНО тестов: {len(test_result.failures)}")
        for test, traceback in test_result.failures:
            print(f"  - {test}")
    else:
        print("ПРОВАЛЕНО тестов: 0")

    if test_result.errors:
        print(f"ОШИБОК при выполнении: {len(test_result.errors)}")
        for test, traceback in test_result.errors:
            print(f"  - {test}")
    else:
        print("ОШИБОК при выполнении: 0")

    success_count = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    success_rate = (success_count / test_result.testsRun * 100) if test_result.testsRun > 0 else 0

    print(f"УСПЕШНО пройдено: {success_count} ({success_rate:.1f}%)")
    print("=" * 70)


if __name__ == '__main__':
    main()
