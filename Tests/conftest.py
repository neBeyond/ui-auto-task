import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def init_driver(request):
    driver = webdriver.Chrome(executable_path='../chromedriver.exe')
    request.cls.driver = driver
    yield
    driver.close()
