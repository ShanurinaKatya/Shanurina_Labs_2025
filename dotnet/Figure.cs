using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Runtime.CompilerServices;

namespace Figures
{
    abstract class Figure : IComparable, IComparable<Figure>
    {
        public string Type
        {
            get { return this.type; }
            protected set { this.type = value; }
        }
        string type = "";
        public abstract double Area();

        public int CompareTo(object? obj)
        {
            Figure other = (Figure)obj!;
            if (this.Area() < other.Area()) return -1;
            else if (this.Area() == other.Area()) return 0;
            else return 1;
        }

        public int CompareTo(Figure? obj)
        {
            Figure other = (Figure)obj!;
            if (this.Area() < other.Area()) return -1;
            else if (this.Area() == other.Area()) return 0;
            else return 1;
        }
    }
} // Figures
