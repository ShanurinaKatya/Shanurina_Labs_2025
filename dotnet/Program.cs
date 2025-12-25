using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics.Contracts;

namespace Figures
{
    class Program
    {
        static void Main(string[] argv)
        {
            //------- Создание объектов геометрических фигур
            Circle circle1 = new Circle(3);
            Circle circle2 = new Circle(92);
            Rectangle rect = new Rectangle(20, 10);
            Square square = new Square(54);

            //------ Коллекция ArrayList из фигур
            ArrayList al = new ArrayList();

            al.Add(circle1);
            al.Add(circle2);
            al.Add(square);
            al.Add(rect);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("ArrayList");
            Console.ForegroundColor = ConsoleColor.White;
            foreach (var x in al) Console.WriteLine(x);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\nОтсортированный список ArrayList:");
            Console.ForegroundColor = ConsoleColor.White;
            al.Sort();
            foreach (var x in al) { Console.WriteLine(x); }

            //------- Создание коллекции List из геометрических фигур
            List<Figure> list = new List<Figure>();
            list.Add(circle1);
            list.Add(circle2);
            list.Add(rect);
            list.Add(square);

            //------ Сортировка и вывод на экран
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\nList<Figures>");
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("Отсортированная коллекция List фигур");
            list.Sort();
            foreach (var x in list) Console.WriteLine(x);

            //------- Создание своей коллекции фигур
            SimpleList<Figure> figures = new SimpleList<Figure>();
            figures.Push(circle1);
            figures.Push(circle2);
            figures.Push(rect);
            figures.Push(square);

            //------ Сортировка коллекции и вывод на экран
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\nSimpleList<Figure>");
            Console.ForegroundColor = ConsoleColor.White;
            figures.Sort();
            foreach (var x in figures) Console.WriteLine(x);
        }
    }
} // Figures
