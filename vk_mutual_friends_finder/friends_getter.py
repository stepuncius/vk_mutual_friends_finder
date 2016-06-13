import pyvkontakte
import sys


class FriendsGetter:

    def _is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def get_friends(self, user_id):
        """ Gets user's friends by id of user given
        as string or int and returns friends as set

        I really have no idea how to write a full test for it
        because we haven't immutable users.
        """
        assert self._is_number(user_id), "not correct id"
        api = pyvkontakte.VkontakteApi()
        return set(api.call('friends.get', user_id=user_id)['items'])
if __name__ == '__main__':
    fg = FriendsGetter()
    print(fg.get_friends(1))  # Pavel Durov's (vkontakte's founder) id
    print(fg.get_friends('1'))
    print(fg.get_friends("uuuuuu"))
    print(fg.get_friends(""))
