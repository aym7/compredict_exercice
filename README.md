# Sensors standarizer

The following deposit contains a Django + DjangoRestFramework application.
Its purpose is to standarize sensors data

## Preparing and launching the project and tests

Installing the requirements :

```
$> pip install -r requirements.txt
```

Running the server :

```
$> python manage.py runserver
```

Running the test :

```
$> python manage.py test
```

You can then test the endpoint by going on the http://127.0.0.1:8000/standarize/ page.

Request works in POST mode.

Expected input should be formatted as follow :
```json
{
	"sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
	"sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
	"sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]
}
```

### Details on the project's architecture

/standarize is handled in a separated app (`standarize`).
The view StandarizerView inherits from `APIView` and uses a serializer `SensorsSerializer`.
