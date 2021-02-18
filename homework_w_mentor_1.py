import unittest


def get_longest_str(input_list):
    """Returns the longest string"""
    longest_str = ""
    for element in input_list:
        if len(element) >= len(longest_str):
            longest_str = element
    return longest_str


def get_kth_longest_str(input_list, k=1):
    """ Returns the kth longest string """
    # bubblesort_list = input_list
    # for i in range(len(input_list) - 1):
    #     for x in range(len(input_list) - 1 - i):
    #         if len(bubblesort_list[x]) < len(bubblesort_list[x+1]):
    #             temp = bubblesort_list[x]
    #             bubblesort_list[x] = bubblesort_list[x+1]
    #             bubblesort_list[x+1] = temp

    # return bubblesort_list[k-1]

    sorted_list = []

    for i in range(len(input_list)):
        longest_str = get_longest_str(input_list)
        sorted_list.append(longest_str)
        input_list.remove(longest_str)

    return sorted_list[k - 1]

    # Next Solution: split the list in two with shortest, longest lists then sort each list


class KthLongestTest(unittest.TestCase):
    def test_three_strings_longest_is_last(self):
        result = get_longest_str(["A", "String", "But this is longer"])

        self.assertEqual(result, "But this is longer")

    def test_three_strings_longest_is_middle(self):
        result = get_longest_str(["A", "But this is longer", "String"])

        self.assertEqual(result, "But this is longer")

    def test_three_strings_tie_for_longest(self):
        result = get_longest_str(["A", "String 1", "String 2"])

        self.assertEqual(result, "String 2")

    def test_longest_element_and_k_is_one(self):
        result = get_kth_longest_str(["String 1"], 1)

        self.assertEqual(result, "String 1")

    def test_two_elements_get_longest_and_k_is_one(self):
        result = get_kth_longest_str(["A", "String 1"], 1)

        self.assertEqual(result, "String 1")

    def test_two_elements_first_is_longer_and_k_is_one(self):
        result = get_kth_longest_str(["String 1", "A"], 1)

        self.assertEqual(result, "String 1")

    def test_three_elements_first_is_longest_and_k_is_two(self):
        result = get_kth_longest_str(["A", "But this is longer", "String 1"], 2)

        self.assertEqual(result, "String 1")

    def test_three_elements_two_same_entry_and_k_is_two(self):
        result = get_kth_longest_str(["A", "String", "But this is longer"], 2)

        self.assertEqual(result, "String")

    def test_four_elements_and_k_is_two(self):
        result = get_kth_longest_str(
            ["A", "String 1", "String", "But this is longer"], 2
        )

        self.assertEqual(result, "String 1")

    def test_four_elements_and_k_is_three(self):
        result = get_kth_longest_str(
            ["A", "String 1", "String", "But this is longer"], 3
        )

        self.assertEqual(result, "String")

    def test_four_elements_and_k_is_four(self):
        result = get_kth_longest_str(
            ["A", "String 1", "String", "But this is longer"], 4
        )

        self.assertEqual(result, "A")

    def test_four_elements_and_k_is_four_in_diff_order(self):
        result = get_kth_longest_str(
            ["String 2", "But this is longer", "A", "String 1"], 4
        )

        self.assertEqual(result, "A")


unittest.main()
