import pytest
import json

'''json格式参数化'''
def test_get_data():
    with open('json.json') as f:
        lst = []
        data = json.load(f)  # 加载json数据为data
        lst.extend(data["user"])  # 提供数据data里的user
        return lst
        # print(lst)


@pytest.mark.parametrize('user',test_get_data())       #将user值传过来 数据来源于test_get_data()
def test_01(user):
    print(user+'1')


if __name__ == '__main__':
    # print(test_get_data())
    pytest.main(['-sv', 'test_json.py'])
