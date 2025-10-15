import unittest
from fundamentals import * 

class TestProblems(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_find_max(self):
        self.assertEqual(find_max([1, 4, 2, 10]), 10)
        self.assertEqual(find_max([-5, -2, -10]), -2)
        self.assertEqual(find_max([3]), 3)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("cat"), "tac")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_average(self):
        self.assertAlmostEqual(average([2, 4, 6]), 4.0)
        self.assertAlmostEqual(average([1]), 1.0)
        self.assertEqual(average([]), 0)

    def test_word_in_sentence(self):
        self.assertTrue(word_in_sentence("cat", "The cat is sleeping"))
        self.assertFalse(word_in_sentence("dog", "The cat is sleeping"))
        self.assertTrue(word_in_sentence("Python", "I am learning Python"))
        self.assertFalse(word_in_sentence("java", "Python is great"))
    
    
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([4, 4, 4, 4]), [4])
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(5), [1, 2, "Fizz", 4, "Buzz"])
        self.assertEqual(fizzbuzz(3), [1, 2, "Fizz"])
        self.assertEqual(fizzbuzz(15)[-1], "FizzBuzz")
        self.assertIn("FizzBuzz", fizzbuzz(30))


if __name__ == "__main__":
    unittest.main()
