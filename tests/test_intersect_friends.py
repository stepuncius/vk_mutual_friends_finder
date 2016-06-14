import pytest
import vk_mutual_friends_finder.intersect_friends as mff


def test_intersect_friends():
    with pytest.raises(TypeError):
        mff.intersect_friends()
    with pytest.raises(AssertionError):
        mff.intersect_friends(set())
    assert type(mff.intersect_friends([1, 2])) == set
