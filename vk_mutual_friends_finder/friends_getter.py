import pyvkontakte
import sys
from get_names_of_users import get_names_of_users


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
        # if user_id is alias, replace it with id
        if not self._is_positive_number(user_id):
            user_id = get_names_of_users(set([user_id]))[0].id
        api = pyvkontakte.VkontakteApi()
        return set(api.call('friends.get', user_id=user_id)['items'])


if __name__ == '__main__':
    fg = FriendsGetter()
    print("Pavel Durov's friends:")
    print(fg.get_friends(1))  # 1 == Pavel Durov's (vkontakte's founder) id
