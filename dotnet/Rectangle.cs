namespace Figures
{
    class Rectangle : Figure, IPrint
    {
        private double width = 0;
        public double Width
        {
            get { return this.width; }
            set { width = value; }
        }
        private double height = 0;
        public double Height
        {
            get { return this.height; }
            set { this.height = value; }
        }

        public Rectangle(double w = 0, double h = 0)
        {
            this.width = w;
            this.height = h;
            this.Type = "Rectangle";
        }
        public override double Area()
        {
            double result = this.width * this.height;
            return result;
        }

        public override string ToString()
        {
            return $"{Type}: w = {this.width}; h = {this.height}; area: {Math.Round(this.Area(), 2)}";
        }
        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }
} // namespace Figures
