from uuid import (
    uuid1,
    uuid3,
    uuid4,
    uuid5
)


def str_uuid1() -> str:
    return uuid1().hex


def str_uuid3() -> str:
    return uuid3().hex


def str_uuid4() -> str:
    return uuid4().hex


def str_uuid5() -> str:
    return uuid5().hex
