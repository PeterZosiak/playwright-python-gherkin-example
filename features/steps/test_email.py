import pytest # Import pytest
import os, time
from playwright.sync_api import *
from pytest_bdd import parsers, scenarios, given, when, then

from models.login_page import LoginPage
from models.home_page import HomePage
from models.components.sidebar_component import SidebarComponent, SidebarFolder
from models.components.composer_component import ComposerComponent
from models.components.mail_item_component import MailItemComponent

@pytest.fixture(scope="function")
def login_page(page: Page):
    page.goto("https://mail.aol.com")
    return LoginPage(page)

@pytest.fixture(scope="function")
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture(scope="function")
def composer(page: Page):
    return ComposerComponent(page)

@pytest.fixture(scope="function")
def sidebar(page: Page):
    return SidebarComponent(page)


@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


scenarios ('email.feature')

@given('I am logged in as a valid user')
def login_without_credentials(login_page: LoginPage, home_page: HomePage):
    username = os.environ['AOLUSER'] 
    pwd = os.environ['AOLPASSWORD']

    login_page.login(username, pwd)
    expect(home_page.logo).to_be_visible()

@given(parsers.parse('I am logged in as a valid {user} user with password {password}'))
def login(login_page: LoginPage, home_page: HomePage, user, password):
    username = os.environ[user] 
    pwd = os.environ[password]

    login_page.login(username, pwd)
    expect(home_page.logo).to_be_visible()

@when(parsers.parse('I send an email to {recipient} with the subject {subject} and attach a file named {attachment}'))
def send_email(composer: ComposerComponent, recipient, subject, attachment):
    recipient_email = os.environ[recipient]
    composer.compose_email(recipient_email, subject, attachment)
    time.sleep(10)

@then('I should see sent email in SENT folder')
def verify_sent_email(page: Page, sidebar: SidebarComponent):
    sidebar.navigate_to_folder(SidebarFolder.SENT)

    sent_email = MailItemComponent(page, 0) 
    expect(sent_email.item).to_be_visible()