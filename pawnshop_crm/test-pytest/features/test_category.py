from pytest_bdd import scenario, given, then


@scenario('category.feature', 'Create category')
def test_category(live_server):
    return live_server

@given("Create superuser")
def super_user(admin_user):
    return admin_user

@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url + '/admin')


@then('I login as admin')
def admin_log_in(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_class_name('submit-row').click()

@then('I should see admin page')
def admin_index(browser):
    assert 'Pawnshop' in browser.html

@then('I click on Category option')
def admin_page_category(browser):
    browser.driver.find_element_by_link_text('Категории').click()

@then('I should see Category list')
def category_index(browser):
    assert 'Категория' in browser.html


@then('I click creation option')
def click_create_catefory(browser):
    browser.driver.find_element_by_class_name('addlink').click()

@then('I should see form')
def category_form(browser):
    assert 'Добавить Категория' in browser.html

@then('I filling name and tariff and save form')
def fill_form(browser):
    browser.fill('name', 'Тест категория')
    browser.fill('interest_rate', '0,9')
    browser.driver.find_element_by_name('_save').click()

@then('I should see Category list and success message')
def success_message(browser):
    assert 'было успешно добавлено' in browser.html

@then('I click main admin menu')
def click_admin_main_menu(browser):
    browser.driver.find_element_by_link_text('Начало').click()

@then('I should see admin page')
def see_admin_index(browser):
    assert 'Pawnshop' in browser.html

@then('I click subcategory option')
def admin_page_subcategory(browser):
    browser.driver.find_element_by_link_text('Подкатегории').click()

@then('I should see subcategory menu')
def subcategory_menu(browser):
    assert 'Подкатегория' in browser.html

@then('I click create subcategory option')
def click_create_subcategory(browser):
    browser.driver.find_element_by_class_name('addlink').click()

@then('I should see create subcategory form')
def see_subcategory_creattion_form(browser):
    assert 'Добавить Подкатегория' in browser.html

@then('I filling form and click save')
def fill_subcategory_form(browser):
    select_elem = browser.driver.find_element_by_name('category')
    select_elem.click()
    options = select_elem.find_elements_by_tag_name('option')
    options[len(options) - 1].click()
    browser.fill('name', 'Тест подкатегория')
    browser.driver.find_element_by_name('_save').click()

@then('I should see success creation page')
def success_message(browser):
    assert 'было успешно добавлено' in browser.html
