using System;
using System.ComponentModel;

namespace Figures
{
    public class SimpleList<T> : IEnumerable<T> where T : IComparable<T>
    {
        private ListNode<T> head = null!;
        private int _count;

        public int Count
        {
            get { return this._count; }
            protected set { this._count = value; }
        }

        public void Push(T param)
        {
            ListNode<T> newElement = new ListNode<T>(param);
            if (head == null)
            {
                this.head = newElement;
            }
            else
            {
                ListNode<T> currentNode = head;
                while (currentNode.next != null)
                {
                    currentNode = currentNode.next;
                }
                currentNode.next = newElement;
            }
            _count++;
        }

        public T Pop()
        {
            if (head == null)
            {
                throw new Exception("Cannot pop element from empty list!");
            }

            ListNode<T> currentNode = this.head;
            while (currentNode.next.next != null)
            {
                currentNode.next = currentNode.next.next;
            }
            T lastNodeData = currentNode.next.data;
            currentNode.next.next = null!;
            this.Count--;
            return lastNodeData;
        }

        public void Sort()
        {
            if (head == null || head.next == null)
            {
                return;
            }

            bool swapped;
            do
            {
                swapped = false;
                ListNode<T> currentNode = head;
                ListNode<T> prevNode = null!;

                while (currentNode != null && currentNode.next != null)
                {
                    if (currentNode.data.CompareTo(currentNode.next.data) > 0)
                    {
                        ListNode<T> sortNext = currentNode.next;
                        currentNode.next = sortNext.next;
                        sortNext.next = currentNode;
                        if (prevNode == null)
                        {
                            head = sortNext;
                        }
                        else
                        {
                            prevNode.next = sortNext;
                        }
                        swapped = true;
                    }

                    prevNode = currentNode;
                    currentNode = currentNode.next;
                }
            } while (swapped);
        }

        public IEnumerator<T> GetEnumerator()
        {
            ListNode<T> current = head;
            while (current != null)
            {
                yield return current.data;
                current = current.next;
            }
        }

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
