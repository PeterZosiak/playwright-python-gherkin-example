from models.components.sidebar_component import SidebarComponent

class ComposerComponent:
    def __init__(self, page):
        self.page = page
        self.wrapper = page.locator('[data-test-id="compose-styler"]')
        self.to_input = self.wrapper.locator('[id="message-to-field"]')
        self.subject_input = self.wrapper.locator('[id="compose-subject-input"]')
        self.insert_image_input = self.wrapper.locator('[data-test-id="icon-btn-insert-picture"] + input')
        self.send_button = self.wrapper.locator('[data-test-id="compose-send-button"]')

    def compose_email(self, to, subject, attachment):
        sidebar = SidebarComponent(self.page)
        sidebar.compose_button.click()

        self.to_input.fill(to)
        self.subject_input.fill(subject)

        self.insert_image_input.set_input_files(attachment)
        # Wait for the attachment to be added
        self.page.wait_for_timeout(2000)

        self.send_button.click()