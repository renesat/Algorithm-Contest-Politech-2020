import pytest

from .task import get_water_count


class Case:
    def __init__(self, name: str, partitions: list, water_count: int):
        self._name = name
        self.partitions = partitions
        self.water_count = water_count

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        partitions=[0, 1, 0, 1, 2, 1, 0, 2],
        water_count=4,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = get_water_count(partitions=case.partitions)
    assert answer == case.water_count
