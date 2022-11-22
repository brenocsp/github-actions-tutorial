import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  
  def setUp(self):
    self.stack = Stack()

  def testEmptyStack(self):
    self.assertTrue(self.stack.is_empty())

  def testNotEmptyStack(self):
    self.stack.push(1)
    self.assertFalse(self.stack.is_empty())

  def testSizeStack(self):
    self.stack.push(1)
    self.stack.push(2)
    self.stack.push(3)
    size = self.stack.size
    self.assertEqual(3, size)

  def testPushPopStack(self):
    self.stack.push(1)
    self.stack.push(2)
    self.stack.push(3)
    self.stack.pop()
    result = self.stack.pop()
    self.assertEqual(2, result)

  def testEmptyStackException(self):
    self.stack.push(10)
    self.stack.pop()
    with self.assertRaises(Exception):
      self.stack.pop()
