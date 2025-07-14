from http.client import responses

import requests
import pprint


def test_create_short_url():
    site_url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    response = requests.get(
        site_url,
        headers={'Content-Type': 'application/json'}
    )
    assert response.status_code == 200
    assert response.json()[0]['status'] == 'sold'


def test_custom_short_url():
    site_url = 'https://petstore.swagger.io/#/pet/findPetsByStatus'
    response = requests.post(
        'https://gotiny.cc/api',
        headers={'Content-Type': 'application/json'},
        json={'input': site_url}
    )
    assert response.status_code == 200
    assert response.json()[0]['long'] == site_url
    assert response.json()[0]['code'] is not None