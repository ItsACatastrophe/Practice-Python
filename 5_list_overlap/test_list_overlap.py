from list_overlap import main


def test_finds_overlap():
    l1 = [0, 2, 4, 5, 6, 7, 9, 10]
    l2 = [2, 3, 4, 8, 9]

    result = main(l1, l2)

    for e in result:
        assert e in l1 and e in l2


def test_list_duplicates():
    l1 = [0, 2, 4, 5, 6, 7, 9, 10]
    l2 = [2, 2, 3, 4, 4]

    result = main(l1, l2)

    for e in result:
        assert result.count(e) == 1
