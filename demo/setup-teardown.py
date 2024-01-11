import pytest

@pytest.fixture(scope="function")
def setup_teardown():
    print("Setup")

    # 在测试函数开始之前执行设置操作

    yield  # 运行测试代码

    print("Teardown")

    # 在测试函数结束后执行清理操作

def test_1(setup_teardown):
    print("Running test_1")

def test_2(setup_teardown):
    print("Running test_2")

if __name__ == '__main__':
    testcase = setup_teardown()
    testcase(test_1(),test_2())