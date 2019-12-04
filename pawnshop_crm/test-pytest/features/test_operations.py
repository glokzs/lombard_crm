import factory
from pytest_factoryboy import register

from pawnshop.models import Client, ConfirmDocument, Category, Subcategory, PledgeItem, Loan

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


@register
class LoanFactory(factory.Factory):
    class Meta:
        model = Loan

    pk = '1'
    client = factory.SubFactory(ClientFactory)
    client_amount = '10000'
    duration = '12'
    date_of_expire = '2019-10-29'
    warranty_date = '2019-11-29'
    total_amount = '11355'
    status = 'STATUS_EXPIRED'
    created_at = '2019-10-16'


@register
class PledgeItemFactory(factory.Factory):
    class Meta:
        model = PledgeItem

    pk = "1"
    loan = factory.SubFactory(LoanFactory)
    category = factory.SubFactory(CategoryFactory)
    subcategory = factory.SubFactory(SubcategoryFactory)
    name = 'Test pledge item'
    price = '100000'
    description = "test description"
    note = 'same new test'


@scenario('operations.feature', 'Operations')
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


@given('Loan')
def test_loan():
    loan = LoanFactory.build()
    loan.save()
    return loan


@given('PledgeItem')
def test_pledgeitem():
    pledgeitem = PledgeItemFactory.build()
    pledgeitem.save()
    return pledgeitem


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


@then('I click "Займы"')
def click_loans(browser):
    browser.driver.find_element_by_link_text('Займы').click()


@then('I should see test loan')
def see_test_loan(browser):
    assert '1' in browser.html


@then('click on test loan')
def click_loan_detail(browser):
    browser.driver.find_element_by_link_text('Детали').click()


@then('I should see detail loan page')
def see_loan_detail(browser):
    assert 'Тест' in browser.html


@then('I click on "Продление"')
def credit_buyout(browser):
    browser.driver.find_element_by_xpath(
        '/html/body/section/div/div/div/div[1]/button[2]').click()


@then('I should see and fill in prolongation loan option')
def prolong(browser):
    from time import sleep
    sleep(0.9)
    browser.driver.find_element_by_name('prolongation_duration').click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
    #                                                             '//*[@id="prolongation_duration_input"]'))).click()
    browser.fill('prolongation_duration', '12')
    sleep(0.3)
    browser.driver.find_element_by_xpath(
        '// *[ @ id = "prolongation_button"]').click()


@then('I click close loan option')
def credit_close(browser):
    from time import sleep
    sleep(0.9)
    browser.driver.find_element_by_xpath(
        '/html/body/section/div/div/div/div[1]/button[1]').click()


@then('I click close button')
def push_credit_close(browser):
    from time import sleep
    sleep(0.9)
    browser.driver.find_element_by_link_text('Выкуп').click()


@then('I click to the "Журнал операций"')
def click_on_operation_list(browser):
    from time import sleep
    sleep(0.9)
    browser.driver.find_element_by_link_text('Журнал операций').click()


@then('I should see list of made operations')
def see_operations(browser):
    from time import sleep
    sleep(4)
    assert "Пролонгация займа" in browser.html
    assert "Выкуп займа" in browser.html
