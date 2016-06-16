import collections
import pyvkontakte


def get_names_of_users(set_of_users):
    """Gets set of user's ids and returns namedtuple
        with their names, last names and link on their pages.

        Caution: It can't work with more than 1000 people,
        it's vkapi's feauture.
    """
    VK_ADRESS = "https://vk.com/id"
    assert type(set_of_users) == set, "Not set given"
    if (len(set_of_users) > 1000):
        print("only first thousand of users will be shown.")
    api = pyvkontakte.VkontakteApi()
    string_of_ids = ",".join(map(str, set_of_users))
    response = api.call("users.get", user_ids=string_of_ids, v='5.8')
    user = collections.namedtuple(
        'user', ['adress', 'first_name', 'last_name', 'id'])
    result = [user(
        adress=VK_ADRESS + str(usr['id']),
        id=usr['id'],
        first_name=usr['first_name'],
        last_name=usr['last_name']
        )
        for usr in response]
    return result
if __name__ == "__main__":
    print(get_names_of_users(set((1, 3, 6))))
