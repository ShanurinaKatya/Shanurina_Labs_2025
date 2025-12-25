namespace Figures
{
    class Square : Rectangle, IPrint
    {
        public Square(double a = 0) : base(a, a)
        {
            this.Type = "Square";
        }
    }
} // namespace Figures
