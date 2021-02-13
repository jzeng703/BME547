import pytest

@pytest.mark.parametrize("(x1,y1), (x2,y2), x, expected",[
    ((1,1), (2,2), 3, 3),
    ((1,2), (2,4), 3, 6),
    ((0,0), (2,0), 3, 0),
])
def test_line((x1,y1), (x2,y2), x, expected):
    from two_points import line
    answer = line((x1,y1), (x2,y2), x)
    assert answer == expected