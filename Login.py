from robobrowser import RoboBrowser
import pandas as pd
# form===>'id'= 'new-login-form'
#name ====> 'id' = 'edit-name'
#password ===> 'id' = 'edit-pass-wrapper'
#loginbutton ===> 'id' = 'edit-submit'
rb = RoboBrowser()
url = 'https://www.codechef.com/'
rb.open(url)

forms = rb.get_forms()
form = forms[1]
form['code'] = '23456'
form['month'] = 'august'
form['day'] = '21'
form['year'] = '2019'
rb.submit_form(form)

html = str(rb.parsed)
data = pd.read_html(html)[0]
