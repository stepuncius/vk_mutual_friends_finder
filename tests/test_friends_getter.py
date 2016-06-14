import pytest
import vk_mutual_friends_finder as mff


def test_get_friends():
    fg = mff.friends_getter.FriendsGetter()
    assert type(fg.get_friends(
        1)) == set, "non set returned, when number was given"
    assert type(fg.get_friends(
        '1')) == set, "non set returned,  when string was given"
    with pytest.raises(AssertionError):
        fg.get_friends("uuuuuu")
    with pytest.raises(AssertionError):
        fg.get_friends("19u5uad21")
    with pytest.raises(AssertionError):
        fg.get_friends("2.5")
    with pytest.raises(AssertionError):
        fg.get_friends(-5)
    with pytest.raises(AssertionError):
        fg.get_friends("-5")
    with pytest.raises(AssertionError):
        fg.get_friends("-5.0")
