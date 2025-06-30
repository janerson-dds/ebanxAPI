from app.api.dto.event import Event


class AccountService:
    def __init__(self):
        self.accounts: dict[str, int] = {}

    def reset_state(self):
        self.accounts.clear()

    def get_balance(self, account_id: str):
        return self.accounts.get(account_id, "0")

    def handle_event(self, event: Event):
        if event.origin not in self.accounts and event.type != 'deposit':
            return None

        match event.type:
            case 'deposit':
                current_balance = self.accounts.get(event.destination, 0)
                self.accounts[event.destination] = current_balance + event.amount

                return {"destination": {"id": event.destination, "balance": self.accounts[event.destination]}}
            case 'withdraw':
                self.accounts[event.origin] -= event.amount

                return {"origin": {"id": event.origin, "balance": self.accounts[event.origin]}}
            case 'transfer':
                self.accounts[event.origin] -= event.amount
                current_destination_balance = self.accounts.get(event.destination, 0)
                self.accounts[event.destination] = current_destination_balance + event.amount

                return {
                    "origin": {"id": event.origin, "balance": self.accounts[event.origin]},
                    "destination": {"id": event.destination, "balance": self.accounts[event.destination]}
                }
