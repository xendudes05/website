import flask
from flask import jsonify, make_response, request

from datetime import datetime, date

from . import db_session
from .events import Events

blueprint = flask.Blueprint(
    'events_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/events')
def get_events():
    db_sess = db_session.create_session()
    events = db_sess.query(Events).all()
    return jsonify(
        {
            'events':
                [item.to_dict(only=('id', 'title', 'time', 'activity_type', 'mood', 'music'))
                 for item in events]
        }
    )


@blueprint.route('/api/events/<int:events_id>', methods=['GET'])
def get_one_event(events_id):
    db_sess = db_session.create_session()
    events = db_sess.query(Events).get(events_id)
    if not events:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'events': events.to_dict(only=(
                'title', 'time', 'activity_type', 'mood', 'music'))
        }
    )


@blueprint.route('/api/events', methods=['POST'])
def create_events():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['title', 'time', 'activity_type', 'mood', 'music']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    try:
        time = datetime.strptime(request.json.get('time'), '%H:%M').time()
        event_datetime = datetime.combine(date.today(), time)
    except Exception as e:
        return make_response(jsonify({'error': f'Invalid time format: {str(e)}'}), 400)
    db_sess = db_session.create_session()
    events = Events(
        user_id=1,
        title=request.json['title'],
        time=event_datetime,
        activity_type=request.json['activity_type'],
        mood=request.json['mood'],
        music=request.json['music'],
    )
    db_sess.add(events)
    db_sess.commit()
    return jsonify({'id': events.id})


@blueprint.route('/api/events/<int:events_id>', methods=['DELETE'])
def delete_events(events_id):
    db_sess = db_session.create_session()
    events = db_sess.query(Events).get(events_id)
    if not events:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(events)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/events/<int:events_id>', methods=['PUT'])
def edit_jobs(events_id):
    db_sess = db_session.create_session()
    events = db_sess.query(Events).get(events_id)

    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['title', 'time', 'activity_type', 'mood', 'music']):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    for key in ['title', 'time', 'activity_type', 'mood', 'music']:
        if key in request.json:
            if key in ['time']:
                try:
                    time = datetime.strptime(request.json[key], '%H:%M').time()
                    event_datetime = datetime.combine(date.today(), time)
                    setattr(events, key, event_datetime)
                except ValueError:
                    return make_response(jsonify({'error': 'Bad request'}), 400)
            else:
                setattr(events, key, request.json[key])

    db_sess.commit()
    return jsonify({'success': 'OK'})
