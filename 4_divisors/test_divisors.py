from divisors import main, main2, main3

solution_refs = [main, main2, main3]


def test_finds_divisors():
    for f in solution_refs:
        result = f(6)

        assert 1 in result
        assert 2 in result
        assert 3 in result
        assert 6 in result
