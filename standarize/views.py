from rest_framework.response import Response
from rest_framework.views import APIView

from sklearn.preprocessing import StandardScaler


# TODO : Use a Serializer, Inherit from a GenericView.
class Standarizer(APIView):
    """ Standardize input value
    Expected arguments : Provides 1+ list (of equal sizes)
    """

    def post(self, request):
        """ validates and return the standarized input data
        :param request:
        :return: Response with the standarized input data.
        """
        sensors_values = list(request.data.values())
        sensors_keys = list(request.data.keys())

        # Check all are list
        for sensor_values in sensors_values:
            if not isinstance(sensor_values, list):
                return Response({"success": False, "result": "All components must be of type 'list'"})
        # check their length
        if len({len(l) for l in sensors_values}) != 1:
            return Response({"success": False, "result": "All lists must be of same length"})

        scl = StandardScaler()
        transformed_values = scl.fit_transform(sensors_values)

        result = dict(zip(sensors_keys, transformed_values))

        return Response({"success": True, "result": result})
