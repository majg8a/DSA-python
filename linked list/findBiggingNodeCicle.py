
class ListNode:
    value = None
    next = None

def foo(nodelist: ListNode):
    acumulator = {}
    start = None
    next = nodelist
    while(start == None):
        if acumulator[next.value] == next.value:
            start = next 
        acumulator[next.value] = next.next
        next = next.next
    return start

