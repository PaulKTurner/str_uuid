from uuid import (
    uuid1,
    uuid3,
    uuid4,
    uuid5
)


def str_uuid1(input: str) -> str:
    return str(uuid1(input))


def str_uuid3(input: str) -> str:
    return str(uuid3(input))


def str_uuid4(input: str) -> str:
    return str(uuid4(input))


def str_uuid5(input: str) -> str:
    return str(uuid5(input))
