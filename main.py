from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from Flatmates_Bill import flat
from Tips_Bill import tip

app = Flask(__name__)


class Homepage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform = bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1,days_in_house1)
        flatmate2 = flat.Flatmate(name2,days_in_house2)

        return render_template('results.html',
                               name1 = flatmate1.name,
                               name2 = flatmate2.name,
                               amount1 = flatmate1.pays(the_bill, flatmate2),
                               amount2 = flatmate2.pays(the_bill, flatmate1))

class BillForm(Form):
    amount = StringField(label= 'Bill Amount: ')
    period = StringField(label= 'Bill Period: ')

    name1 = StringField(label='Name:')
    days_in_house1 = StringField(label='Days in the house: ')
    name2 = StringField(label='Name:')
    days_in_house2 = StringField(label='Days in the house: ')

    button = SubmitField("Calculate")


class TipFormPage(MethodView):

    def get(self):
        tip_form = TipForm()
        return render_template('tip_form_page.html', tipform = tip_form)

class TipResultsPage(MethodView):

    def post(self):
        tipform = TipForm(request.form)
        amount = float(tipform.amount.data)
        r_name = tipform.r_name.data

        tip_percent = int(tipform.tip_percent.data)
        person_count = int(tipform.person_count.data)

        the_bill = tip.Bill(amount, r_name)
        count1 = tip.Count(tip=tip_percent,people=person_count)

        return render_template('tipresults.html',
                               r_name = the_bill.r_name,
                               amount1 = count1.pays(the_bill,count1))

class TipForm(Form):

    amount = StringField(label='Bill Amount: ')
    r_name = StringField(label='Restaurant Name: ')

    tip_percent = StringField(label='Tip: ')
    person_count = StringField(label='Number of People: ')

    button1 = SubmitField("Calculate")

app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/billform', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
app.add_url_rule('/tipform', view_func=TipFormPage.as_view('tip_form_page'))
app.add_url_rule('/tipresults', view_func=TipResultsPage.as_view('tip_results_page'))


app.run(debug=True)
