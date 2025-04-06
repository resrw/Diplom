import configuration
import data
import requests

# создание заказа
def post_new_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=order_body,
                         headers=data.headers)

# получение данных о заказе по треку
def get_order_data_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_TRACK_ORDERS + str(track),
                            headers=data.headers)