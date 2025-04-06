# Геннадий Боев, 28-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

# Тест
def test_get_order_data_by_track():
    track = sender_stand_request.post_new_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_data_by_track(track)
    assert response.status_code == 200