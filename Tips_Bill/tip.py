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

    def __init__(self, tip_percent, person_count):
        self.tip_percent = tip_percent
        self.person_count = person_count

    def pays(self, bill, tip1):
        tips = self.tip_percent / 100
        final_tip = bill.amount * tips
        final_bill = bill.amount + final_tip
        to_pay = final_bill / self.person_count
        return "{:.2f}".format(to_pay)