from rest_framework import serializers
from rest_framework.fields import ListField, DictField

from sklearn.preprocessing import StandardScaler


class SensorsSerializer(serializers.Serializer):
    """ Serializer to handle sensor data.
    """
    sensors = DictField(child=ListField(child=serializers.FloatField()))

    success = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()

    def get_result(self, validated_data):
        """Computes the result using standard scaling
        :param validated_data: Our serializer's data.
        :return: Datas from our sensors standarized using sklearn's StandardScaler
        """
        sensors_values = list(validated_data['sensors'].values())
        sensors_keys = list(validated_data['sensors'].keys())
        scl = StandardScaler()

        transformed_values = scl.fit_transform(sensors_values)
        return dict(zip(sensors_keys, transformed_values))

    def get_success(self, validated_data):
        return self.is_valid()

    def validate(self, params_data):
        """ Custom validation for 'sensors'. Ensures that all lists in the dictionary have the same length.
        NB : We don't need to check if it's a dictionary of list of float as the serializer automatically checks it.
        :param params_data: data to validate
        :return: The data if validated
        :raise: serializers.ValidationError
        """
        sensors_values = list(params_data['sensors'].values())
        unique_lens = {len(sensor) for sensor in sensors_values}
        # If the set created has a length > 1, it means that there was at least 2 list of different length
        if len(unique_lens) != 1:
            raise serializers.ValidationError('All lists must be of same length.')
        if 0 in unique_lens:
            raise serializers.ValidationError('Empty lists are not allowed.')

        return params_data

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
