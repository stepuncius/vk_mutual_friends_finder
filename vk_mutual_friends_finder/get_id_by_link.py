def get_id_by_link(link):
    """Gets link on vk profile and returns identificator of user, that can
    be  used in vkapi functions.

    Vkontakte has to types of links:
    1)vk.com/id[userid] ex.: vk.com/id1
    2)vk.com/[user_alias] ex.: vk.com/anton21 , vk.com/vasya
    We need to parse both of them.
    """
    last_part = link.split("/")[-1]
    is_id = True if last_part[:2] == "id" and last_part[2:].isdigit()\
        else False
    return last_part[2:] if is_id else last_part
