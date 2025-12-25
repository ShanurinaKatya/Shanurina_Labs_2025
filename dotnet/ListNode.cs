using System;

namespace Figures
{
    public class ListNode<T> where T : IComparable<T>
    {
        public T data { get; set; }
        public ListNode<T> next { get; set; }

        public ListNode(T param)
        {
            this.data = param;
            this.next = null!;
        }
    }
} // namespace Figures
