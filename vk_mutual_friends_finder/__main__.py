import sys
import get_id_by_link as gidb
import get_names_of_users
import intersect_friends


if __name__ == "__main__":
    ids = intersect_friends.intersect_friends(list(
        map(lambda x:
            gidb.get_id_by_link(x) if "vk.com" in x else x, sys.argv[1:])))
    result = get_names_of_users.get_names_of_users(ids)
    for user in result:
        print(user.first_name, user.last_name, user.adress)
    print("total:", len(result))
