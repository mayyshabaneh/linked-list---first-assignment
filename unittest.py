from assignment1 import  LinkedList

ll = LinkedList()

def test_add_First_Node():
    ll.add_First_Node(1)
    ll.display_List()
    assert ll.head.value == 1 ,"method doesn't work"

def test_add_Last_Node():
    ll.add_Last_Node(1)
    ll.display_List()
    assert ll.head.value == 1 ,"method doesn't work"

def test_insert_At_Index():
    ll.add_First_Node(1)
    ll.add_Last_Node(3)
    ll.insert_At_Index(1, 2)
    ll.display_List()
    assert ll.head.next.value == 2 ,"method doesn't work"
    assert ll.head.next.next.value == 3 ,"method doesn't work"


def test_add_Values():
    ll.add_Values(2)
    ll.add_Values(1)
    ll.add_Values(3)
    ll.display_List()
    assert ll.head.value == 1 ,"method doesn't work"
    assert ll.head.next.value == 2 ,"method doesn't work"
    assert ll.head.next.next.value == 3 ,"method doesn't work"

def test_delete_First():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.display_List()
    deleted_node = ll.delete_First()
    ll.display_List()
    assert deleted_node.value == 1 ,"method doesn't work"
    assert ll.head.value == 2 ,"method doesn't work"

def test_delete_Last():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.display_List()
    deleted_node = ll.delete_Last()
    ll.display_List()
    assert deleted_node.value == 2 ,"method doesn't work"
    assert ll.head.value == 1 ,"method doesn't work"


def test_delete_At_Index():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)
    ll.display_List()
    deleted_node = ll.delete_At_Index(1)
    ll.display_List()
    assert deleted_node.value == 2 ,"method doesn't work"
    assert ll.head.next.value == 3 ,"method doesn't work"

def test_count_Item():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)
    ll.display_List()
    assert ll.count_Item() == 3 ,"method doesn't work"


def test_remove_duplicates():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(2)
    ll.add_Values(3)
    ll.display_List()
    ll.remove_duplicates()
    ll.display_List()
    assert ll.head.next.value == 2 ,"method doesn't work"
    assert ll.head.next.next.value == 3 ,"method doesn't work"


def test_reverse():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)
    ll.display_List()
    ll.reverse()
    ll.display_List()
    assert ll.head.value == 3 ,"method doesn't work"
    assert ll.head.next.value == 2 ,"method doesn't work"
    assert ll.head.next.next.value == 1 ,"method doesn't work"


def test_merge_Lists():
    ll1 = LinkedList()
    ll1.add_Values(1)
    ll1.add_Values(3)
    ll2 = LinkedList()
    ll2.add_Values(2)
    ll2.add_Values(4)
    merged_ll = ll.merge_Lists(ll1, ll2)
    assert merged_ll.head.value == 1 ,"method doesn't work"
    assert merged_ll.head.next.value == 2 ,"method doesn't work"
    assert merged_ll.head.next.next.value == 3 ,"method doesn't work"
    assert merged_ll.head.next.next.next.value == 4 ,"method doesn't work"

def test_merge_Sorted():
    ll1 = LinkedList()
    ll1.add_Values(1)
    ll1.add_Values(3)
    ll2 = LinkedList()
    ll2.add_Values(2)
    ll2.add_Values(4)
    merged_ll = ll.merge_Sorted(ll1, ll2)
    assert merged_ll.head.value == 1 ,"method doesn't work"
    assert merged_ll.head.next.value == 2 ,"method doesn't work"
    assert merged_ll.head.next.next.value == 3 ,"method doesn't work"
    assert merged_ll.head.next.next.next.value == 4 ,"method doesn't work"


def test_split_Halves():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)
    ll.add_Values(4)
    first_half, second_half = ll.split_Halves()
    assert first_half.head.value == 1 ,"method doesn't work"
    assert first_half.head.next.value == 2 ,"method doesn't work"
    assert second_half.head.value == 3 ,"method doesn't work"
    assert second_half.head.next.value == 4 ,"method doesn't work"


def test_reduce_List():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)
    assert ll.reduce_List() == 6 ,"method doesn't work"


def test_return_Index():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)
    assert ll.return_Index(2) == 1 ,"method doesn't work"


def test_print_Asterisk():
    ll.add_Values(1)
    ll.add_Values(2)
    ll.add_Values(3)


test_add_First_Node()
test_add_Last_Node()
test_add_Values()
