import web
from ex52 import map

urls = (
        '/game', 'GameEngine',
        '/', 'Index'
        )

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.Diskstore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web_config._session = session
else:
    session = web.config._session

class Index(object):
    def GET(self):
        # This is used to setup the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # Why is there here? Do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)
        # There is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
