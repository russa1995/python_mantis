import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    return fixture


@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = ORMFixture(host=db_config["host"], user=db_config["user"], password=db_config["password"], db=db_config["db"])
    return dbfixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


#def pytest_generate_tests(metafunc):
#    for fixture in metafunc.fixturenames:
#        if fixture.startswith("data_"):
#            testdatas = load_from_module(fixture[5:])
#            metafunc.parametrize(fixture, testdatas, ids=(str(x) for x in testdatas))
#        elif fixture.startswith("json_"):
#            testdatas = load_from_json(fixture[5:])
#            metafunc.parametrize(fixture, testdatas, ids=(str(x) for x in testdatas))


#def load_from_module(module):
#     return importlib.import_module("data.%s" % module).testdatas


#def load_from_json(file):
#    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
#        return jsonpickle.decode(f.read()) 