from flask import Flask, render_template, redirect, abort, request, make_response, jsonify
from data import db_session
from data.events import Events
from data.users import User
from form.user import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from form.loginform import LoginForm
from form.events import EventsForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    events = db_sess.query(Events)
    return render_template("index.html", events=events)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# @app.route('/events', methods=['GET', 'POST'])
# @login_required
# def add_events():
#     form = EventsForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         events = Events()
#         events.title = form.title.data
#         events.time = form.time.data
#         events.activity_type = form.activity_type.data
#         events.mood = form.mood.data
#         events.music = form.music.data
#         current_user.events.append(events)
#         db_sess.merge(current_user)
#         db_sess.commit()
#         return redirect('/')
#     return render_template('events.html', title='Добавление события',
#                            form=form)
#
#
# @app.route('/events/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_events(id):
#     form = EventsForm()
#     if request.method == "GET":
#         db_sess = db_session.create_session()
#         events = db_sess.query(Events).filter(Events.id == id,
#                                           Events.user == current_user
#                                           ).first()
#         if events:
#             form.title.data = events.title
#             form.time.data = events.time
#             form.activity_type.data = events.activity_type
#             form.mood.data = events.mood
#             form.music.data = events.music
#         else:
#             abort(404)
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         events = db_sess.query(Events).filter(Events.id == id,
#                                           Events.user == current_user
#                                           ).first()
#         if events:
#             events.title = form.title.data
#             events.time = form.time.data
#             events.activity_type = form.activity_type.data
#             events.mood = form.mood.data
#             events.music = form.music.data
#             db_sess.commit()
#             return redirect('/')
#         else:
#             abort(404)
#     return render_template('events.html',
#                            title='Редактирование события',
#                            form=form
#                            )
#
#
# @app.route('/events_delete/<int:id>', methods=['GET', 'POST'])
# @login_required
# def events_delete(id):
#     db_sess = db_session.create_session()
#     events = db_sess.query(Events).filter(Events.id == id,
#                                       Events.user == current_user
#                                       ).first()
#     if events:
#         db_sess.delete(events)
#         db_sess.commit()
#     else:
#         abort(404)
#     return redirect('/')
#
#
def main():
    db_session.global_init("db/days.db")
    # app.register_blueprint(events_api.blueprint)
    app.run()
#
#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)
#
#
# @app.errorhandler(400)
# def bad_request(_):
#     return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    main()
