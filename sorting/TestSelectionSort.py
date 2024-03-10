import unittest
import selection_sort

class TestSelectionSort(unittest.TestCase):

    def test_selection_sort_empty_array(self):
        arr = []
        sorted_arr = selection_sort.selection_sort(arr)
        self.assertEqual(sorted_arr,[])
    def test_selection_sort_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = selection_sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_selection_sort_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = selection_sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_selection_sort_random_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = selection_sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])



if __name__ == '__main__':
    unittest.main()