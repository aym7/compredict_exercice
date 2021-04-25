from django.urls import reverse
from sklearn.preprocessing import StandardScaler
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status


class TestStandarize(APITestCase):
    def setUp(self):
        """ Prepares the data required for the tests (url, sensor, standardScaler, ...)
        """
        self.sensors = {"sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
                        "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
                        "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]}
        self.sensors_values = list(self.sensors.values())
        self.scl = StandardScaler()
        self.scl.fit(self.sensors_values)
        self.url = reverse("standarize")

    def test_request(self):
        """ Tests the standarize's requests
        Test if the requests answers and if the parameter's validation is valid
        """
        # Correct test. We've sent the valid requirements.
        rsp = self.client.post(self.url, self.sensors, format="json")
        self.assertEqual(rsp.status_code, status.HTTP_200_OK)
        self.assertTrue(rsp.data['success'])

        # Test error : at least one element is not a list
        rsp = self.client.post(self.url, {"false_sensor": "hello world",
                                          "sensor1": [5.45, 2.787]
                                          }, format="json")
        self.assertFalse(rsp.data['success'])

        # Test error : One of the list doesn't have the same length as the other
        rsp = self.client.post(self.url, {"sensor1": [1.5454, 5465465.54],
                                          "sensor2": [5.45, 2.787, 454.21],
                                          "sensor3": [5.45, 2.787]
                                          }, format="json")
        self.assertFalse(rsp.data['success'])

    def test_standarization(self):
        """ Tests the standarization's validity.
        """
        rsp = self.client.post(self.url, self.sensors, format="json")
        self.assertTrue(rsp.data['success'])
        # If the standarization is valid, inversing it should return the original data.
        result_values = list(rsp.data['result'].values())
        inverse = self.scl.inverse_transform(result_values)
        # It seems as inversing it adds unnecessary "noise" : eg 5.440000000000055 instead of 5.44
        # Therefore, needs to round the content of 'inverse' to 2-3 decimals
        # Converts it to list as inverse_transform returns a ndarray
        inverse = inverse.round(decimals=3).tolist()
        for i, j in zip(inverse, self.sensors_values):
            self.assertListEqual(i, j)
