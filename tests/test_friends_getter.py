import pytest
import vk_mutual_friends_finder as mff


def test_get_friends():
    fg = mff.friends_getter.FriendsGetter()
    assert type(fg.get_friends(
        1)) == set, "non set returned, when number was given"
    assert type(fg.get_friends(
        '1')) == set, "non set returned,  when string was given"
