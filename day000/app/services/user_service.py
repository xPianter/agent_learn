from app.models.user import User


def parse_age(age: str) -> int | None:
    try:
        return int(age)
    except ValueError:
        return None


def create_user(user_id: int, name: str, age: str) -> User:
    parsed_age = parse_age(age)

    return User(
        id=user_id,
        name=name,
        age=parsed_age,
    )