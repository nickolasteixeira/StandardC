# StandardC Challenge

### To Run Application:
From the root of the project folder, run:
```
$ MYSQL_USER=dev MYSQL_PWD=dev_pwd MYSQL_HOST=localhost MYSQL_DB=dev_db python3 -m api.v1.app
```

### Challenge 1:
Build an API to take in the following values: a,b,c,d, x and returns:

- y1 = a.X^2 + b.X^2 + c
- y2 = d.sin(X)
- y3 = y1/y2

#### API Routes:

- Correctly uses API Route for the challenge:
  - GET: API ROUTE: /api/v1/standardc
  - parameter values = ['a', 'b', 'c', 'd', 'x']
  - Example Uage:
  - http://52.53.173.11:5000/api/v1/standardc?a=2&b=3&c=4&d=5&x=6

- Return Value:

```
{
  "a": 2, 
  "b": 3, 
  "c": 4, 
  "d": 5, 
  "x": 6, 
  "y1": 94, 
  "y2": -1.4, 
  "y3": -67.28
}
```

- Incorrectly Uses API route for the challenge:
  - http://52.53.173.11:5000/api/v1/standardc?a=2&b=3&c=4&d=5&x=0

- Return Value
```
{
  "error": "Incorrect paramers. Please input valid integers"
}
```

 - POST: 
 - Example Usage:

```
$ curl -X POST -H "Content-Type: application/json" http://52.53.173.11:5000/api/v1/standardc -d '{"a":2, "b":3,"c":4,"d":5,"x":20}'
```


### Challenge 2

API would return values of a, b, c, d, x, y1, y2, y3 for any inquiry that was submitted in the past.

- Return either a time interval (date1 to date2, Feb 19 to Feb 22) and returns a list of all the objects in that date range OR
- Return the newest number of inquiries (Ex: 5 of the most recent inquiries or 5 - 15 of the most recent inquiries)

#### API Routes:
- Correctly uses API Route for the challenge:
  - API ROUTE: /api/v1/standardc/date1/date2
  - Example Uage:
  - http://52.53.173.11:5000/api/v1/standardc/2018-01-01/2019-03-06

- Return Value:

```
{
  "all items": [
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Sun, 25 Mar 2018 02:17:06 GMT", 
      "d": 5, 
      "id": "05b0b99c-f10e-4e3a-88d1-b3187d6998ee", 
      "updated_at": "Sun, 25 Mar 2018 02:17:06 GMT", 
      "x": 7, 
      "y1": 123.0, 
      "y2": 3.28, 
      "y3": 37.44
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Fri, 22 Feb 2019 02:17:06 GMT", 
      "d": 5, 
      "id": "14e2f358-f8fb-419c-8e8f-0017f971d82d", 
      "updated_at": "Fri, 22 Feb 2019 02:17:06 GMT", 
      "x": 8, 
      "y1": 156.0, 
      "y2": 4.95, 
      "y3": 31.54
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Sun, 24 Feb 2019 02:17:06 GMT", 
      "d": 5, 
      "id": "1721b75c-e0b2-46ae-8dd2-f86b62fb46e6", 
      "updated_at": "Sun, 24 Feb 2019 02:17:06 GMT", 
      "x": 10, 
      "y1": 234.0, 
      "y2": -2.72, 
      "y3": -86.03
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 19:08:42 GMT", 
      "d": 5, 
      "id": "1a3d7cf7-ce3b-46e8-a6ae-9c17453bbf5a", 
      "updated_at": "Tue, 05 Mar 2019 19:08:42 GMT", 
      "x": 20, 
      "y1": 864.0, 
      "y2": 4.56, 
      "y3": 189.28
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 17:52:52 GMT", 
      "d": 5, 
      "id": "3dc36c1c-62d3-4958-87e2-23b70709a805", 
      "updated_at": "Tue, 05 Mar 2019 17:52:52 GMT", 
      "x": 7, 
      "y1": 123.0, 
      "y2": 3.28, 
      "y3": 37.44
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Sat, 23 Feb 2019 02:17:06 GMT", 
      "d": 5, 
      "id": "459e021a-e794-447d-9dd2-e03b7963f7d2", 
      "updated_at": "Sat, 23 Feb 2019 02:17:06 GMT", 
      "x": 8, 
      "y1": 156.0, 
      "y2": 4.95, 
      "y3": 31.54
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 17:53:55 GMT", 
      "d": 5, 
      "id": "4da4f5f3-9c27-4a2c-bfee-aa11e121b422", 
      "updated_at": "Tue, 05 Mar 2019 17:53:55 GMT", 
      "x": 20, 
      "y1": 864.0, 
      "y2": 4.56, 
      "y3": 189.28
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 17:55:19 GMT", 
      "d": 5, 
      "id": "5ff7fe28-63b0-4325-b649-898f0f2b9e62", 
      "updated_at": "Tue, 05 Mar 2019 17:55:19 GMT", 
      "x": 50, 
      "y1": 5154.0, 
      "y2": -1.31, 
      "y3": -3928.73
    }, 
    {
      "a": 99, 
      "b": 99, 
      "c": 99, 
      "created_at": "Tue, 05 Mar 2019 19:37:26 GMT", 
      "d": 99, 
      "id": "7299327b-f267-42b2-b592-ccc300f5a397", 
      "updated_at": "Tue, 05 Mar 2019 19:37:26 GMT", 
      "x": 99, 
      "y1": 980199.0, 
      "y2": -98.92, 
      "y3": -9908.86
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 17:57:30 GMT", 
      "d": 5, 
      "id": "a670b029-25b4-4bd8-96a0-e1d1877eeddf", 
      "updated_at": "Tue, 05 Mar 2019 17:57:30 GMT", 
      "x": 100, 
      "y1": 20304.0, 
      "y2": -2.53, 
      "y3": -8019.5
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Sun, 24 Feb 2019 02:17:06 GMT", 
      "d": 5, 
      "id": "d2398800-dd87-482b-be21-50a3063858ad", 
      "updated_at": "Sun, 24 Feb 2019 02:17:06 GMT", 
      "x": 9, 
      "y1": 193.0, 
      "y2": 2.06, 
      "y3": 93.66
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 18:04:34 GMT", 
      "d": 5, 
      "id": "d7ec6a57-80a6-40ba-9378-b1bc496af0e1", 
      "updated_at": "Tue, 05 Mar 2019 18:04:34 GMT", 
      "x": 99, 
      "y1": 19903.0, 
      "y2": -5.0, 
      "y3": -3983.76
    }, 
    {
      "a": 2, 
      "b": 3, 
      "c": 4, 
      "created_at": "Tue, 05 Mar 2019 18:04:14 GMT", 
      "d": 5, 
      "id": "e9d8a7ce-5c10-4ad4-9a07-26932146f395", 
      "updated_at": "Tue, 05 Mar 2019 18:04:14 GMT", 
      "x": 1000, 
      "y1": 2003000.0, 
      "y2": 4.13, 
      "y3": 484473.0
    }
  ]
}
```

- Incorrectly Uses API route for the challenge:
  - http://52.53.173.11:5000/api/v1/standardc/2018-01-01/2019-03-33

- Return Value:
```
{'error': 'Incorrect date values. Enter new valid dates. EX: 2019-03-05'}
```
