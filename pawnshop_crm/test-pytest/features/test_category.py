from pytest_bdd import scenario, given, then, when
import factory
from pytest_factoryboy import register

from pawnshop.models import Category


@scenario('category.feature', 'Логирование')
def test_login(live_server):
    return live_server


@given("Суперпользователь")
def super_user_login(admin_user):
    return admin_user


@given('Страница авторизации')
def go_to_login_page_login(browser, live_server):
    browser.visit(live_server.url + '/admin')


@when('Я логирусь как администратор')
def admin_log_in_login(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_class_name('submit-row').click()


@then('Я должен видеть админ страницу')
def admin_index_login(browser):
    assert 'Pawnshop' in browser.html


@scenario('category.feature', 'Создание категорий')
def test_category(live_server):
    return live_server


@given('Суперпользователь')
def super_user_category(admin_user):
    return admin_user


@given('Страница входа в форму создания категорий')
def go_to_login_page_category(browser, live_server):
    browser.visit(live_server.url + '/admin/pawnshop/category/add/')


@when('Я логирусь как администратор')
def admin_log_in_category(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_class_name('submit-row').click()


@when('Я заполняю поля формы категорий')
def fill_form_category(browser):
    browser.fill('name', 'Тест категория')
    browser.fill('interest_rate', '0,9')
    browser.driver.find_element_by_name('_save').click()


@then('Я вижу сообщение об успешном создании категории')
def check_category_list_category(browser):
    assert 'было успешно добавлено' in browser.html


@register
class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    pk = '1'
    name = 'test_category'
    interest_rate = '0.9'


@scenario('category.feature', 'Создание подкатегорий')
def test_subcategory(live_server):
    return live_server


@given('Суперпользователь')
def super_user_subcategory(admin_user):
    return admin_user


@given('Категория')
def test_category_category():
    category = CategoryFactory.build()
    category.save()
    return category


@given('Страница входа в форму создания подкатегорий')
def go_to_login_page_subcategory(browser, live_server):
    browser.visit(live_server.url + '/admin/pawnshop/subcategory/add/')


@when('Я логирусь как администратор')
def admin_log_in_subcategory(browser):
    browser.fill('username', 'admin')
    browser.fill('password', 'password')
    browser.driver.find_element_by_class_name('submit-row').click()


@when('Я заполняю поля формы подкатегорий')
def fill_subcategory_form(browser):
    select_elem = browser.driver.find_element_by_name('category')
    select_elem.click()
    options = select_elem.find_elements_by_tag_name('option')
    options[len(options) - 1].click()
    browser.fill('name', 'Тест подкатегория')
    browser.driver.find_element_by_name('_save').click()


@then('Я вижу сообщение об успешном создании подкатегории')
def success_message_subcategory(browser):
    assert 'было успешно добавлено' in browser.html
