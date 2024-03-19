import pytest


class TestStringReversal:
    @pytest.mark.parametrize(
        "input_str, expected_result",
        [
            ("Let's take LeetCode contest", "contest LeetCode take Let's"),
        ]
                            )
    def test_reverse_string(self, input_str, expected_result):
        output = self.reverse_string(input_str)
        assert output == expected_result

    @staticmethod
    def reverse_string(input_str: str) -> object:
        return " ".join(reversed(input_str.split()))

        # OR
        # word_list = input_str.split()
        # unstructured_data_in_reverse_order = reversed(word_list)
        # new_reversed_list = list(unstructured_data_in_reverse_order)
        # new_sentence = " ".join(new_reversed_list)
        # return new_sentence
