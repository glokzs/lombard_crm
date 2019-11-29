from pytest_bdd import scenario, given, then

@scenario('create_loan.feature', 'Create loan')
def test_login(live_server):
    return live_server

@given ('Create superuser')
def super_user(admin_user):
    return admin_user

@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url +'/accounts/login/')


@then('I logging as user')
def user_login(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_css_selector('.btn').click()

@then('I should see index page')
def index(browser):
    assert 'Добро пожаловать' in browser.html
    # assert browser.status_code == 200

@then('I click "Займы"')
def click_loans(browser):
    browser.driver.find_element_by_link_text('Займы').click()

@then('I should see "Список кредитов"')
def users_index(browser):
    assert 'Список кредитов' in browser.html

@then('I click "Добавить операцию"')
def click_create_loans(browser):
    browser.driver.find_element_by_class_name('control-button').click()

@then('I should see "Выбор клиента"')
def create_index(browser):
    assert 'Выбор клиента' in browser.html


@pytest.fixture
def client():

    return client


@then('I click on client')
def click_on_client(browser, ):
    browser.fill('client_search_input', '89')
    from time import sleep
    sleep(0.5)
    browser.driver.find_element_by_css_selector(".recent-client-wrapper > div:nth-child(2)").click()

@then('I click to choose client')
def choose_client(browser):
    browser.driver.find_element_by_css_selector('#client_choose_btn').click()


@then('I should see "Добавить займ"')
def create_index(browser):
    assert 'Добавить займ' in browser.html

@then('I click "Добавить залоговое имущество"')
def click_add_item(browser):
    browser.driver.find_element_by_css_selector(".mb-4").click()

@then('I should see "Добавить залоговое имущество"')
def create_index(browser):
    assert 'Добавить залоговое имущество' in browser.html

@then('I add loan item')
def add_loan_item(browser):
    select_elem = browser.driver.find_element_by_name('category')
    select_elem.click()
    options = select_elem.find_elements_by_tag_name('option')
    options[len(options) - 1].click()
#
#     select_elem = browser.driver.find_element_by_name('subcategory')
#     select_elem.click()
#     options = select_elem.find_elements_by_tag_name('option')
#     options[len(options) - 1].click()


    browser.fill('name', 'test')
    browser.fill('price', '1000')
    browser.fill('description', 'new')
    # browser.fill('criteria', '100')
    # browser.driver.find_element_by_css_selector("#pledge_item_create_button").click()