import pyvkontakte
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
        """Takes user's friends by id of user given
        as string or int and returns friends as set

        I really have no idea how to write a full test for it
        because we haven't immutable users.
        """
        # if user_id is alias, replace it with id
        if not self._is_positive_number(user_id):
            user_id = get_names_of_users(set([user_id]))[0].id
        api = pyvkontakte.VkontakteApi()
        return set(api.call('friends.get', user_id=user_id, v='5.8')['items'])
