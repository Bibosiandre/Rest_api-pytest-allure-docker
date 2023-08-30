class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_sum1 = 14
        assert a+b == expected_sum1, f"Sum of variables is not equal to {expected_sum1}"
        assert a+b == 14
    # NEGATIVE_CHECK

    # def test_check_math2(self):
    #     a = 5
    #     b = 11
    #     expected_sum = 14
    #     assert a+b == expected_sum, f"Sum of variables is not equal to {expected_sum}"