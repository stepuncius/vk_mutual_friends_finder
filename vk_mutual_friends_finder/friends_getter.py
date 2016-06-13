import pyvkontakte
import sys


class FriendsGetter:

    def _is_positive_number(self, s):
        try:
            n = int(s)
            if n > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_friends(self, user_id):
        """ Gets user's friends by id of user given
        as string or int and returns friends as set

        I really have no idea how to write a full test for it
        because we haven't immutable users. But I still can test
        assertion on incorrect id's.
        """
        assert self._is_positive_number(user_id), "not correct id"
        api = pyvkontakte.VkontakteApi()
        return set(api.call('friends.get', user_id=user_id)['items'])


if __name__ == '__main__':
    fg = FriendsGetter()
    print("Pavel Durov's friends:")
    print(fg.get_friends(1))  # 1 == Pavel Durov's (vkontakte's founder) id
