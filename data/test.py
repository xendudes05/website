from requests import get, post, delete, put

# print(get('http://localhost:5000/api/events').json())
# print(get('http://localhost:5000/api/events/1').json())
# # события с id = 999 нет в базе
# print(get('http://localhost:5000/api/events/999').json())
# # неверное значение events_id
# print(get('http://localhost:5000/api/events/q').json())
# # Пустой запрос
# print(post('http://localhost:5000/api/events', json={}).json())
# # Введены не все данные
# print(post('http://localhost:5000/api/events',
#            json={'title': 'Сон'}).json())
# print(post('http://localhost:5000/api/events',
#            json={'music': 'Нет'}).json())
# # Верный запрос
# print(post('http://localhost:5000/api/events',
#            json={'title': 'Подъём',
#                  'time': '10:00',
#                  'activity_type': 'Умывание',
#                  'mood': 'Собранность',
#                  'music': 'Бодрая'}).json())
# # событий с такими id нет в базе
# print(delete('http://localhost:5000/api/events/999').json())
# print(delete('http://localhost:5000/api/events/998').json())
# print(delete('http://localhost:5000/api/events/997').json())
# print(delete('http://localhost:5000/api/events/996').json())
# # Верный запрос
# print(delete('http://localhost:5000/api/events/1').json())
# # события с id = 999 нет в базе
# print(put('http://localhost:5000/api/events/999',
#           json={"title": "Подъём",
#                 "activity_type": 'Умывание'}).json())
# # Пустой запрос
# print(put('http://localhost:5000/api/events/1', json={}).json())
# # Неверный формат даты
# print(put('http://localhost:5000/api/events/1',
#           json={"time": "20-03-2025 12:00:00"}).json())
# # Верный запрос
# print(put('http://localhost:5000/api/events/2',
#           json={'title': 'Подъём',
#                 'time': '9:00',
#                 'activity_type': 'Купание',
#                 'mood': 'Собранность',
#                 'music': 'Бодрая'}).json())
# print(get('http://localhost:5000/api/events').json())

# print(get('http://localhost:5000/api/users').json())
# print(get('http://localhost:5000/api/users/1').json())
# # пользователя с id = 999 нет в базе
# print(get('http://localhost:5000/api/users/999').json())
# # неверное значение users_id
# print(get('http://localhost:5000/api/users/q').json())
# # Пустой запрос
# print(post('http://localhost:5000/api/users', json={}).json())
# # Введены не все данные
# print(post('http://localhost:5000/api/users',
#            json={'email': 'dsfsdfsdf@gmail.com'}).json())
# print(post('http://localhost:5000/api/users',
#            json={'name': 'User'}).json())
# # Верный запрос
# print(post('http://localhost:5000/api/users',
#            json={'email': 'sadasdasd@gmail.com',
#                  'name': 'User',
#                  'password': '12345678'}).json())
# # пользователей с такими id нет в базе
# print(delete('http://localhost:5000/api/users/999').json())
# print(delete('http://localhost:5000/api/users/998').json())
# print(delete('http://localhost:5000/api/users/997').json())
# print(delete('http://localhost:5000/api/users/996').json())
# # Верный запрос
# print(delete('http://localhost:5000/api/users/2').json())
# # события с id = 999 нет в базе
# print(put('http://localhost:5000/api/users/999',
#           json={"email": "sdfsdfsdf@gmail.com",
#                 "name": 'User'}).json())
# # Пустой запрос
# print(put('http://localhost:5000/api/users/2', json={}).json())
# Верный запрос
print(put('http://localhost:5000/api/users/2',
          json={'email': 'sdfsdfsdf@gmail.com',
                'name': 'User',
                'password': '12345678'}).json())
print(get('http://localhost:5000/api/users').json())
