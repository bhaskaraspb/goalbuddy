import web
from web import form

def make_text(string):
    return string

urls = ('/', 'tutorial')

app = web.application(urls, globals())

render = web.template.render('templates/')

my_form = form.Form(
    form.Textbox('username'),
    form.Password('password'),
    form.Button('Login')
)

class tutorial(object):
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Sample text.")
    
    def POST(self):
		form = my_form()
		form.validates()
		s = form.value['textfield']
		return make_text(s)

if __name__ == "__main__":
    app.run()