import pytest
from vk_mutual_friends_finder import get_id_by_link as gidbl
def test_get_id_by_link():
    assert gidbl.get_id_by_link("vk.com/tolya") == "tolya"
    assert gidbl.get_id_by_link("vk.com/id256") == "256"
    assert gidbl.get_id_by_link("vk.com/idiot") == "idiot"
    assert gidbl.get_id_by_link("vk.com/id1ot") == "id1ot"
    assert gidbl.get_id_by_link("http://vk.com/tolya") == "tolya"
    assert gidbl.get_id_by_link("https://vk.com/id1ot") == "id1ot"
