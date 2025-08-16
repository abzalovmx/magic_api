from http.client import responses
import pprint
from endpoints.create_url_endpoint import CreateUrlEndpoint


def test_create_short_url(url_creator_endp):
    url_creator_endp.create_short_url_for_long_url(long_url='https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    url_creator_endp.check_response_status_is_ok()
    url_creator_endp.check_status_is_available()
    url_creator_endp.check_code_is_not_empty()


def test_custom_short_url(url_creator_endp):
    site_url = 'https://petstore.swagger.io/#/pet/findPetsByStatus'
    response = requests.post(
        'https://gotiny.cc/api',
        headers={'Content-Type': 'application/json'},
        json={'input': site_url}
    )
    assert response.status_code == 200
    assert response.json()[0]['long'] == site_url
    assert response.json()[0]['code'] is not None



# 57-09