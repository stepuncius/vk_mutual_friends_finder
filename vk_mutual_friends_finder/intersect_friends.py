import sys
from friends_getter import FriendsGetter


def intersect_friends(list_of_users):
    """Takes list with id's of users and
        returns intersection of sets their friends.
    """
    assert type(list_of_users) == list, "not list given"
    fg = FriendsGetter()
    result = fg.get_friends(list_of_users[0])
    for friends_set in map(fg.get_friends, list_of_users[1:]):
        result &= friends_set
    return result


if __name__ == "__main__":
    print(intersect_friends(sys.argv[1:]))  # sys.argv[0] == current_path
