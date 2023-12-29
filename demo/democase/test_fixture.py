import pytest


@pytest.fixture()  # 将下面的第一个函数变更为一个参数
def test01():
    print('test01')
    return 1


def test2(test01):
    a = 2
    print(test01 + a)
    return test01 + a


def test3(test02):
    a = 3
    print(test02 + a)


if __name__ == '__main__':
    pytest.main(['-sv'], 'test_fixture.py')
