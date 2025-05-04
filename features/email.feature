Feature: Email Feature
    As a valid user
    I want to be able to send emails with attachments
    So that I can share files with my colleagues

    Scenario: Send email with attachment
        Given I am logged in as a valid "AOLUSER" user with password "AOLPASSWORD"
        When I send an email to <recipient> with the subject <subject> and attach a file named <attachment>
        Then I should see sent email in SENT folder

        Examples:
            | recipient    | subject              | attachment       |
            | AOLRECIPIENT | PlaywrightAutomation | fixtures/img.jpg |