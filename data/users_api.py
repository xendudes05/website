import flask
from flask import jsonify, make_response, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'email', 'name', 'avatar'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_user(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'users': users.to_dict(only=(
                'email', 'name', 'avatar'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_users():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['email', 'name', 'password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    users = User(
        email=request.json['email'],
        name=request.json['name'],
    )
    users.set_password(request.json['password'])
    db_sess.add(users)
    db_sess.commit()
    return jsonify({'id': users.id})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    elif users.id == 1:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT'])
def edit_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(users_id)

    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['email', 'name', 'password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    elif users.id == 1:
        return make_response(jsonify({'error': 'Bad request'}), 400)

    for key in ['email', 'name', 'password']:
        if key in request.json:
            if key == 'password':
                users.set_password(request.json['password'])
            else:
                setattr(users, key, request.json[key])

    db_sess.commit()
    return jsonify({'success': 'OK'})
