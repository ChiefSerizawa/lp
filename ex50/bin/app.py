import web

urls = ('/index', 'Index', '/hello', 'Hello')
app = web.application(urls, globals())
render = web.template.render('templates/', base = 'layout')

class Index(object):
    def GET(self):
        return render.index()

    def POST(self):
        return render.index()

class Hello(object):

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s %s" % (form.greet, form.name)
        return render.hello(greeting = greeting)


if __name__ == '__main__':
    app.run()

