import collections
import pytest
import vk_mutual_friends_finder.get_names_of_users as gnfu


def test_get_names_of_friends():
    with pytest.raises(TypeError):
        gnfu.get_names_of_users()
    with pytest.raises(AssertionError):
        gnfu.get_names_of_users([1, 2, 3])
    durov = gnfu.get_names_of_users(set((1, )))[0]
    assert isinstance(durov, tuple),\
        "Function must return namedtuple.".format(type_of_result)
    assert durov.last_name == "Дуров" and durov.first_name == "Павел" \
        and durov.id == 1, \
        "Wrong result returned or Pavel Durov changed his name :)"
