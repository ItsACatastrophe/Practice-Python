from datetime import date

from pytest_mock import MockerFixture

from character_input import main


def test_success(mocker: MockerFixture):
    # Utilizing the iterable input of side_effect
    mocker.patch("builtins.input").side_effect = ["Catherine", "90"]
    mock_print = mocker.patch("builtins.print")

    main()

    assert "Catherine" in mock_print.call_args[0][0]
    assert str(date.today().year + 9) in mock_print.call_args[0][0]
    assert str(date.today().year + 10) in mock_print.call_args[0][0]
