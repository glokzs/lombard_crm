import pytest
from django.test import Client

from pytest_bdd import scenario, given, then

from django.contrib.auth.models import User
from pytest_django.fixtures import admin_user, django_user_model, client

# pytestmark = pytest.mark.django_db

@scenario('login.feature', 'Login as admin')
def test_login():
    pass


@given('Login page')
def go_to_login_page(browser, live_server):
    browser.visit(live_server.url +'/admin')



# @then('Taking out superuser from db')
# def get_admin_user():
#     superusers = User.objects.filter(is_superuser=True)
#     superuser = superusers.first()
#     return superuser

# @then('Taking out superuser from db')
# def get_admin_user():
#     superuser = admin_user(, django_user_model=User )
#     print (superuser)
#     print('asdasd')
#     return superuser

            # return superuser

# @pytest.fixture(scope="session", autouse=True)


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


#
@then ('Create superuser')
def super_user( django_user_model):
    username = 'ro'
    password = 'ro'
    user = django_user_model.objects.create_user(
        username=username,
        password=password,
        first_name='ro',
        last_name='ro',
        is_staff=True,
        is_superuser=True
    ).save()
    return user




@then('I logging as admin')
def admin_login(browser):
    # clients = User.objects.all()
    # print(clients)
    password = 'ro'
    client = django_user_model.get(is_superuser=True)
    browser.fill('username', client.username)
    browser.fill('password', password)
    browser.driver.find_element_by_class_name('submit-row').click()
    assert browser.status_code == 200




@then('I should see admin page')
def admin_index(browser):
    assert 'PAWNSHOP' in browser.html

# # @pytest.mark.django_db(db=True)
# @then('Click on user model')
# def click_user_model(browser):
#     assert 'ПОЛЬЗОВАТЕЛИ И ГРУППЫ' in browser.html
#

# browser.visit(live_server.url +'/admin')

