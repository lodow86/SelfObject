import pytest
import json


def test_json_user():
    with open('json.json') as data:
        user_lis = []
        data = json.load(data)
        user_lis.extend(data['user'])
        return user_lis


def test_json_account():
    with open('json.json') as f:
        account_lis = []
        data = json.load(f)
        account_lis.extend(data['account'])
        return account_lis


@pytest.mark.parametrize('user', test_json_user())
@pytest.mark.parametrize('account', test_json_account())
def test_login(user, account):
    print(user+account)


if __name__ == '__main__':
    # print(test_json())
    pytest.main(['-sv', 'test_json2.py'])