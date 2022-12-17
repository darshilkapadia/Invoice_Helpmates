from flask.views import MethodView
from wtforms import Form
from flask import Flask, render_template

app = Flask(__name__)

class Homepage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        return render_template('bill_form_page.html')


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass

app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/billform', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)
