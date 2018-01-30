# encoding=utf-8'
import copy


def dict_copy_demo():
    """
    shallow copy:
        在dict层次上复制, 不深入value内部结构;
        实现方式: dict内置方法和copy api
    deep copy:
        深入value内部结构;
        实现方式: copy api
    :return:
    """
    print '---dict copy demo'
    d = {
        'old_attr': 'OLD',
        'list': range(0, 10)
    }

    shallow_cp = d.copy()
    shallow_cp['new_attr'] = 'NEW by shallow-cp'
    shallow_cp['list'].append(100)

    shallow_cp2 = copy.copy(d)
    shallow_cp2['new_attr'] = 'NEW by shallow-cp2'
    shallow_cp2['list'].append(101)

    deep_cp = copy.deepcopy(d)
    deep_cp['new_attr'] = 'NEW by deep-cp'
    deep_cp['list'].append(200)
    # result
    print "original:", d
    print "shallow copy:", shallow_cp
    print "shallow copy2:", shallow_cp2
    print "deep copy:", deep_cp


def list_copy_demo():
    """
    shallow copy: 3种实现方式
        list(old)
        old[:]
        copy api
    deep copy:
        copy api
    :return:
    """
    print '---list copy demo'
    l = [1, 2, 'text', {'dict': 'dict'}]
    print "original list:", l

    print "result by step"
    deep_cp = copy.deepcopy(l)
    deep_cp.append(1000)
    deep_cp[3]['dict'] = 'dict deep'
    deep_cp[3]['new dict deep'] = 'new dict deep'
    print "deep cp:", deep_cp

    shallow_cp1 = list(l)
    shallow_cp1.append(100)
    shallow_cp1[3]['dict'] = 'dict1'
    shallow_cp1[3]['new_dict1'] = 'new dict1'
    print "shallow cp1:", shallow_cp1

    shallow_cp2 = l[:]
    shallow_cp2.append(200)
    shallow_cp2[3]['dict'] = 'dict2'
    shallow_cp2[3]['new_dict2'] = 'new dict2'
    print "shallow cp2:", shallow_cp2

    shallow_cp3 = copy.copy(l)
    shallow_cp3.append(300)
    shallow_cp3[3]['dict'] = 'dict3'
    shallow_cp3[3]['new_dict3'] = 'new dict3'
    print "shallow cp3:", shallow_cp3

    print "final result"
    print "original list:", l
    print "shallow cp1:", shallow_cp1
    print "shallow cp2:", shallow_cp2
    print "shallow cp3:", shallow_cp3
    print "deep cp:", deep_cp


if __name__ == '__main__':
    dict_copy_demo()
    list_copy_demo()
