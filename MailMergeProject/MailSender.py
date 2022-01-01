class MailSender:
    def __init__(self):
        self.names = []
        self.templateData = ""
        self.fetchAllInvitees()
        self.mailTemplate()

    def fetchAllInvitees(self):
        with open("./Input/Names/invited_name.txt") as file:
            contents = file.read()
            self.names = contents.splitlines()

    def mailTemplate(self):
        with open("./Input/Letters/starting_letters.txt") as file:
            self.templateData = file.read()

    def prepareMailLetters(self):
        for invitee in self.names:
            modified_text = self.templateData.replace('[name]', invitee)
            with open(f"./Output/ReadyToSend/readyToSend_{invitee}.txt", mode='w') as file:
                file.write(modified_text)
