from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from ape.api import AccountAPI
    from ape.contracts import ContractContainer, ContractInstance


def pytest_addoption(parser):
    parser.addoption(
        "--no-forks",
        action="store_true",
        help="Don't run tests requiring forked networks",
    )


@pytest.fixture(scope="session")
def run_fork_tests(request):
    return not request.config.getoption("--no-forks")


@pytest.fixture(scope="session")
def contract(project) -> "ContractContainer":
    return project.VyperContract


@pytest.fixture(scope="session")
def owner(accounts) -> "AccountAPI":
    return accounts[0]


@pytest.fixture(scope="session")
def not_owner(accounts) -> "AccountAPI":
    return accounts[1]


@pytest.fixture(scope="session")
def contract_instance(contract, owner) -> "ContractInstance":
    return contract.deploy(123, sender=owner)
