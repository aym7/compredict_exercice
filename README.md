# Compredict exercice

The following deposit contains the code required for compredict recruitment, phase 2.

## Preparing and launching the project and tests

Installing the requirements :

```
$> pip install requirements.txt
```

To run the server :

```
$> python manage.py runserver
```

Running the test :

```
$> python manage.py test
```

You can then test the endpoint by going on the http://127.0.0.1:8000/standarize/ page.

Request works in POST mode.

### Details on the architecture

/standarize is handled in a separated app (`standarize`).
The view StandarizerView inherits from `APIView` and uses a serializer `SensorsSerializer`.