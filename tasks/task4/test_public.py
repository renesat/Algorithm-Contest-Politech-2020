import pytest

from .task import non_repeating_characters


class Case:
    def __init__(self, name: str, line: str, length: int):
        self._name = name
        self.line = line
        self.length = length

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(name='base', line="abcabcbb", length=3),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = non_repeating_characters(line=case.line)
    assert answer == case.length
