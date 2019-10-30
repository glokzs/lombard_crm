import pytest
from pytest_bdd import scenario, given, then
from django.contrib.auth.models import User

password = 'ro'
@scenario('login.feature', 'Login as admin')
def test_login():
    pass

@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url +'/admin')


@pytest.fixture(scope="session", autouse=True)


# def admin_client(db, admin_user):
#     """A Django test client logged in as an admin user."""
#     from django.test.client import Client
#
#     client = Client()
#     client.login(username=admin_user.username, password="password")
#     return client




# @then('Create superuser')
# def new_user(admin_user=None):
    # admin_user.objects.create(username="someone", password="something")
    # admin_user.is_staff = True
    # admin_user.is_superuser = True
    # admin_user.username()
    # admin_user.password()
    # username ='ro'
    # password ='ro'
    # adminuser.save()
    # admin_user.save()


# def create_admin(**kwargs):
# adminuser = create_admin(**kwargs)
    # adminuser.username('ro')
    # adminuser.is_staff = True
    # adminuser.is_staff = True
    # adminuser.save()

# @pytest.mark.django_db
@then('I logging as admin')
def create_admin_login(browser):
    browser.fill('username', 'ro')
    browser.fill('password', 'ro')
    browser.driver.find_element_by_class_name('submit-row').click()

@then('I should see admin page')
def admin_login(browser):
    assert 'PAWNSHOP' in browser.html

@pytest.mark.django_db(transaction=True)
def access_db():
    pass

@then('Click on user model')
def click_user_model(browser):
    assert 'ПОЛЬЗОВАТЕЛИ И ГРУППЫ' in browser.html


# browser.visit(live_server.url +'/admin')

