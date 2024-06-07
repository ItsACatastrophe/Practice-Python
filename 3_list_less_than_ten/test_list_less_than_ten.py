from pytest_mock import MockerFixture

from list_less_than_ten import main


def test_main(mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")

    values = [0, 4, 8, 16, 20]
    main(values)

    assert 0 in mock_print.call_args[0][0]
    assert 4 in mock_print.call_args[0][0]
    assert 8 in mock_print.call_args[0][0]
    assert 16 not in mock_print.call_args[0][0]
    assert 20 not in mock_print.call_args[0][0]


def test_empty_result(mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")

    values = [10, 15, 20]
    main(values)

    assert 10 not in mock_print.call_args[0][0]
    assert 15 not in mock_print.call_args[0][0]
    assert 20 not in mock_print.call_args[0][0]

    assert [] == mock_print.call_args[0][0]
