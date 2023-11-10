"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import pytest
from src.stack import Node, Stack

n1 = Node(5, None)
n2 = Node('a', n1)


def test_node():
    assert n1.data == 5
    assert n2.data == 'a'


stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

def test_stack():
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'
    assert stack.top.next_node.next_node.data == 'data1'
    assert stack.top.next_node.next_node.next_node == None

# ---------- coverage: platform darwin, python 3.11.3-final-0 ----------
# Name                 Stmts   Miss  Cover
# ----------------------------------------
# src/__init__.py          0      0   100%
# src/linked_list.py      17     17     0%
# src/queue.py            12     12     0%
# src/stack.py            15      3    80%


# home wprk 2
def test_pop1():
    stack = Stack()
    stack.push('data1')
    data = stack.pop()
    assert stack.top is None
    assert data == 'data1'


def test_pop2():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()
    assert stack.top.data == 'data1'
    assert data == 'data2'

# ---------- coverage: platform darwin, python 3.11.3-final-0 ----------
# Name                 Stmts   Miss  Cover
# ----------------------------------------
# src/__init__.py          0      0   100%
# src/linked_list.py      17     17     0%
# src/queue.py            12     12     0%
# src/stack.py            15      0   100%
