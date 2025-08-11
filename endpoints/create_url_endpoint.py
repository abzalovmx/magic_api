import requests

class CreateUrlEndpoint:
    status_code = None
    status = None
    name = None
    sent_url = None

    def create_short_url_for_long_url(self, long_url, code=None):
        if code:
            pass
        else:
            response = requests.get(
                'https://petstore.swagger.io/v2/pet/findByStatus?status=available', verify=False
            )
        self.sent_url = long_url
        self.status_code = response.status_code
        self.status = response.json()[0]['status']
        self.name = response.json()[0]['name']
        return response

    def check_response_status_is_ok(self):
        return self.status_code == 200

    def check_code_is_not_empty(self):
        assert len(self.sent_url) > 0

    def check_status_is_available(self):
        assert self.status == 'available'

res = CreateUrlEndpoint()
print(res.create_short_url_for_long_url('https://petstore.swagger.io/v2/pet/findByStatus?status=available').json())
