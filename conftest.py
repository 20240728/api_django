import pytest


def pytest_addoption(parser):
    # 添加命令行参数
    parser.addoption(
        "--env", default="PRD", choices=["SIT", "UAT", "PRD"], help="切换环境参数"
    )


@pytest.fixture(scope="class")
def get_env(request):
    # 获取环境参数 --env
    return request.config.getoption("--env")


