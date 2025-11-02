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
        }

        public override double Area()
        {
            return Math.PI * this.radius * this.radius;
        }

        public override string ToString()
        {
            return $"r = {this.radius}; area: {Math.Round(this.Area(), 2)}";
        }
        public void Print()
        {
            Console.WriteLine($"Круг: {this.ToString()}");
        }
    }
}
