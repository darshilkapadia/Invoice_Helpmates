class Bill:
    """
    Tip Calculator
    """

    def __init__(self, amount, r_name):
        self.amount = amount
        self.r_name = r_name


class Count:
    """
    Head count
    """

    def __init__(self, tip, people):
        self.tip = tip
        self.people = people

    def pays(self, bill, tip1):
        tips = self.tip / 100
        final_tip = bill.amount * tips
        final_bill = bill.amount + final_tip
        to_pay = final_bill / self.people
        return "{:.2f}".format(to_pay)