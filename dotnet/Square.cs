namespace Figures
{
    class Square : Rectangle, IPrint
    {
        private double sideSize = 0;
        public double Side
        {
            get { return this.sideSize; }
            set { this.sideSize = value; }
        }
        public Square(int a = 0)
        {
            this.sideSize = a;
        }

        public override double Area()
        {
            return this.sideSize * this.sideSize;
        }

        public override string ToString()
        {
            return $"side = {this.sideSize}; area: {Math.Round(this.Area(), 2)}";
        }
    }
}
