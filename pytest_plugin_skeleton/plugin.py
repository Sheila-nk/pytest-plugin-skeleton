def pytest_addoption(parser):
    parser.addoption(
        "--new-cli-arg",
        action="store_true",
        help="New cli argument that does something"
        )

def pytest_configure(config):
    new_cli_arg = config.getoption("--new-cli-arg")
    if not new_cli_arg:
        return