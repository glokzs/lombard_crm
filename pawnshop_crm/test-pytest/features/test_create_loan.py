import factory
from pytest_factoryboy import register

from pawnshop.models import Client, ConfirmDocument, Category, Subcategory

from pytest_bdd import scenario, given, then


@register
class ClientFactory(factory.Factory):
    class Meta:
        model = Client

    pk = '1'
    first_name = 'Test'
    last_name = 'Тест'
    middle_name = 'Ivanovich'
    birth_date = '1999-05-10'
    location = 'Алматы'
    street = 'Достык'
    house_number = '47'
    apartment_number = '21'
    actual_address = 'Талгар'
    birth_place = 'Казахстан'
    phone = '77059056487'
    email = 'Ivan@gmail.com'
    citizenship = 'Казахстан'


@register
class ConfirmDocumentFactory(factory.Factory):
    class Meta:
        model = ConfirmDocument

    pk = '1'
    client = factory.SubFactory(ClientFactory)
    document_type = "Паспорт"
    iin = '909090909'
    serial_number = '9090090909'
    given_by = 'Мин Юст'
    given_at = '1999-09-09'


@register
class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    pk = '1'
    name = 'test_category'
    interest_rate = '0.9'


@register
class SubcategoryFactory(factory.Factory):
    class Meta:
        model = Subcategory

    pk = '1'
    category = factory.SubFactory(CategoryFactory)
    name = 'test_subcategory'


@scenario('create_loan.feature', 'Create loan')
def test_login(live_server):
    return live_server


@given('Client')
def test_client():
    client = ClientFactory.build()
    client.save()
    return client


@given('Client document')
def test_document():
    document = ConfirmDocumentFactory.build()
    document.save()
    return document


@given('Category')
def test_category():
    category = CategoryFactory.build()
    category.save()
    return category


@given('Subcategory')
def test_subcategory():
    subcategory = SubcategoryFactory.build()
    subcategory.save()
    return subcategory


@given('Create superuser')
def super_user(admin_user):
    return admin_user


@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url + '/accounts/login/')


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
def check_client_choose(browser):
    assert 'Выбор клиента' in browser.html


@then('I click on client')
def click_on_client(browser, client):
    browser.fill('client_search_input', 'Тест')
    from time import sleep
    sleep(1)
    browser.driver.find_element_by_xpath('/html/body/section/div/div/div[1]/div/div[1]/div[1]/div/div[1]/span').click()


@then('I click to choose client')
def choose_client(browser):
    browser.driver.find_element_by_css_selector('#client_choose_btn').click()


@then('I should see "Добавить займ"')
def check_add_loan(browser):
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
    select_elem = browser.driver.find_element_by_name('subcategory')
    select_elem.click()
    options = select_elem.find_elements_by_tag_name('option')
    options[len(options) - 1].click()
    browser.fill('name', 'test')
    browser.fill('price', '100000')
    browser.fill('description', 'new')
    from time import sleep
    sleep(0.5)
    browser.driver.find_element_by_css_selector("#pledge_item_create_button").click()


@then('I should see "Добавить займ"')
def should_see_add_credit(browser):
    assert 'Добавить займ' in browser.html


@then('I add loan sum, duration, warranty period')
def add_loan_usm_duration_warranty(browser):
    browser.fill('client_amount', '10000')
    browser.fill('duration', '10')
    browser.fill('warranty_date', '20.11.2019')
    from time import sleep
    sleep(0.5)
    browser.driver.find_element_by_xpath('/html/body/section/div/div[2]/form/div[5]/button').click()


@then('I should see "Кредит"')
def should_see_credit(browser):
    assert 'Кредит' in browser.html


@then('I click on "Выкуп"')
def credit_buyout(browser):
    browser.driver.find_element_by_xpath(
        '/html/body/section/div/div/div/div[1]/button[1]').click()
    from time import sleep
    sleep(0.9)
