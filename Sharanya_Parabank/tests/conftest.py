import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    url = "https://parabank.parasoft.com/parabank/admin.htm"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
