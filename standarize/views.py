from .serializers import SensorsSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# TODO : Inherit from a GenericView.
class StandarizerView(APIView):
    """ View to handle sensors'values standarization.
    Provides a POST request, expecting a dictionary of list of values.
    If the arguments are valid, will returned the data standarized using a standard scaler.
    """

    def post(self, request):
        """ Validates and return the standarized input data
        :param request:
        :return: Response with the standarized input data.
        """
        serializer = SensorsSerializer(data={"sensors": request.data})
        if serializer.is_valid():
            # Format in the following way as we don't want the "sensors" original values in the answer.
            serializer_data = serializer.data
            return Response({"success": serializer_data['success'],
                             "result": serializer_data['result']})

        return Response({"success": False, "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
