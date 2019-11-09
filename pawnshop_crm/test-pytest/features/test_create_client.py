from pytest_bdd import scenario, given, then


@scenario('create_loans.feature', 'Create loan')
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


@then('I enter new client info')
def Create_client_form(browser):
    browser.fill('first_name', 'Ivan')
    browser.fill('last_name', 'Ivanov')
    browser.fill('middle_name', 'Ivanovich')
    browser.fill('birth_date', '10.05.1988')
    browser.fill('location', 'Алматы')
    browser.fill('street', 'Достык')
    browser.fill('house_number', '47')
    browser.fill('apartment_number', '21')
    browser.fill('actual_address', 'Талгар')
    browser.fill('birth_place', 'Казахстан')
    browser.fill('phone', '77059056487')
    browser.fill('email', 'Ivan@gmail.com')
    browser.fill('citizenship', 'Казахстан')
    browser.driver.find_element_by_css_selector("button[type='submit']").click()

@then('I should see "Добавить документ"')
def creation_success(browser):
    assert 'Добавить документ' in browser.html

@then('I enter client document info')
def Create_client_document_form(browser):
    select_elem = browser.driver.find_element_by_name('document_type')
    select_elem.click()
    options = select_elem.find_elements_by_tag_name('option')
    options[len(options) - 1].click()
    browser.fill('iin', '123456789012')
    browser.fill('serial_number', '123456789')
    select_elem = browser.driver.find_element_by_name('given_by')
    select_elem.click()
    options = select_elem.find_elements_by_tag_name('option')
    options[len(options) - 1].click()
    browser.fill('given_at', '12.05.2015')
    browser.driver.find_element_by_css_selector("button[type='submit']").click()

@then('I should see "Выбор клиента"')
def create_index(browser):
    assert 'Выбор клиента' in browser.html