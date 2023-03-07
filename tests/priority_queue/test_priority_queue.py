from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"qtd_linhas": 5})
    priority_queue.enqueue({"qtd_linhas": 3})

    assert len(priority_queue) == 2
    assert priority_queue.search(0) == {"qtd_linhas": 3}
    assert priority_queue.search(1) == {"qtd_linhas": 5}

    with pytest.raises(IndexError):
        priority_queue.search(7)

    assert priority_queue.dequeue() == {"qtd_linhas": 3}
    assert priority_queue.dequeue() == {"qtd_linhas": 5}
    assert len(priority_queue) == 0
