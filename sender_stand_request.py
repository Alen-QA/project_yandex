
# Алена Саврасова, 7-я когорта - Финальный проект. Инженер по тестированию плюс

import requests
import configuration as c
import data as d


# Функция создания заказа
def new_order():
    current_order = requests.post(c.URL_SERVICE + c.CREATE_ORDER_PATH,
                                  json=d.order_body)
    return current_order.json()['track']


num_track = new_order()  # сохранение номера трека заказа
print(num_track)


# Запрос на получение заказа по номеру трека заказа
def get_order_by_track(track):
    params = d.params.copy()
    params['t'] = track
    return requests.get(c.URL_SERVICE + c.GET_ORDER_PATH,
                        params=params)


response = get_order_by_track(num_track)
assert response.status_code == 200  # проверка кода ответа 200
print(response.status_code)
