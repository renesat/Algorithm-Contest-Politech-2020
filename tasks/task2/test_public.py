import pytest

from .task import general_prefix


class Case:
    def __init__(self, name: str, k: int, lines: list, prefix: str):
        self._name = name
        self.k = k
        self.lines = lines
        self.prefix = prefix

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        k=3,
        lines=[
            "python",
            "pyramid",
            "pyjamas",
        ],
        prefix="py",
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = general_prefix(k=case.k, lines=case.lines)
    assert answer == case.prefix
