def pytest_addoption(parser):
    parser.addoption(
        "--new-cli-arg",
        action="store_true",
        help="New cli argument that does something"
        )
    
    parser.addini(
        "new_ini_config",
        "An ini config that configures something"
    )