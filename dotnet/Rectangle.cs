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

        public Rectangle(int w = 0, int h = 0)
        {
            this.width = w;
            this.height = h;
        }
        public override double Area()
        {
            return this.width * this.height;
            throw new NotImplementedException();
        }

        public override string ToString()
        {
            return $"w = {this.width}; h = {this.height}; area: {Math.Round(this.Area(), 2)}";
        }
        public void Print()
        {
            Console.WriteLine($"Прямоугльник: {this.ToString()}");
        }
    }
}
