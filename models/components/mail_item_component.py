class MailItemComponent:
    def __init__(self, page, index: int = 0):
        self.page = page
        self.index = index
        self.item = page.locator('[data-test-id="message-list-item"]').nth(index)