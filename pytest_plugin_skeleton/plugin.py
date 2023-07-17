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

def configure(config):
    new_ini_config = config.getini("new_ini_config")
    if not new_ini_config:
        return