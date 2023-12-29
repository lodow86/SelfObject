import pytest

data = (
    {
        'user': 123,
        'password': 'asdfv'
    },
    {
        'user': 123,
        'password': 'z1243'
    }
)
password1 = ['123', '999']
password2 = ['a', 'b']

data_01 = [
    pytest.param(1, 3, 4, id='(a+b):pass'),
    pytest.param(2, 3, 5, id='(a+b):error')
]


# 传字典
@pytest.mark.parametrize('dic', data)
def test01(dic):
    print(dic['user'], dic['password'])


# 传多个参数
@pytest.mark.parametrize('a', password1)
@pytest.mark.parametrize('b', password2)
def test02(a, b):
    print(a + b)


#传参数对比，查看可读性
@pytest.mark.parametrize('a,b,expect', data_01)
def add(a, b):
    return a + b


def test_03(a, b, expect):
    assert add(a, b) == expect


if __name__ == '__main__':
    pytest.main()
