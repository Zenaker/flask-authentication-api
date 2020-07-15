# flask-authentication-api
a simple flask authentication API with SQLite3 database management and RSA encrypted passwords

P.S change the public and private keys in the database/encryption folder :)

## API Calls

### Register
 * Register an account on the database
 
Send a `POST` request to `/auth/register` to register your account with the following parameters:

| Parameter     | Value                                             |
| ------------- | -----------------------------------------------   |
| `username`    | **String**: `the account's username`              |
| `email`       | **String**: `the account's email`                 |
| `password`    | **String**: `the account's password`              |

> Example request
```
POST /auth/register HTTP/1.1

username=test_username&email=test_email@email.com&password=password123
```

> Example Response
```JSON
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "success",
}
```
> Error Response
```JSON
HTTP/1.1 404
Content-Type: application/json

{
  "error":"error message"
}
```

### Login
 * Sign in the account
 
Send a `POST` request to `/auth/login` to sign in your account with the following parameters:

| Parameter     | Value                                             |
| ------------- | -----------------------------------------------   |
| `email`       | **String**: `the account's email`                 |
| `password`    | **String**: `the account's password`              |

> Example request
```
POST /auth/login HTTP/1.1

email=test_email@email.com&password=password123
```
> Example Response
```JSON
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "success",
}
```
> Error Response
```
HTTP/1.1 404
Content-Type: application/json

{
  "error":"error message"
}
```
