import pytest
import csv


# @pytest.fixture()
def get_data():
    with open('test.csv') as data:  # 打开文件
        lis = csv.reader(data)  # 给list赋值为 csv打开读取的数据
        data2 = []
        for s in lis:
            data2.extend(s)
        return data2
        # print(data2)


@pytest.mark.parametrize('name', get_data())
def test_01(name):
    print(name)


if __name__ == '__main__':
    # get_data()
    pytest.main(['-sv', 'test_csv'])
