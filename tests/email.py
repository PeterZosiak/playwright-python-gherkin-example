import pytest
import os, time
from playwright.sync_api import *
from pytest_bdd import scenarios, given, when, then

from models.login_page import LoginPage
from models.home_page import HomePage
from models.components.sidebar_component import SidebarComponent, SidebarFolder
from models.components.composer_component import ComposerComponent
from models.components.mail_item_component import MailItemComponent


@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

scenarios ('../features/email.feature')

@given('I am logged in as a valid "{user}" user with password "{password}"')
def login(login_page: LoginPage, home_page: HomePage, user, password):
    os.environ[user]
    login_page = LoginPage(login_page)
    login_page.login(os.environ[user], os.environ[password])

    home_page = HomePage(home_page)
    expect(home_page.logo).to_be_visible()

@when('I send an email to "{recipient}" with the subject "{subject}" and attach a file named "{attachment}"')
def send_email(composer: ComposerComponent, recipient, subject, attachment):
    composer = ComposerComponent(composer)
    composer.compose_email(os.environ[recipient], subject, attachment)
    time.sleep(10)

@then('I should see sent email in SENT folder')
def verify_sent_email(page: Page, sidebar: SidebarComponent):
    sidebar = SidebarComponent(page)
    sidebar.navigate_to_folder(SidebarFolder.SENT)

    sent_email = MailItemComponent(page, 0)
    expect(sent_email.item).to_be_visible()