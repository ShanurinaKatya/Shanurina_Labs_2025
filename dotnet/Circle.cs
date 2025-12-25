namespace Figures
{
    class Circle : Figure, IPrint
    {
        private double radius = 0;
        public double Radius
        {
            get { return this.radius; }
            set { this.radius = value; }
        }

        public Circle(double r = 0)
        {
            this.radius = r;
            this.Type = "Circle";
        }

        public override double Area()
        {
            double result = Math.PI * this.radius * this.radius;
            return result;
        }

        public override string ToString()
        {
            return $"{Type}: r = {this.radius}; area: {Math.Round(this.Area(), 2)}";
        }
        public void Print()
        {
            Console.WriteLine($"{Type}: {this.ToString()}");
        }
    };
}
