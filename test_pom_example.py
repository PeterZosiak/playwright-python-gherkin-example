import pytest
import os

from playwright.sync_api import Page, expect
from models.login_page import LoginPage
from models.home_page import HomePage
from models.components.sidebar_component import SidebarComponent, SidebarFolder
from models.components.composer_component import ComposerComponent
from models.components.mail_item_component import MailItemComponent

subject = "AOL Mail Automation Tests"
attachemnt = 'fixtures/img.jpg'

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    # Arrange
    page.goto("https://mail.aol.com")
    yield

def test_compose_and_send_email(page: Page):
    # Act
    login_page = LoginPage(page)
    login_page.login(os.environ['AOLUSER'], os.environ['AOLPASSWORD'])

    home_page = HomePage(page)
    expect(home_page.logo).to_be_visible()

    composer = ComposerComponent(page)
    composer.compose_email(os.environ['AOLRECIPIENT'], subject, attachemnt)
    page.wait_for_timeout(10000)

    # Assert
    sidebar = SidebarComponent(page)
    sidebar.navigate_to_folder(SidebarFolder.SENT)

    sent_email = MailItemComponent(page, 0)
    expect(sent_email.item).to_be_visible()

    