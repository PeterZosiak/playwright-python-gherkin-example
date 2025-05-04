from enum import Enum

class SidebarComponent:
    def __init__(self, sidebar):
        self.sidebar = sidebar
        self.compose_button = sidebar.locator('[data-test-id="compose-button"]')
        self.navigation = sidebar.locator('[data-test-id="navigation"]')
        self.inbox_folder_button = sidebar.locator('[data-test-folder-name="Inbox"]')
        self.unread_folder_button = sidebar.locator('[data-test-smartview-type="UNREAD"]')
        self.sent_folder_button = sidebar.locator('[data-test-folder-name="Sent"]')

    def componse_new_email(self):
        self.compose_button.click()

    def navigate_to_folder(self, folder_name):
        match folder_name:
            case SidebarFolder.INBOX:
                self.inbox_folder_button.click()
            case SidebarFolder.UNREAD:
                self.unread_folder_button.click()
            case SidebarFolder.SENT:
                self.sent_folder_button.click()
            case _:
                raise ValueError(f"Unknown folder name: {folder_name}")

    
class SidebarFolder(Enum):
    INBOX = "Inbox"
    UNREAD = "Unread"
    SENT = "Sent"