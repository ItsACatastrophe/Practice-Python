from odd_or_even import main

from pytest_mock import MockerFixture


def test_no_remainder(mocker: MockerFixture):
    mocker.patch("builtins.input").side_effect = ["4", "2"]

    mock_print = mocker.patch("builtins.print")

    main()

    assert "not" not in mock_print.call_args[0][0]


def test_has_remainder(mocker: MockerFixture):
    mocker.patch("builtins.input").side_effect = ["2", "3"]

    mock_print = mocker.patch("builtins.print")

    main()

    assert "not" in mock_print.call_args[0][0]
