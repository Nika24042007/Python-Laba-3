import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.__len__(), 0)

    def test_enqueue(self):
        self.queue.enqueue(2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.__len__(), 1)

        self.queue.enqueue(3)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.__len__(), 2)

    def test_front(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.front(), 3)

        self.queue.enqueue(10)
        self.assertEqual(self.queue.front(), 3)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(3)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 1)