# encoding=utf-8
from enum import Enum, unique


class EnumDemo:
    """
    TIP:
        1. enum类型实例的__str__方法: class_name.member_name
        2. 每个实例默认拥有两个属性: name, value
        3. 两个enum对象比较推荐根据identity(is), 当然也可以用==比较
    """
    __week = Enum('Week', ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))

    def __init__(self):
        EnumDemo.itr_by_list()
        print '-----------'
        EnumDemo.itr_by_buildinattr()
        print '-----------'
        day_by_name = EnumDemo.get_day_by_name('Sun')
        print 'Sun of the week: name=%s, value=%s' % (day_by_name.name, day_by_name.value)
        day_by_value = EnumDemo.get_day_by_value(1)
        print 'the 1st day of the week: name=%s, value=%s' % (day_by_value.name, day_by_value.value)
        print '-----------'
        m1 = EnumDemo.__week.Mon
        m2 = EnumDemo.__week.Tue
        print ' %s is %s: %s' % (m1, m2, EnumDemo.cmp_by_is(m1, m2))
        print ' %s equals to %s: %s' % (m1, m2, EnumDemo.com_by_equals(m1, m2))

    @staticmethod
    def itr_by_list():
        for member in list(EnumDemo.__week):
            print 'name=%s, value=%s' % (member.name, member.value)

    @staticmethod
    def itr_by_buildinattr():
        """
        enum的__members__是一个dict({member.name: member})
        :return:
        """
        for member in EnumDemo.__week.__members__.values():
            print 'name=%s, value=%s' % (member.name, member.value)

    @staticmethod
    def get_day_by_name(name):
        return EnumDemo.__week[name]

    @staticmethod
    def get_day_by_value(idx):
        return EnumDemo.__week(idx)

    @staticmethod
    def cmp_by_is(m1, m2):
        return m1 is m2

    @staticmethod
    def com_by_equals(m1, m2):
        return m1 == m2


class MyEnumDemo:
    def __init__(self):
        print '-----------'
        m_1st = MyEnum.FirstMem
        print '%s(%s): name=%s, value=(%s:%s)' % (m_1st, type(m_1st), m_1st.name, m_1st.value.key, m_1st.value.title)
        print 'MyEnum.FirstMem: %s' % MyEnum.get_by_key(1)
        print 'MyEnum.SecondMem: %s' % MyEnum.get_by_title('2nd')


class EnumVal:
    def __init__(self, key, title):
        self.key = key
        self.title = title


@unique
class MyEnum(Enum):
    """
    自定义枚举类:
        1. 枚举类名称: 等号左边(字符串)
        2. 枚举类取值: 等号右边
    """
    FirstMem = EnumVal(1, '1st')
    SecondMem = EnumVal(2, '2nd')

    @staticmethod
    def get_by_key(key):
        for item in list(MyEnum):
            if item.value.key == key:
                return item
        raise ValueError('key does not exist')

    @staticmethod
    def get_by_title(title):
        for item in list(MyEnum):
            if item.value.title == title:
                return item
        raise ValueError('title does not exist')


if __name__ == "__main__":
    EnumDemo()
    MyEnumDemo()
