class Employee:
    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@dundermifflin.com'.format(self.first_name.lower(), self.last_name.lower())

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
