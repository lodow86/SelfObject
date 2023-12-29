import xlrd
import pytest


def test_data():
    filename = 'test.xls'                           #
    all_data = xlrd.open_workbook(filename)
    sheet = all_data.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    lst = []
    for row in range(nrows):
        for col in range(ncols):
            lst.append(sheet.cell_value(row, col))
    return lst


@pytest.mark.parametrize('user, password', test_data())
def test01(user, password):
    test = {
        "user": user,
        "pwd": password
    }
    print(test)


if __name__ == '__main__':
    pytest.main(['-sv', 'test——xlrd.py'])
