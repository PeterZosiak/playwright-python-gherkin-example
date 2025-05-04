class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("[id='login-username']")
        self.password_input = page.locator("[id='login-passwd']")
        self.login_button = page.locator("[id='login-signin']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.login_button.click()
        self.password_input.fill(password)
        self.login_button.click()