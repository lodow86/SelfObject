import xlrd
import pytest
import os


def get_testdata():
    # path = os.path.dirname(os.path.abspath(__file__))
    # filepath = 'file:///' + path + 'testcase\ddt\test.xls'
    filename= 'test.xls'
    all_data = xlrd.open_workbook(filename)  # 打开指定文档获取数据
    '''获取第一个页面的数据'''
    sheet = all_data.sheet_by_index(0)  # 获取第一个sheet页数据
    hang = sheet.nrows  # 行值为sheet页行值
    lie = sheet.ncols  # 列值为sheet页列值
    lis = []
    for rows in range(0,hang):
        for cols in range(0,lie):
            data = sheet.cell_value(rows, cols)  # 将行列对应的单元格数据赋值给data
            lis.append(data)  # 将data值添加到lis中
    return lis


@pytest.mark.parametrize('data', get_testdata())
def test_01(data):
    print(data)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_xlrd.py'])
