def pytest_addoption(parser):
    parser.addoption(
        "--new-cli-arg",
        action="store_true",
        help="New cli argument that does something"
        )
    
    parser.addini(
        "doctest_optionflags",
        "Option flags for doctests",
        type="args",
        default=["NORMALIZE_WHITESPACE", "ELLIPSIS", "IGNORE_EXCEPTION_DETAIL"]
        )