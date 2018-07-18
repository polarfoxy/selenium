import pytest
from selenium import webdriver



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path='C:\pyton\env\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.ya.ru")
    driver.get("http://www.yandex.ru")