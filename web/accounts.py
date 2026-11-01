from dataclasses import dataclass
@dataclass
class Membership:
    nickname: str
    mailbox: str
    secret_hash: str
class Accounts:
    def __init__(self):
        self.members = []
    def exists(self, email):
        return self.find(email) is not None
    def insert(self, name, email, password_hash):
        self.members.append(Membership(name, email.casefold(), password_hash))
    def find(self, email):
        member = next((m for m in self.members if m.mailbox == email.casefold()), None)
        return {'name': member.nickname, 'hash': member.secret_hash} if member else None
