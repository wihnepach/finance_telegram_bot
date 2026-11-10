from models.user import User


def test_user_creation():
    user = User(
        telegram_id=123456789,
        username="test_user",
        first_name="Иван"
    )

    assert user.telegram_id == 123456789
    assert user.username == "test_user"
    assert user.first_name == "Иван"
    assert user.currency == "RUB"
    assert user.language == "ru"


def test_user_without_username():
    user = User(
        telegram_id=123456789,
        first_name="Иван"
    )

    assert user.username is None


def test_user_default_timezone():
    user = User(
        telegram_id=123456789,
        first_name="Иван"
    )

    assert user.timezone == "Europe/Moscow"