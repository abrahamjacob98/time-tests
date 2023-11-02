from times import compute_overlap_time
from times import time_range
import pytest

# from times import


# def test_given_input():
#     if __name__ == "__main__":
#         large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#         short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#         result = compute_overlap_time(large, short)
#         expected = 1.75 * 60 * 60
#         assert result == expected
#         print(compute_overlap_time(large, short))


# def test_overlap():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#     short = time_range("2010-01-12 11:30:00", "2010-01-12 11:45:00", 2, 60)
#     result = compute_overlap_time(large, short)
#     expected = 0
#     assert result == expected
#     print(compute_overlap_time(large, short))


def test_edge_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = 0
    print(compute_overlap_time(large, short))
    assert result == expected


# def test_reverse_time():
#     large = time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")
#     # short = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00", 2, 60)
#     result = large
#     expected = True
#     assert result == expected
#     # print(compute_overlap_time(large, short))
