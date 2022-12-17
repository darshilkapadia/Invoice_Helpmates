from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

app = Flask(__name__)

class Homepage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform = bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        return amount

class BillForm(Form):
    amount = StringField(label= 'Bill Amount: ')
    period = StringField(label= 'Bill Period: ')

    name1 = StringField(label='Name:')
    days_in_house1 = StringField(label='Days in the house: ')
    name2 = StringField(label='Name:')
    days_in_house2 = StringField(label='Days in the house: ')

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/billform', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))


app.run(debug=True)
