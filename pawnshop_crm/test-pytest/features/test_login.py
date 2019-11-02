
from pytest_bdd import scenario, given, then

from pytest_django.fixtures import admin_user, django_user_model, client


@scenario('login.feature', 'Login as admin')
def test_login(live_server):
    return live_server



@then ('Create superuser')
def super_user(admin_user):
    return admin_user

@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url +'/admin')


@then('I logging as admin')
def admin_login(browser):

    password = 'ro'
    client = django_user_model.get(is_superuser=True)
    browser.fill('username', client.username)
    browser.fill('password', password)
    browser.driver.find_element_by_class_name('submit-row').click()




@then('I should see admin page')
def admin_index(browser):
    assert browser.response.status_code == 200
    assert 'Pawnshop' in browser.html

