from pytest_bdd import scenario, given, then


@scenario('login.feature', 'Login as admin')
def test_login(live_server):
    return live_server

@given ('Create superuser')
def super_user(admin_user):
    return admin_user

@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url +'/admin')


@then('I logging as admin')
def admin_login(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_class_name('submit-row').click()

@then('I should see admin page')
def admin_index(browser):
    assert 'Pawnshop' in browser.html
    # assert browser.status_code == 200

@then('I click "Пользователи"')
def click_users(browser):
    browser.driver.find_element_by_class_name('model-user').first().click()

@then('I should see "Выберите пользователь для изменения"')
def admin_index(browser):
    assert 'Выберите пользователь для изменения' in browser.html

