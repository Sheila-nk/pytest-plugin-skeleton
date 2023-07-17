def pytest_addoption(parser):
    parser.addoption(
        "--new-cli-arg",
        action="store_true",
        help="New cli argument that does something"
        )