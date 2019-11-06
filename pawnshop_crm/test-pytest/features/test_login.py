from pytest_bdd import scenario, given, then


@scenario('login.feature', 'Login as admin')
def test_login(live_server):
    return live_server


@given('Create superuser')
def super_user(admin_user):
    return admin_user


@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url + '/admin')


@then('I login as admin')
def admin_login(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_class_name('submit-row').click()


@then('I should see admin page')
def admin_index(browser):
    assert 'Pawnshop' in browser.html


@then('I click "Пользователи"')
def click_users(browser):
    browser.driver.find_element_by_link_text('Пользователи').click()


@then('I should see "Выберите пользователь для изменения"')
def users_index(browser):
    assert 'Выберите пользователь для изменения' in browser.html


@then('I click "Добавить пользователя"')
def click_create_users(browser):
    browser.driver.find_element_by_class_name('addlink').click()


@then('I should see user create menu')
def create_index(browser):
    assert 'Пароль' in browser.html


@then('I enter new user info')
def create_user_form(browser):
    browser.fill('username', 'testuser')
    browser.fill('password1', 'xsw2.1qaz')
    browser.fill('password2', 'xsw2.1qaz')
    browser.fill('user-0-middle_name', 'testuly')
    browser.driver.find_element_by_link_text('Сегодня').click()
    browser.driver.find_element_by_link_text('Сейчас').click()
    browser.fill('user-0-email', 'test@test.ts')
    browser.driver.find_element_by_name('_save').click()


@then('I should see user successful creation')
def creation_success(browser):
    assert 'было успешно добавлено.' in browser.html, "Пожалуйста, исправьте ошибки ниже."


