from src.stack import Node, Stack

if __name__ == '__main__':
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)  # 5
    print(n2.data)  # a
    print(n1)  # <__main__.Node object at 0x0000022803036050>
    print(n2.next_node)  # <__main__.Node object at 0x0000022803036050>

    # пушинг
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    # выгрузка начиная с верхушки
    print(stack.top.data)  # data3
    print(stack.top.next_node.data)  # data2
    print(stack.top.next_node.next_node.data)  # data1
    print(stack.top.next_node.next_node.next_node)  # None

    # чтобы код завершался без ошибки нижняя строка закомментирована
    # print(stack.top.next_node.next_node.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'
