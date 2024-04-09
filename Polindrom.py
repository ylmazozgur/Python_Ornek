import unittest

def is_palindrome(s):
    s = s.lower()
    liste = []
    Rliste = []
    for i in s:
        liste.append(i)
    Rliste = liste.copy()
    Rliste.reverse()

    if liste == Rliste:
        return True
    else:
        return False

# is_palindrome("aba")
# is_palindrome("ali")


class TestPalindrome(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(is_palindrome("a"),True)
        self.assertEqual(is_palindrome("aba"),True)
        self.assertEqual(is_palindrome("Abba"),True)
        self.assertEqual(is_palindrome("amalam"),True)
        self.assertEqual(is_palindrome("walter"),False)
        self.assertEqual(is_palindrome("kodok"),True)
        self.assertEqual(is_palindrome("Kasue"),False)

if __name__ == "__main__":
    unittest.main()



