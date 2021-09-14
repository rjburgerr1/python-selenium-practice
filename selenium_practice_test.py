import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(chrome_options=chrome_options)

def testWebDriver(webDriver):
	driver.get("http://www.python.org")
	assert "Python" in driver.title
	elem = driver.find_element_by_name("q")
	elem.clear()
	elem.send_keys("pycon")
	elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source


def testVerifyLogo(webDriver):
	driver.get("http://www.automationpractice.com")
	assert driver.find_element(By.CSS_SELECTOR, '#header_logo > a > img')

@pytest.mark.skip()	
def testSkip():
	print("Shouldn't print, should be skipped")

@pytest.fixture(scope='session', autouse=True)
def webDriver():
	yield
	driver.close()

# Similar to TestNG groups
# Runs with -m markedTest
@pytest.mark.markedTest
def testMarkedTest():
	assert True

@pytest.mark.xfail
def testFailTest():
	assert 1 == 2

@pytest.mark.parametrize("num",[1, 5, "e", 6.4, 10, True, [1], 19])	
@pytest.mark.xfail
def testParamsFail(num):
	assert isinstance(num, int)

@pytest.fixture()
def get24():
	return 24

def testCheck24(get24):
	assert get24 == 24

@pytest.fixture(scope='function')
def funcScoped():
	return True

@pytest.fixture(scope='class')
def classScoped():
	return True

# Parametrized test for scopes in pytest
# Use with --setup-show
def testScopes(funcScoped, classScoped):
	return True


	
