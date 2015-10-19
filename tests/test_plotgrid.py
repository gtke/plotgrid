import requests
import httpretty
import unittest

from sure import expect


class PlotGridTestCase(unittest.TestCase):
    @httpretty.activate
    def test_ping(self):
        httpretty.register_uri(httpretty.GET,
                                "https://plotgrid.herokuapp.com/ping",
                                body='[{"status": "alive"}]',
                                content_type="application/json",
                                status=200)

        response = requests.get('https://plotgrid.herokuapp.com/ping')
        expect(response.json()).to.equal([{"status": "alive"}])
        expect(response.status_code).to.equal(200)

    @httpretty.activate
    def test_data(self):
        httpretty.register_uri(httpretty.GET,
                                "https://plotgrid.herokuapp.com/data",
                                body='[{"value": "100"}]',
                                content_type="application/json",
                                status=200)

        response = requests.get('https://plotgrid.herokuapp.com/data')
        expect(response.json()).to.equal([{"value": "100"}])
        expect(response.status_code).to.equal(200)


if __name__ == '__main__':
    unittest.main()
