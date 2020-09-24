import pytest

from .task import find_indexes


class Case:
    def __init__(self, name: str, t: int, n: int, a: list, indexes: tuple):
        self._name = name
        self.t = t
        self.n = n
        self.a = a
        self.indexes = indexes

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        t=9,
        n=4,
        a=[2, 7, 11, 15],
        indexes=(0, 1),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = find_indexes(t=case.t, n=case.n, a=case.a)
    assert answer == case.indexes
