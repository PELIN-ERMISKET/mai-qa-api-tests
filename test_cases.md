## Test #1 - GET /users (List Users)

Endpoint: GET /users?limit=10&offset=0&sort_by=id&order=asc
Expected Result: 200 OK + list of users
Actual Result: 200 OK + users returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to GET, endpoint to /users?limit=10&offset=0&sort_by=id&order=asc.
2.Add header Content-Type: application/json.
3.Send the request.
4.Verify that the returned status code is 200.
5.Verify that the response body contains an array of user objects (e.g., "username": "john_doe").

**Sample Response (truncated):**
```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "age": 30,
    "created_at": "2025-09-14T12:46:36.572887",
    "is_active": true,
    "phone": "+15551234567",
    "last_login": null
  }
]
```

Screenshot
![List Users Success](./screenshots/list_users_success.png)

## Test #2 - POST /users (Create User)

**Endpoint:** `POST /users`  
**Expected Result:** 201 Created + new user returned successfully (without password in response)  
**Actual Result:** 201 Created + user created and returned successfully  
**Result:** ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with valid user data (username, email, password, age, phone).
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body contains the newly created user object without the password field (e.g., "username": "new_user").

**Sample Request Body:**
```json
{
  "username": "new_user",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**

```json
{
  "id": 11,
  "username": "new_user",
  "email": "new_user@example.com",
  "age": 25,
  "created_at": "2025-09-14T15:44:47.880142",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}
```

Screenshot
![Create User Success](./screenshots/create_user_success.png)

## Test #3 - POST /users (Validation Error - Username too short)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username must be at least 3 characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with an invalid username shorter than 3 characters (e.g., "username": "ne").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username must have at least 3 characters.

**Sample Request Body:**
```json
{
  "username": "ne",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "username"
      ],
      "msg": "String should have at least 3 characters",
      "input": "ne",
      "ctx": {
        "min_length": 3
      }
    }
  ]
}
```
Screenshot
![Username_too_short](./screenshots/Username_too_short.png)

## Test #4 - POST /users (Boundary Test - Username length 50)
Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (username accepted with 50 characters)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username that has exactly 50 characters.
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body contains the newly created user object, and the username field matches the 50-character input.

**Sample Request Body:**
```json
{
  "username": "newusernewusernewusernewusernewusernewusernewusern",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "id": 13,
  "username": "newusernewusernewusernewusernewusernewusernewusern",
  "email": "new_user@example.com",
  "age": 25,
  "created_at": "2025-09-14T17:25:57.722934",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}
```
Screenshot
![Username_50chars](./screenshots/Username_50chars.png)

## Test #5 - POST /users (Boundary Test - Username length = 3)

Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (minimum 3-character username should be valid)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username that has exactly 3 characters (minimum allowed).
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body contains the newly created user object with the 3-character username included.

**Sample Request Body:**
```json
{
  "username": "new",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**

```json
{
  "id": 14,
  "username": "new",
  "email": "new_user@example.com",
  "age": 25,
  "created_at": "2025-09-14T18:08:37.195188",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}

```
Screenshot
![Username_min_length](./screenshots/Username_min_length.png)

## Test #6 – POST /users (Validation Error – Username too long)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username must be at most 50 characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username longer than 50 characters.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating the username must have at most 50 characters.

**Sample Request Body:**
```json
{
  "username": "newusernewusernewusernewusernewusernewusernewuserne",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_too_long",
      "loc": [
        "body",
        "username"
      ],
      "msg": "String should have at most 50 characters",
      "input": "newusernewusernewusernewusernewusernewusernewuserne",
      "ctx": {
        "max_length": 50
      }
    }
  ]
}
```
Screenshot
![Username_tool_long](./screenshots/Username_tool_long.png)

## Test #7 – POST /users (Validation Error – Username must be a string)

Endpoint: POST /users  
Expected Result: 422 Unprocessable Content + validation error (username must be a string)  
Actual Result: 422 Unprocessable Content + validation error returned successfully  
Result: ✅ Pass  

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a non-string value for the username field (e.g., an integer 123).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username must be a valid string.

**Sample Request Body:**
```json
{
  "username": 123,
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": [
        "body",
        "username"
      ],
      "msg": "Input should be a valid string",
      "input": 123
    }
  ]
}
```
Screenshot
![Username must be a string](./screenshots/Username_string.png)

## Test #8 – POST /users (Validation Error – Username Null)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username must be a valid string)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with username set to null.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username must be a valid string.

**Sample Request Body:**
```json
{
  "username": null,
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": [
        "body",
        "username"
      ],
      "msg": "Input should be a valid string",
      "input": null
    }
  ]
}
```
Screenshot
![Username  Null](./screenshots/Username_Null.png)

## Test #9 – POST /users (Validation Error – Username Empty String)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username must have at least 3 characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with username as an empty string "".
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username must have at least 3 characters.

**Sample Request Body:**
```json
{
  "username": "",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "username"
      ],
      "msg": "String should have at least 3 characters",
      "input": "",
      "ctx": {
        "min_length": 3
      }
    }
  ]
}
```
Screenshot
![Username Empty String](./screenshots/Username_Empty_String.png)

## Test #10 – POST /users (Validation Error – Duplicate Username)

Endpoint: POST /users
Expected Result: 400 Bad Request + validation error (Username already exists)
Actual Result: 400 Bad Request + "Username already exists" returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username value that already exists in the system (e.g., "john_doe").
4.Send the request.
5.Verify that the returned status code is 400.
6.Verify that the response body contains the validation error message "Username already exists".

**Sample Request Body:**
```json
{
  "username": "john_doe",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": "Username already exists"
}
```
Screenshot
![Duplicate Username](./screenshots/Duplicate_Username.png)

## Test #11 – POST /users (Validation Error – Username with space)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username contains invalid characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username that contains a space (e.g., "new user").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username contains invalid characters.

**Sample Request Body:**
```json
{
  "username": "new user",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "username"
      ],
      "msg": "Value error, Username contains invalid characters",
      "input": "new user",
      "ctx": {
        "error": {}
      }
    }
  ]
}
```
Screenshot
![Username with space](./screenshots/Username_with_space.png)

## Test #12 – POST /users (Validation Error – Username contains invalid characters)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username should only contain allowed characters: letters, numbers, underscore)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username containing invalid characters (e.g., "user:)")
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username contains invalid characters.

**Sample Request Body:**
```json
{
  "username": "user:)",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "username"
      ],
      "msg": "Value error, Username contains invalid characters",
      "input": "user:)",
      "ctx": {
        "error": {}
      }
    }
  ]
}
```
Screenshot
![Username invalid characterse](./screenshots/Username_invalid_characters.png)

## Test #13 – POST /users (Validation Error – Username with leading/trailing spaces)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username should not contain leading or trailing spaces)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username that contains leading or trailing spaces (e.g., " new_user ").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username should not contain leading or trailing spaces.

**Sample Request Body:**
```json
{
  "username": " new_user ",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "username"
      ],
      "msg": "Value error, Username contains invalid characters",
      "input": " new_user ",
      "ctx": {
        "error": {}
      }
    }
  ]
}
```
Screenshot
![Username_spaces](./screenshots/Username_spaces.png)

## Test #14 – POST /users (Validation Error – Username contains underscore)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (username must not contain invalid/non-ASCII characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a username that includes an invalid or non-ASCII character (e.g., "pelin_ç").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error message indicating that the username contains invalid characters.

**Sample Request Body:**
```json
{
  "username": "pelin_ç",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "username"
      ],
      "msg": "Value error, Username contains invalid characters",
      "input": "pelin_ç",
      "ctx": {
        "error": {}
      }
    }
  ]
}
```
Screenshot
![Username contains underscore](./screenshots/Username_contains_underscore.png)

## Test #15 – POST /users (Validation Error – Username Case Sensitivity Not Enforced)

Endpoint: POST /users
Expected Result: 400 Bad Request + validation error (API should reject duplicate usernames regardless of letter case, e.g., "Username already exists")
Actual Result: 201 Created + second user created successfully with same username in different case
Result: ❌ Fail (Bug Found)

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Create a user with username "john_doe".
4.Create another user with username "John_Doe" (different only by case).
5.Send both requests sequentially.
6.Verify that the second request should fail with "Username already exists", but instead it is accepted.

Evidence:

// Request
```json
{
  "username": "John_Doe",
  "email": "new_user@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
// Response
```json
{
  "id": 17,
  "username": "john_doe",
  "email": "new_user@example.com",
  "age": 25,
  "created_at": "2025-09-14T22:11:13.545343",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}
```
Screenshot
![Create_Username_BUG-001](./screenshots/BUG-001.png)

## Test #16 – POST /users (Validation Error – Email missing local-part before @)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (email is invalid; missing local-part before @)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with email set to "@example.com" (no local-part before @).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating the email is not valid because something must exist before the @ sign.

**Sample Request Body:**
```json
{
  "username": "user_new",
  "email": "@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "email"
      ],
      "msg": "value is not a valid email address: There must be something before the @-sign.",
      "input": "@example.com",
      "ctx": {
        "reason": "There must be something before the @-sign."
      }
    }
  ]
}
```
Screenshot
![Create_Username_Email missing](./screenshots/Email_missing.png)

## Test #17 – POST /users (Validation Error – Email missing domain)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (email is invalid; missing domain after @)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with email set to "new_user@" (no domain after @).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating there must be something after the @ sign.

**Sample Request Body:**
```json
{
  "username": "user_new",
  "email": "new_user@",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "email"
      ],
      "msg": "value is not a valid email address: There must be something after the @-sign.",
      "input": "new_user@",
      "ctx": {
        "reason": "There must be something after the @-sign."
      }
    }
  ]
}
```
Screenshot
![Create_Username_Email missing domain](./screenshots/Email_missing_domain.png)

## Test #18 – POST /users (Validation Error – Email Empty String)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (email is invalid; must contain @)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with email set to "" (empty string).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating an email address must have an @-sign.

**Sample Request Body:**
```json
{
  "username": "user_new",
  "email": "",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "email"
      ],
      "msg": "value is not a valid email address: An email address must have an @-sign.",
      "input": "",
      "ctx": {
        "reason": "An email address must have an @-sign."
      }
    }
  ]
}
```
Screenshot
![Create_Username_Email Empty String](./screenshots/Email_Empty_String.png)

## Test #19 – POST /users (Validation Error – Email Null)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (email must be a valid string; null not allowed)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with email set to null.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating the email must be a valid string.

**Sample Request Body:**
```json

{
  "username": "user_new",
  "email": null,
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}

```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": [
        "body",
        "email"
      ],
      "msg": "Input should be a valid string",
      "input": null
    }
  ]
}

```
Screenshot
![Create_Username_Email_Null](./screenshots/Email_Null.png)

## Test #20 – POST /users (Validation Error – Duplicate Email)

Endpoint: POST /users
Expected Result: 400 Bad Request + validation error (Email already exists)
Actual Result: 201 Created + user created successfully with duplicate email
Result: ❌ Fail (Bug Found)

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with an email value that already exists in the system (e.g., "new_user@example.com
").
4.Send the request.
5.Verify that the second request should fail with "Email already exists", but instead it is accepted (201 Created).

**Sample Request Body:**
```json
{
  "username": "user_neww",
  "email": "new_user@example.com",
  "password": "oldneew",
  "age": 25,
  "phone": "+25452548521"
}


```
**Sample Response Body:(buggy behavior)**
```json 
{
    "id": 20,
    "username": "user_neww",
    "email": "new_user@example.com",
    "age": 25,
    "created_at": "2025-09-15T09:44:17.533662",
    "is_active": true,
    "phone": "+25452548521",
    "last_login": null
}
```
Screenshot
![Create_Username_BUG-002](./screenshots/BUG-002.png)

## Test #21 – POST /users (Validation Error – Duplicate Email, case-insensitive)

Endpoint: POST /users
Expected Result: 400 Bad Request + validation error (Email already exists – case-insensitive)
Actual Result: 201 Created + user created successfully with duplicate email (different case)
Result: ❌ Fail (Bug Found)

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Create a user with email "new_user@example.com".
4.Create another user with email "New_User@example.com" (same email, different case).
5.Send both requests sequentially.
6.Verify that the second request should fail with "Email already exists", but instead it is accepted (201 Created).

**Sample Request Body:**
```json
{
  "username": "usernewuser",
  "email": "New_User@example.com",
  "password": "oldnew",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:(buggy behavior)**
```json 
{
  "id": 19,
  "username": "usernewuser",
  "email": "New_User@example.com",
  "age": 25,
  "created_at": "2025-09-15T09:26:34.404698",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}
```
Screenshot
![Create_Username_BUG-003](./screenshots/BUG-003.png)

## Test #22 – POST /users (Boundary – Password length = 6)

Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (minimum 6-character password should be valid)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password having exactly 6 characters (e.g., "janedo").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body does not include the password field and the user object is returned.

**Sample Request Body:**
```json
{
  "username": "jane_doe",
  "email": "jane_doe@example.com",
  "password": "janedo",
  "age": 25,
  "phone": "+25452548521"
}

```
**Sample Response Body:**
```json
{
  "id": 21,
  "username": "jane_doe",
  "email": "jane_doe@example.com",
  "age": 25,
  "created_at": "2025-09-15T10:25:02.613657",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}
```
Screenshot
![Create Boundary_Password_length](./screenshots/Password_length.png)

## Test #23 – POST /users (Validation Error – Password too short, length = 5)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (password must be at least 6 characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password set to a 5-character string (e.g., "johnn").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating min length 6 (type "string_too_short").

**Sample Request Body:**
```json
{
  "username": "John",
  "email": "John_user@example.com",
  "password": "johnn",
  "age": 25,
  "phone": "+25452540521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "password"
      ],
      "msg": "String should have at least 6 characters",
      "input": "johnn",
      "ctx": {
        "min_length": 6
      }
    }
  ]
}
```
Screenshot
![Create Boundary_Password_short](./screenshots/Password_short.png)

## Test #24 – POST /users (Validation Error – Password empty string)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (password must be at least 6 characters)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password set to "" (empty string).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating min length 6 (type "string_too_short").

**Sample Request Body:**
```json
{
  "username": "Johnny",
  "email": "Johnny@example.com",
  "password": "",
  "age": 25,
  "phone": "+25453548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "password"
      ],
      "msg": "String should have at least 6 characters",
      "input": "",
      "ctx": {
        "min_length": 6
      }
    }
  ]
}
```
Screenshot
![Create Boundary_Password_empty](./screenshots/Password_empty.png)

## Test #25 – POST /users (Validation Error – Password null)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (password must be a valid string)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password set to null.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error indicating the password must be a valid string (type "string_type").

**Sample Request Body:**
```json
{
  "username": "Doe",
  "email": "doe@example.com",
  "password": null,
  "age": 25,
  "phone": "+25451548521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": [
        "body",
        "password"
      ],
      "msg": "Input should be a valid string",
      "input": null
    }
  ]
}
```
Screenshot
![Create Boundary_Password_null](./screenshots/Password_null.png)

## Test #26 – POST /users (Validation Error – Password non-string (number))

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (password must be a valid string)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password as a number (unquoted), e.g., 123456.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error of type "string_type" for the password field.

**Sample Request Body:**
```json
{
  "username": "JohnnDoe",
  "email": "JohnnDoe@example.com",
  "password": 123456,
  "age": 25,
  "phone": "+25452578521"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": [
        "body",
        "password"
      ],
      "msg": "Input should be a valid string",
      "input": 123456
    }
  ]
}
```
Screenshot
![Create Boundary_Password_non-string](./screenshots/Password_non-string.png)

## Test #27 – POST /users (Password with only spaces (6) – accepted)

Endpoint: POST /users
Expected Result: 201 Created + user created successfully (password meets only min_length=6)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password set to exactly six spaces " ".
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body does not include the password field and the user object is returned.
**Sample Request Body:**
```json
{
  "username": "JDoe",
  "email": "JDoe@example.com",
  "password": "      ",
  "age": 25,
  "phone": "+25452528521"
}
```
**Sample Response Body:**
```json
{
  "id": 22,
  "username": "jdoe",
  "email": "JDoe@example.com",
  "age": 25,
  "created_at": "2025-09-15T11:09:42.503964",
  "is_active": true,
  "phone": "+25452528521",
  "last_login": null
}
```
Screenshot
![Create Boundary_Password_only_spaces](./screenshots/Password_only_spaces.png)

## Test #28 – POST /users (Password with leading/trailing spaces – accepted)

Endpoint: POST /users
Expected Result: 201 Created + user created successfully (password with leading/trailing spaces is accepted; only min_length=6 enforced)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with password containing leading and trailing spaces (e.g., " jane ").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body excludes the password field and returns the created user.
**Sample Request Body:**
```json
{
  "username": "Jane",
  "email": "janeuser@example.com",
  "password": " jane ",
  "age": 25,
  "phone": "+25488548521"
}

```
**Sample Response Body:**
```json
{
  "id": 23,
  "username": "jane",
  "email": "janeuser@example.com",
  "age": 25,
  "created_at": "2025-09-15T11:14:46.784683",
  "is_active": true,
  "phone": "+25488548521",
  "last_login": null
}
```
Screenshot
![Create Boundary_Password_trailing_spaces](./screenshots/Password_trailing_spaces.png)

## Test #29 – POST /users (Password very long – 350 chars → accepted)

Endpoint: POST /users
Expected Result: 201 Created + user created successfully (no max length constraint)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a password of 350 characters (e.g., Postman var {{pw350}} or 'A'×350).
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body does not include the password field.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw350}}",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
  "id": 24,
  "username": "pw1757925429527",
  "email": "pw1757925429527@example.com",
  "age": 25,
  "created_at": "2025-09-15T11:37:09.763465",
  "is_active": true,
  "phone": "+25452548521",
  "last_login": null
}
```
Screenshot
![Create Boundary_Password_very_long](./screenshots/Password_very_long.png)

## Test #30 – POST /users (Password with special characters – accepted)

Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (special characters allowed; only min_length=6 enforced)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a password containing special characters (e.g., "p@ss^&*()!").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body excludes the password field and returns the created user.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "p@ss^&*()!",
  "age": 25,
  "phone": "+25452549521"
}

```
**Sample Response Body:**
```json

{
  "id": 25,
  "username": "pw1757926464452",
  "email": "pw1757926464452@example.com",
  "age": 25,
  "created_at": "2025-09-15T11:54:24.514424",
  "is_active": true,
  "phone": "+25452549521",
  "last_login": null
}
```
Screenshot
![Create Boundary_Password_special_characters](./screenshots/Password_special_characters.png)

## Test #31 – POST /users (Password with Unicode characters – accepted)

Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (Unicode characters allowed; only min_length=6 enforced)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a password containing Unicode characters (e.g., "Şifré🙂123").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body excludes the password field and returns the created user.

**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "Şifré🙂123",
  "age": 25,
  "phone": "+25452549521"
}
```
**Sample Response Body:**
```json

{
  "id": 26,
  "username": "pw1757926890859",
  "email": "pw1757926890859@example.com",
  "age": 25,
  "created_at": "2025-09-15T12:01:30.939578",
  "is_active": true,
  "phone": "+25452549521",
  "last_login": null
}
```
Screenshot
![Create Boundary_Password_Unicode](./screenshots/Password_Unicode.png)

## Test #33 – POST /users (Security – Password must NOT appear in response)

Endpoint: POST /users
Expected Result: 201 Created + response body does not contain password (veya password_hash/hash/salt)
Actual Result: 201 Created + password alanı yok
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide a valid request body with a password (>=6 chars).
4.Send the request.
5.Verify status code is 201.
6.Verify response text does not include "password", "password_hash", "hash", or "salt".

**Sample Request Body:**
```json
{
  "username": "no_pwd_leak",
  "email": "no_pwd_leak@example.com",
  "password": "secret123",
  "age": 25,
  "phone": "+25452548521"
}
```
**Sample Response Body:**
```json
{
    "id": 27,
    "username": "no_pwd_leak",
    "email": "no_pwd_leak@example.com",
    "age": 25,
    "created_at": "2025-09-15T12:15:50.849055",
    "is_active": true,
    "phone": "+25452548521",
    "last_login": null
}
```
Screenshot
![Create Boundary_Password_NOT_appear_in_response](./screenshots/Password_NOT_appear_in_response.png)

## Test #34 – POST /users (Boundary – Age = 18)

Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (minimum age 18 is valid)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": 18 (boundary minimum).
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body returns the created user; password not included.

**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 18,
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json

{
  "id": 28,
  "username": "pw1757930979865",
  "email": "pw1757930979865@example.com",
  "age": 18,
  "created_at": "2025-09-15T13:09:39.901820",
  "is_active": true,
  "phone": "+254930979865",
  "last_login": null
}
```
Screenshot
![Create Boundary_Boundary_Age18](./screenshots/Boundary_Age18.png)

## Test #35 – POST /users (Boundary – Age = 150)

Endpoint: POST /users
Expected Result: 201 Created + new user returned successfully (maximum age 150 is valid)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": 150 (boundary maximum).
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body returns the created user; password not included.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 150,
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json
{
  "id": 29,
  "username": "pw1757931741680",
  "email": "pw1757931741680@example.com",
  "age": 150,
  "created_at": "2025-09-15T13:22:21.721376",
  "is_active": true,
  "phone": "+254931741680",
  "last_login": null
}
```
Screenshot
![Create Boundary_Boundary_Age_150](./screenshots/Boundary_Age_150.png)

## Test #36 – POST /users (Validation Error – Age below minimum, 17)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (age must be ≥ 18)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": 17.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body indicates the min age is 18.
**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 17,
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": [
        "body",
        "age"
      ],
      "msg": "Input should be greater than or equal to 18",
      "input": 17,
      "ctx": {
        "ge": 18
      }
    }
  ]
}
```
Screenshot
![Create Boundary_Boundary_Age_min](./screenshots/Boundary_Age_min.png)

## Test #37 – POST /users (Validation Error – Age above maximum, 151)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (age must be ≤ 150)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": 151.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body shows less_than_equal with "le": 150.
**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 151,
  "phone": "{{uniqPhone}}"
}

```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": [
        "body",
        "age"
      ],
      "msg": "Input should be less than or equal to 150",
      "input": 151,
      "ctx": {
        "le": 150
      }
    }
  ]
}
```
Screenshot
![Create Boundary_Boundary_Age_max](./screenshots/Boundary_Age_max.png)

## Test #39 – POST /users (Validation Error – Age not an integer: "25a")

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (age must be a valid integer)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with age as a non-integer string (e.g., "25a").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body reports an integer parsing error for the age field.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": "25a",
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "body",
        "age"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "25a"
    }
  ]
}
```
Screenshot
![Create Boundary_Age_not_int](./screenshots/Age_not_int.png)

## Test #40 – POST /users (Validation Error – Age not integer (float 18.5))

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (age must be an integer, floats not allowed)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": 18.5 (float).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body indicates age must be a valid integer.
**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 18.5,
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "int_from_float",
      "loc": ["body", "age"],
      "msg": "Input should be a valid integer, got a number with a fractional part",
      "input": 18.5
    }
  ]
}
```
Screenshot
![Create Boundary_Age_float](./screenshots/Age_float.png)

## Test #41 – POST /users (Validation Error – Age Null)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (age must be a valid integer)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": null.
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the error type indicates integer required (e.g., int_type / “Input should be a valid integer”).
**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": null,
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "int_type",
      "loc": [
        "body",
        "age"
      ],
      "msg": "Input should be a valid integer",
      "input": null
    }
  ]
}
```
Screenshot
![Create Boundary_Age_null](./screenshots/Age_null.png)

## Test #42 – POST /users (Validation Error – Age Empty String)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (age must be a valid integer)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with "age": "" (empty string).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response shows an integer parsing error for age.
**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": "",
  "phone": "{{uniqPhone}}"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["body", "age"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": ""
    }
  ]
}
```
Screenshot
![Create Boundary_Age_Empty](./screenshots/Age_Empty.png)

## Test #43 – POST /users (Valid Phone – E.164 format)

Endpoint: POST /users
Expected Result: 201 Created + user returned successfully (phone accepted)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a valid E.164 phone number (e.g., “+254931741680”).
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body contains the created user object and the phone matches the submitted value.

**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+254931741680"
}
```
**Sample Response Body:**
```json

{
  "id": 31,
  "username": "ph17579351382070",
  "email": "ph17579351382070@example.com",
  "age": 25,
  "created_at": "2025-09-15T14:18:58.317515",
  "is_active": true,
  "phone": "+254931741680",
  "last_login": null
}
```
Screenshot
![Create User_Phone_E_164_format](./screenshots/Phone_E_164_format.png)

## Test #44 – POST /users (Boundary Test – Phone min length = 9 digits)

Endpoint: POST /users
Expected Result: 201 Created + phone accepted when it has 9 digits (minimum allowed by regex)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a phone containing exactly 9 digits after the plus (e.g., "+254931740").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body contains the created user object and no password field.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+254931740"
}
```
**Sample Response Body:**
```json

{
"id": 35,
    "username": "ph1757937363832",
    "email": "ph1757937363832@example.com",
    "age": 25,
    "created_at": "2025-09-15T14:56:03.873792",
    "is_active": true,
    "phone": "+254931740",
    "last_login": null
}
```
Screenshot
![Create User_Phone_Boundary_9](./screenshots/Phone_Boundary_9.png)

## Test #45 – POST /users (Boundary Test – Phone length = 15 digits)

Endpoint: POST /users
Expected Result: 201 Created + user created successfully (phone with 15 digits after optional "+" is accepted)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a phone that has exactly 15 digits after the "+" (e.g., "+254931740254152").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body includes the created user and phone equals "+254931740254152".

**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+254931740254152"
}
```
**Sample Response Body:**
```json

{
    "id": 36,
    "username": "ph1757937701260",
    "email": "ph1757937701260@example.com",
    "age": 25,
    "created_at": "2025-09-15T15:01:41.302513",
    "is_active": true,
    "phone": "+254931740254152",
    "last_login": null
}
```
Screenshot
![Create User_Phone_Boundary_15](./screenshots/Phone_Boundary_15.png)

## Test #46 – POST /users (Valid – Phone digits only, without “+”)

Endpoint: POST /users
Expected Result: 201 Created + user created successfully (phone with digits-only format is accepted)
Actual Result: 201 Created + user created and returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body where phone has only digits (e.g., "254931741680").
4.Send the request.
5.Verify that the returned status code is 201.
6.Verify that the response body includes the created user and phone equals "254931741680".

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "254931741680"
}
```
**Sample Response Body:**
```json
{
  "id": 37,
  "username": "ph1757937983157",
  "email": "ph1757937983157@example.com",
  "age": 25,
  "created_at": "2025-09-15T15:06:23.193754",
  "is_active": true,
  "phone": "254931741680",
  "last_login": null
}
```
Screenshot
![Create User_Phone_digits_only](./screenshots/Phone_digits_only.png)

## Test #47 – POST /users (Validation Error – Phone too short)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (“Invalid phone number format”)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:

1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body with a phone shorter than 9 digits after optional “+” (e.g., "+25493416").
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error for phone with message Invalid phone number format.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+25493416"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "phone"
      ],
      "msg": "Value error, Invalid phone number format",
      "input": "+25493416",
      "ctx": {
        "error": {}
      }
    }
  ]
}
```
Screenshot
![Create User_Phone_short](./screenshots/Phone_short.png)

## Test #48 – POST /users (Invalid – Phone length 16 digits)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (phone number too long; >15 digits)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body where phone has 16 digits after the optional “+” (e.g., “+2549265231741680”).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error for "phone" with a message like "Invalid phone number format".
**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+2549265231741680"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "phone"],
      "msg": "Value error, Invalid phone number format",
      "input": "+2549265231741680",
      "ctx": { "error": {} }
    }
  ]
}
```
Screenshot
![Create User_Phone_length](./screenshots/Phone_length.png)

## Test #49 – POST /users (Invalid – Phone contains spaces)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (phone contains spaces; not E.164)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body where phone includes a space character (e.g., “+254 9265680”).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error for "phone" with a message like "Invalid phone number format".

**Sample Request Body:**
```json

{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+254 9265680"
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "phone"],
      "msg": "Value error, Invalid phone number format",
      "input": "+254 9265680",
      "ctx": { "error": {} }
    }
  ]
}
```
Screenshot
![Create User_Phone_empty](./screenshots/Phone_empty.png)

## Test #50 – POST /users (Invalid – Phone contains letters)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error (phone contains non-digit characters; not E.164)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body where phone includes alphabetic characters (e.g., “+254a9265680”).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error for "phone" with a message like "Invalid phone number format".

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+254a9265680"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "phone"],
      "msg": "Value error, Invalid phone number format",
      "input": "+254a9265680",
      "ctx": { "error": {} }
    }
  ]
}
```
Screenshot
![Create User_Phone_Invalid](./screenshots/Phone_Invalid.png)

## Test #51 – POST /users (Invalid – “+” sonrası 0 ile başlıyor)

Endpoint: POST /users
Expected Result: 422 Unprocessable Content + validation error .
Actual Result: 201 Created + user created and returned successfully (BUG – “+00…” )
Result: ❌ Fail

Steps to Execute:
1.Set method to POST, endpoint to /users.
2.Add header Content-Type: application/json.
3.Provide the request body where phone starts with “+0” (e.g., “+0049265680”).
4.Send the request.
5.Verify that the expected status code is 422.
6.If 201 is returned, log a defect for non-compliant E.164 validation.

**Sample Request Body:**
```json
{
  "username": "{{uniqUser}}",
  "email": "{{uniqEmail}}",
  "password": "{{pw6}}",
  "age": 25,
  "phone": "+0049265680"
}
```
**Sample Response Body:**
```json

{
  "id": 38,
  "username": "ph1757942908198",
  "email": "ph1757942908198@example.com",
  "age": 25,
  "created_at": "2025-09-15T16:28:28.235929",
  "is_active": true,
  "phone": "+0049265680",
  "last_login": null
}
```
Screenshot
![Create User_BUG-004](./screenshots/BUG-004.png)

## Test #52 – POST /login (Valid Login)

Endpoint: POST /login
Expected Result: 200 OK + token issued successfully (token, expires_in, user_id present)
Actual Result: 200 OK + token returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /login.
2.Add header Content-Type: application/json.
3.Provide the request body with a valid existing username and password (e.g., admin_user / Admin@2024).
4.Send the request.
5.Verify that the returned status code is 200.
6.Verify that the response body contains token (non-empty string), expires_in (integer), and user_id (integer).

**Sample Request Body:**
```json

{
  "username": "admin_user",
  "password": "Admin@2024"
}
```
**Sample Response Body:**
```json

{
  "token": "e694542a755bdc1dbd72fba2302f51ac",
  "expires_in": 86400,
  "user_id": 7
}
```
Screenshot
![Create User_Valid_Login](./screenshots/Valid_Login.png)

## Test #53 – POST /login (Invalid – Wrong password)

Endpoint: POST /login
Expected Result: 401 Unauthorized + error message “Invalid username or password”
Actual Result: 401 Unauthorized + error message returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /login.
2.Add header Content-Type: application/json.
3.Provide the request body with a valid existing username and an incorrect password.
4.Send the request.
5.Verify that the returned status code is 401.
6.Verify that the response body contains detail with the message “Invalid username or password”.

**Sample Request Body:**
```json

{
  "username": "admin_user",
  "email": "admin@company.com",
  "password": "Admin@WRONG",
  "age": 45,
  "phone": "+19175551234"
}

```
**Sample Response Body:**
```json
{
  "detail": "Invalid username or password"
}

```
Screenshot
![Create User_Login_Wrong_password](./screenshots/Login_Wrong_password.png)

## Test #54 – POST /login (Invalid – Non-existent username)

Endpoint: POST /login
Expected Result: 401 Unauthorized + error message “Invalid username or password”
Actual Result: 401 Unauthorized + error message returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /login.
2.Add header Content-Type: application/json.
3.Provide the request body with a non-existent username and a valid-looking password.
4.Send the request.
5.Verify that the returned status code is 401.
6.Verify that the response body contains detail with the message “Invalid username or password”.

**Sample Request Body:**
```json
{
  "username": "no_such_user",
  "email": "admin@company.com",
  "password": "Admin@2024",
  "age": 45,
  "phone": "+19175551234"
}
```
**Sample Response Body:**
```json

{
  "detail": "Invalid username or password"
}
```
Screenshot
![Create User_Login_Non_existent_username](./screenshots/Login_Non_existent_username.png)

## Test #55 – POST /login (Invalid – Null/Missing password)

Endpoint: POST /login
Expected Result: 422 Unprocessable Content + validation error for "password" (e.g., "Input should be a valid string" when null)
Actual Result: 422 Unprocessable Content + validation error returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /login.
2.Add header Content-Type: application/json.
3.Provide the request body where password is null (not a string).
4.Send the request.
5.Verify that the returned status code is 422.
6.Verify that the response body contains a validation error for "password" with a message like "Input should be a valid string".
**Sample Request Body:**
```json

{
  "username": "john_doe",
  "password": null
}
```
**Sample Response Body:**
```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": ["body", "password"],
      "msg": "Input should be a valid string",
      "input": null
    }
  ]
}
```
Screenshot
![Create User_Login_Missing_password](./screenshots/Login_Missing_password.png)

## Test #56 – POST /login (Invalid – Empty password string)

Endpoint: POST /login
Expected Result: 401 Unauthorized + error message “Invalid username or password”
Actual Result: 401 Unauthorized + error message returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to POST, endpoint to /login.
2.Add header Content-Type: application/json.
3.Provide the request body where password is an empty string ("").
4.Send the request.
5.Verify that the returned status code is 401.
6.Verify that the response body contains detail with the message “Invalid username or password”.

**Sample Request Body:**
```json
{
  "username": "john_doe",
  "password": ""
}
```
**Sample Response Body:**
```json
{
  "detail": "Invalid username or password"
}
```
Screenshot
![Create User_Login_Empty_password](./screenshots/Login_Empty_password.png)

## Test #57 – PUT /users/{id} (Valid – Self Update with Bearer)

Endpoint: PUT /users/{id}
Expected Result: 200 OK + user updated successfully (returns updated user; no password in response)
Actual Result: 200 OK + user updated successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to PUT, endpoint to /users/{{selfUserId}}.
2.Add headers Content-Type: application/json and Authorization: Bearer {{token}}.
3.Provide the request body with valid updatable fields (email/age/phone).
4.Send the request.
5.Verify that the returned status code is 200.
6.Verify that the response body reflects the updated fields and does not contain a password field.

**Sample Request Body:**
```json
{
  "email": "new_email@example.com",
  "age": 46,
  "phone": "+19175551235"
}

```
**Sample Response Body:**
```json
{
  "id": 7,
  "username": "admin_user",
  "email": "new_email@example.com",
  "age": 46,
  "created_at": "2025-09-14T12:46:48.906068",
  "is_active": true,
  "phone": "+19175551235",
  "last_login": "2025-09-15T19:27:57.124805"
}
```
Screenshot
![PUT-UPDATE-Self Update](./screenshots/Self_Update.png)

## Test #58 – PUT /users/{id} (Invalid – Missing Bearer)

Endpoint: PUT /users/{id}
Expected Result: 401 Unauthorized + error message “Authentication required”
Actual Result: 401 Unauthorized + error message returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to PUT, endpoint to /users/{{selfUserId}}.
2.Authorization: No Auth (ensure the Authorization header is not sent).
3.Add header Content-Type: application/json.
4.Provide the request body with a valid field (e.g., email) as JSON.
5.Send the request.
6.Verify that the returned status code is 401.
7.Verify that the response body contains detail with the message "Authentication required".
**Sample Request Body:**
```json

{
  "email": "missingbearer@example.com"
}

```
**Sample Response Body:**
```json

{
  "detail": "Authentication required"
}

```
Screenshot
![PUT-UPDATE-Missing_Bearer](./screenshots/Missing_Bearer.png)

## Test #59 – PUT /users/{otherId} (Invalid – Ownership check)

Endpoint: PUT /users/{otherId}
Expected Result: 403 Forbidden or 404 Not Found + error message (user cannot update another user)
Actual Result: 200 OK + target user updated successfully (ownership check missing – IDOR/BOLA)
Result: ❌ Fail

Steps to Execute:
1.Set method to PUT, endpoint to /users/11.
2.Authorization: Bearer {{token}} (token belongs to self user_id=7).
3.Add header Content-Type: application/json.
4.Body → raw → JSON:

{ "phone": "+19175551236" }


5.Send the request.
6.Verify expected status code is 403 or 404.
7.Observed 200 OK with updated target user → BUG.

**Sample Request Body:**
```json

{
  "phone": "+19175551236"
}
```
**Sample Response Body:**
```json

{
  "id": 11,
  "username": "new_user",
  "email": "new_user@example.com",
  "age": 25,
  "created_at": "2025-09-14T15:44:47.880142",
  "is_active": true,
  "phone": "+19175551236",
  "last_login": null
}

```
Screenshot
![PUT-UPDATE-BUG-005](./screenshots/BUG-005.png)

## Test #60 – PUT /users/{id} (Invalid – Phone = "string")

Endpoint: PUT /users/{id}
Expected Result: 422 Unprocessable Content + validation error (phone must be E.164; non-numeric string should be rejected)
Actual Result: 200 OK + user updated with phone: "string" (BUG – phone accepts non-numeric string)
Result: ❌ Fail

Steps to Execute:
1.Set method to PUT, endpoint to /users/{{selfUserId}}.
2.Add headers Content-Type: application/json and Authorization: Bearer {{token}}.
3.Provide the request body where phone is the literal string "string".
4.Send the request.
5.Verify that the expected status code is 422.
6.If 200 is returned, log a defect for missing phone validation on update.

**Sample Request Body:**
```json

{
  "phone": "string"
}
```
**Sample Response Body:**
```json
{
  "id": 7,
  "username": "admin_user",
  "email": "missingbearer@example.com",
  "age": 46,
  "created_at": "2025-09-14T12:46:48.906068",
  "is_active": true,
  "phone": "string",
  "last_login": "2025-09-15T19:27:57.124805"
}
```
Screenshot
![PUT-UPDATE-BUG-006](./screenshots/BUG-006.png)

## Test #61 – PUT /users/{id} (Invalid – Phone length 16 digits)

Endpoint: PUT /users/{id}
Expected Result: 422 Unprocessable Content + validation error (E.164 allows max 15 digits after “+”)
Actual Result: 200 OK + user updated with a 16-digit phone (BUG – length validation missing)
Result: ❌ Fail

Steps to Execute:

1.Set method to PUT, endpoint to /users/{{selfUserId}}.
2.Add headers Content-Type: application/json and Authorization: Bearer {{token}}.
3.Provide the request body where phone has 16 digits after the plus sign (e.g., +1917555123456789).
4.Send the request.
5.Verify that the expected status code is 422.
**Sample Request Body:**
```json

{
  "phone": "+1917555123456789"
}
```
**Sample Response Body:**
```json

{
  "id": 7,
  "username": "admin_user",
  "email": "missingbearer@example.com",
  "age": 46,
  "created_at": "2025-09-14T12:46:48.906068",
  "is_active": true,
  "phone": "+1917555123456789",
  "last_login": "2025-09-15T19:27:57.124805"
}
```
Screenshot
![PUT-UPDATE-BUG-007](./screenshots/BUG-007.png)

## Test #62 – PUT /users/{selfId} 

Endpoint: PUT /users/{id}
Expected Result: 422 Unprocessable Content with a validation error on email (invalid email format).
Actual Result: 422 Unprocessable Content with message indicating invalid characters in the email (e.g., “The part after the @-sign contains invalid characters: '@'.").
Result: ✅ Pass

Steps to Execute:

1.Set method to PUT, endpoint to /users/{{selfUserId}} (e.g., /users/7).
2.Add headers Content-Type: application/json and Authorization: Bearer {{token}}.
3.In Body → raw → JSON, provide an invalid email (e.g., contains double @).
4.Send the request.
5.Verify status code is 422.
6.Verify response contains a validation error for "email".
**Sample Request Body:**
```json

{
  "email": "new_email@@example.com"
}
```
**Sample Response Body:**
```json

{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "email"],
      "msg": "value is not a valid email address: The part after the @-sign contains invalid characters: '@'.",
      "input": "new_email@@example.com",
      "ctx": {
        "reason": "The part after the @-sign contains invalid characters: '@'."
      }
    }
  ]
}
```
Screenshot
![PUT-UPDATE-selfId](./screenshots/selfId.png)


## Test #63 – PUT /users/{selfId} (Invalid – Basic Auth instead of Bearer)

Endpoint: PUT /users/{id}
Expected Result: 401 Unauthorized + error message (e.g., "Invalid authorization header" or "Authentication required")
Actual Result: 401 Unauthorized + "Invalid authorization header"
Result: ✅ Pass

Steps to Execute:
1.Set method to PUT, endpoint to /users/{{selfUserId}}.
2.In Authorization tab select “Basic Auth” (or add header manually) and set credentials admin_user / Admin@2024.
3.Ensure headers: Content-Type: application/json and Accept: application/json.
4.Provide a simple update body (e.g., phone).
5.Send the request.
6.Verify status code is 401 and response body contains an authorization error message.
Sample Request Headers:

Content-Type: application/json
Accept: application/json
Authorization: Basic YWRtaW5fdXNlcjpBZG1pbkAyMDI0

**Sample Request Body:**
```json

{
  "phone": "+19175551234"
}
```
**Sample Response Body:**
```json

{
  "detail": "Invalid authorization header"
}
```
Screenshot
![PUT-UPDATE-Basic_Auth](./screenshots/Basic_Auth.png)

## Test #64 – PUT /users/{id} (Invalid – Extra field username in body)

Endpoint: PUT /users/11
Expected Result: 422 Unprocessable Content + validation error (immutable/disallowed field username; unexpected fields should be rejected)
Actual Result: 200 OK + request accepted; username was ignored (unchanged) and update succeeded (BUG – extra field not validated/blocked)
Result: ❌ Fail

Steps to Execute:
1.Set method to PUT, endpoint to /users/11.
2.Set Authorization to Bearer {{token}}.
3.Add headers: Content-Type: application/json, Accept: application/json.
4.Body includes an extra immutable field username along with a valid field (e.g., phone).
5.Send the request.
6.Verify the status code and whether an error is returned for the unexpected field.

**Sample Request Body:**
```json

{
  "username": "hacker_takeover",
  "phone": "+19175551234"
}
```
**Sample Response Body:**
```json
{
  "id": 11,
  "username": "new_user",
  "email": "new_user@example.com",
  "age": 25,
  "created_at": "2025-09-14T15:44:47.880142",
  "is_active": true,
  "phone": "+19175551234",
  "last_login": null
}
```
Screenshot
![PUT-UPDATE-BUG-008](./screenshots/BUG-008.png)

## Test #65 – DELETE /users/{id} (Valid – Admin credentials → 200 OK)

Endpoint: DELETE /users/{id}
Expected Result: 200 OK + { "message": "User deleted successfully", "was_active": true }
Actual Result: 200 OK + message returned successfully
Result: ✅ Pass

Steps to Execute:
1.Set method to DELETE, endpoint to /users/11.
2.In Authorization, choose Basic Auth; Username: admin_user, Password: Admin@2024.
3.Optionally ensure header Accept: application/json is present.
4.Leave Body empty (no payload).
5.Send the request.
6.Verify status code is 200.
7.Verify response body contains "message": "User deleted successfully" and "was_active": true.

Sample Request (no body): None

**Sample Response Body:**
```json
{
  "message": "User deleted successfully",
  "was_active": true
}
```
Screenshot
![DELETE-Delete_Admin](./screenshots/Delete_Admin.png)

## Test #66 – DELETE /users/{id} (Invalid – Missing Basic Auth  → 401)

Endpoint: DELETE /users/39
Expected Result: 401 Unauthorized with "detail": "Not authenticated"
Actual Result: 401 Unauthorized with "detail": "Not authenticated"
Result: ✅ Pass

Steps to Execute

1.Set method to DELETE and URL to {{baseUrl}}/users/39.
2.Authorization: No Auth (remove the Authorization header entirely).

Body: none.
**Sample Response Body:**
```json

{
  "detail": "Not authenticated"
}
```
Screenshot
![DELETE-Delete_Missing_Basic_Auth](./screenshots/Delete_Missing_Basic_Auth.png)

## Test #67 – DELETE /users/{id} (Wrong Auth Scheme — Bearer instead of Basic → 401)

Endpoint: DELETE /users/39
Expected Result: 401 Unauthorized with "detail": "Not authenticated" because this endpoint requires Basic Auth and ignores Bearer tokens.
Actual Result: 401 Unauthorized with "detail": "Not authenticated"
Result: ✅ Pass

Steps to Execute:
1.Set method to DELETE, URL: {{baseUrl}}/users/39
2.Authorization: Type = Bearer Token
3.Paste any token (valid or corrupted)
4.Headers: Accept: application/json (optional)
5.Body: none , Send
7.Verify status code is 401 and body contains "detail": "Not authenticated"

Sample Request (headers):
Authorization: Bearer 037d6b5a9450f01deb559cf9a737ce5x
Accept: application/json

**Sample Response Body:**
```json

{ "detail": "Not authenticated" }

```
Screenshot
![DELETE-Delete_Wrong_Auth_Scheme](./screenshots/Delete_Wrong_Auth_Scheme.png)


## Test #68 – DELETE /users/{id} (Invalid – Non-existent user → 404)

Endpoint: DELETE /users/{id}
Expected Result: 404 Not Found + error like "User not found"
Actual Result: 404 Not Found + "detail": "User not found"
Result: ✅ Pass

Steps to Execute:
1.Method DELETE, URL: {{baseUrl}}/users/26585 (use a clearly non-existent id)
2.Authorization: Basic Auth (admin token)
3.Headers: Accept: application/json (optional)
4.Body: none
5.Send and verify status and message
**Sample Response Body:**
```json
{
  "detail": "User not found"
}
```
Screenshot
![DELETE-Delete_Non-existent_user](./screenshots/Delete_Non-existent_user.png)

## Test #69 – DELETE /users/{id} (Idempotent re-delete)

Endpoint: DELETE /users/11
Precondition: User 11 was already deleted in Test #65 (or delete it once first).
Expected Result: 200 OK and a no-op response indicating the user was already inactive, e.g. "was_active": false. The operation must be idempotent (no 404, no state change other than confirming already deleted).
Actual Result: 200 OK with "was_active": false (idempotent confirmed).
Result: ✅ Pass

Steps to Execute:
1.Set method to DELETE, URL {{baseUrl}}/users/11
2.Authorization: Basic (admin_user / Admin@2024)
3.Body: none
4.Send
5.Verify status code 200
6.Verify response contains "was_active": false and message indicates deletion was (already) successful

**Sample Response (first delete):**
```json
{
  "message": "User deleted successfully",
  "was_active": true
}
```

**Sample Response (repeat delete):**
```json
{
  "message": "User deleted successfully",
  "was_active": false
}
```
Follow-up: Test 65-repeat delete idempotent (200, was_active:false)

Screenshot
![DELETE-Delete_Idempotent](./screenshots/Delete_Idempotent.png)

## Test #70 – DELETE /users/{id} (Authorization Gap – Non-admin deletes another user)

Endpoint: DELETE /users/4
Preconditions: A non-admin user exists with known creds ({{attacker_username}} / {{attacker_password}}). ID=4 is a different user (not admin_user and not the attacker).
Expected Result: 403 Forbidden with an authorization error.
Actual Result: 200 OK with { "message": "User deleted successfully", "was_active": true }.
Result: ❌ Fail

Steps to Execute:
1.Set method to DELETE and URL to {{baseUrl}}/users/4
2.Authorization: Basic → Username={{attacker_username}}, Password={{attacker_password}}
3.Headers: Accept: application/json
4.Body: none
5.Send
6.Verify status code should be 403 (observed 200)
7.Verify response body unexpectedly contains "message":"User deleted successfully" and "was_active": true

**Sample Response:**
```json

{
  "message": "User deleted successfully",
  "was_active": true
}
```
Screenshot
![DELETE-Delete_BUG-009](./screenshots/BUG-009.png)

## Test #71 – DELETE /users/{selfId} (Policy – Self-delete should be forbidden)

Endpoint: DELETE /users/{{selfId}} (e.g., /users/41)
Expected Result: 403 Forbidden; account must remain active.
Actual Result: 200 OK with { "message": "User deleted successfully", "was_active": true }.
Result: ❌ Fail

Steps to Execute:
1.Set method to DELETE and URL to {{baseUrl}}/users/{{selfId}} (e.g., /users/41)
2.Authorization: Basic → Username={{self_username}}, Password={{self_password}} (e.g., attacker_1758004274/oldnew1)
3.Headers: Accept: application/json
4.Body: none
5.Send
6.Verify status code should be 403 (observed 200)
7.Verify response erroneously contains "message":"User deleted successfully" and "was_active": true

**Sample Response:**
```json
{
  "message": "User deleted successfully",
  "was_active": true
}
```
Screenshot
![DELETE-Delete_BUG-010](./screenshots/BUG-010.png)

## Test #72 – GET /users/{id} after delete (Observed Soft – 200 + is_active:false)

Endpoint: GET /users/40
Precondition: User 40 was deleted via DELETE /users/40
Expected Result: 200 OK and "is_active": false
Actual Result: 200 OK and "is_active": false
Result: ✅ Pass
Steps to Execute:
1.Set method to GET and URL to {{baseUrl}}/users/40
2.Authorization: No Auth
3.Headers: Accept: application/json
4.Send
5.Verify status code is 200
6.Verify response contains "is_active": false

**Sample Response:**
```json
{
  "id": 40,
  "username": "victim_...",
  "is_active": false
}
```
Screenshot
![DELETE-GET_Check_Observed_Soft](./screenshots/GET_Check_Observed_Soft.png)

## Test #73 – List excludes deleted user (Hard-delete expectation) → Spec mismatch

Endpoint: GET /users?limit=100&offset=0&sort_by=id&order=desc
Precondition: User 40 was deleted via DELETE /users/40
Expected Result: Deleted user should be absent from the list (hard-delete expectation)
Actual Result: User 40 still appears in the list with "is_active": false (soft delete behavior)
Result: ❌ Fail (Spec mismatch – API is soft delete by design)

Steps to Execute:
1.Set method to GET and URL to {{baseUrl}}/users?limit=100&offset=0&sort_by=id&order=desc
2.Authorization: No Auth
3.Headers: Accept: application/json
4.Send
5.Verify user 40 should be absent (hard-delete expectation)
6.Observe user 40 is present with "is_active": false

Sample Observation:
```json
{
  "id": 40,
  "username": "victim_...",
  "is_active": false
}
```
Screenshot
![DELETE-GET-Hard-delete_expectation](./screenshots/GET-Hard-delete_expectation.png)

Note: This is not an implementation bug; it’s a spec decision (soft delete). Consider updating requirements or adding filters to exclude inactive users.

## Test #74 – DELETE /users/{id} (Invalid path format: alpha/SQL Injection attempt → 422)

Endpoint: DELETE /users/{id}
Preconditions: None
Expected Result: 422 Unprocessable Entity when {id} is not an integer (e.g., abc, 1 OR 1=1).
Actual Result: 422 Unprocessable Entity with validation error (int_parsing).
Result: ✅ Pass

Steps to Execute:
1.Set method to DELETE and URL to {{baseUrl}}/users/abc
2.Authorization: Basic (admin_user / Admin@2024)
3.Headers: Accept: application/json
4.Send and verify status 422
5.Set method to DELETE and URL to {{baseUrl}}/users/1%20OR%201=1
6.Authorization: Basic (admin_user / Admin@2024)
7.Headers: Accept: application/json
8.Send and verify status 422

**Sample Response:**
```json
{
  "detail": [
  {
  "type": "int_parsing",
  "loc": [
 "path",
 "user_id"
 ],
"msg": "Input should be a valid integer, unable to parse string as an integer",
 "input": "1 OR 1=1"
 }
]
}
```
Screenshot
![DELETE-Delete_Invalid_path_format](./screenshots/Delete_Invalid_path_format.png)

## Test #75 – POST /users (Rate Limit – 101 requests in 1 minute → 429)

Endpoint: POST /users
Expected Result: First 100 requests return 201 Created; the 101st request within the same 60-second window returns 429 Too Many Requests with {"detail":"Rate limit exceeded"}
Actual Result: First 100 → 201; 101st → 429 with detail: "Rate limit exceeded"
Result: ✅ Pass

Steps to Execute
1.Set method to POST and URL to {{baseUrl}}/users.
2.Add header Content-Type: application/json.
3.Body → raw → JSON; use dynamic values to avoid duplicates (e.g., {{$timestamp}} / {{$randomInt}}).
4.Right-click the single request “POST Create User” (paper-plane icon) and choose Run.
5.In Runner: Iterations=101, Delay=0 ms, keep variables enabled; run the single request only.
6.Verify iterations 1–100 return 201 Created; iteration 101 returns 429 with body {"detail":"Rate limit exceeded"}.
7.Capture the run summary and the 101st response as evidence.

**Sample Request Body:**
```json
{
  "username": "rl_{{$timestamp}}",
  "email": "rl_{{$timestamp}}@example.com",
  "password": "oldnew1",
  "age": 25,
  "phone": "+1555{{$randomInt}}"
}
```

**Sample 429 Response:**
```json
{
  "detail": "Rate limit exceeded"
}
```
Screenshot
![POST-Users_Rate_Limit](./screenshots/Users_Rate_Limit.png)

## Test #76 – POST /login (No Rate Limit → Brute-Force Risk)

Endpoint: POST /login
Expected Result: After multiple failed attempts within a 60-second window, once the threshold (e.g., 100) is exceeded, respond with 429 Too Many Requests (or apply a temporary lockout).
Actual Result: For 101 consecutive failed attempts, every response was 401 Unauthorized; no 429 was returned (no rate limit).
Result: ❌ Fail (Security finding)

Steps to Execute

1.Set method to POST and URL to {{baseUrl}}/login.
2.Body → raw → JSON; provide an invalid password.
3.In the left panel, right-click POST /Login_Wrong_password → Run.
4.In Runner set Iterations = 101, Delay = 0 ms; ensure only this single request is selected.
5.Run and verify all responses are 401 Unauthorized and no 429 appears.
6.Capture the run summary and a few sample responses as evidence.

**Sample Request Body:**
```json

{
  "username": "admin_user",
  "password": "Admin@WRONG"
}
```
Screenshot
![POST-Login_Brute_Force_Risk](./screenshots/Login_Brute_Force_Risk.png)

Note (classification): This is not a functional bug — the rate limiter applies only to POST /users, not to POST /login; returning 401 is expected by design.
Recommendation: Add brute-force protection.

## Test #77 – GET /stats?include_details=true (Info Disclosure: emails & session tokens exposed without auth)

Endpoint: GET /stats?include_details=true
Expected Result: 401/403 unless an admin is authenticated. Even for admins, the response should never return raw user_emails or session_tokens (only aggregated counts).
Actual Result: 200 OK without any authorization; response includes user_emails list and session_tokens array.
Result: ❌ Fail (Security finding – Sensitive Data Exposure / CWE-200, session token exposure → possible account takeover)

Steps to Execute

1.Method GET, URL {{baseUrl}}/stats?include_details=true.
2.Ensure no Authorization header is sent.
3.Send the request; observe 200 OK and presence of "user_emails" and "session_tokens" in the body.

**Sample Response (truncated)**
```json
{
  "total_users": 40,
    "active_users": 35,
    "inactive_users": 5,
    "active_sessions": 3,
    "api_version": "1.0.0",
    "user_emails": [
    "new_userd@example.com",
    "victim_17580032033@example.com",
    "attacker_1758004247@example.com"
  ],
  "session_tokens": [
    "e694542a755bdc1dbd72fba2302f51ac",
    "037d6b5a9450f01deb559cf9a737ce5x",
    "f9d2f43a83be47c176d8a4bf6c1e6738"
  ]
}

```
Screenshot
![GET-Token_BUG-011](./screenshots/BUG-011.png)

## Test #78 – POST /logout (Logout consistency – invalid/missing Bearer returns 200 instead of 401)

Endpoint: POST /logout
Expected Result: When the Authorization header is missing or contains an invalid Bearer token, the API should respond with 401 Unauthorized (or at least the same generic response for both cases).
Actual Result:

Case A (No Auth): 200 OK with {"message":"No active session"}

Case B (Invalid Bearer, e.g., token=deadbeef): 200 OK with {"message":"Logged out successfully"}
Result: ❌ Fail (consistency & security semantics)

Steps to Execute

1.Method POST, URL {{baseUrl}}/logout.
2.Case A – Missing token: Authorization → No Auth → Send → observe 200 OK and body {"message":"No active session"}.
3.Case B – Invalid token: Authorization → Bearer Token, Token=deadbeef → Send → observe 200 OK and body {"message":"Logged out successfully"}.
4.Capture both responses as evidence (screenshots attached).

**Sample Responses**

Case A (No Auth):
```json
{ "message": "No active session" }
```
Case B (Invalid Bearer):

```json
{ "message": "Logged out successfully" }
```
Screenshot
![POST-Logout_BUG-012_A](./screenshots/BUG-012_A.png)
Screenshot
![POST-Logout_BUG-012_B](./screenshots/BUG-012_B.png)

## Test #79 – POST /logout (Positive: session invalidation)

Endpoint: POST /logout
Expected Result:200 OK with body {"message":"Logged out successfully"}.
Any subsequent call to a protected endpoint with the same token returns 401 Unauthorized with "Invalid session".
Actual Result:200 OK + "Logged out successfully" (SS1).
Then PUT /users/{id} with the same token → 401 Unauthorized + "Invalid session" (SS2). ✅
Result: ✅ Pass

Steps

1.Log in via POST /login and capture the token.
2.Send POST {{baseUrl}}/logout with Authorization: Bearer {{token}}.
3.Verify response is 200 OK and message is "Logged out successfully".
4.Reuse the same token on a protected request (e.g., PUT {{baseUrl}}/users/{id}).
5.Verify it returns 401 Unauthorized with "Invalid session".

Sample 200 Response (logout):
```json
{ "message": "Logged out successfully" }
```
Sample 401 Response (after logout):
```json
{ "detail": "Invalid session" }
```
Screenshot
![POST-Logout_check](./screenshots/Logout_check.png)

## Test #80 – GET /health (Positive: session metric reflects login/logout)

Endpoint: GET /health
Expected Result: 200 OK with body containing status, timestamp, memory_users, memory_sessions. After login, memory_sessions_after_login > memory_sessions_baseline. After logout, memory_sessions_after_logout < memory_sessions_after_login.
Actual Result: 200 OK + health payload (SS1). After login, memory_sessions increased (SS2). After logout, memory_sessions decreased (SS3). 
Result: ✅ Pass

Steps
1.GET {{baseUrl}}/health and record memory_sessions as A.
2.POST {{baseUrl}}/login with valid creds, capture token.
3.GET {{baseUrl}}/health again → record memory_sessions as B; verify B > A.
4.POST {{baseUrl}}/logout with Authorization: Bearer {{token}}.
5.GET {{baseUrl}}/health again → record memory_sessions as C; verify C < B.

Sample 200 Response (health):
```json
{
  "status": "healthy",
  "timestamp": "2025-09-16T16:57:26.484620",
  "memory_users": 11406,
  "memory_sessions": 847
}
```
Screenshot
![GET-health_login_logout](./screenshots/health_login_logout.png)

## Test #81 – POST /login (Regression: No lockout after multiple failed attempts)

Endpoint: POST /login
Preconditions: A valid user exists (e.g., username: rl_1758032074, password: oldnew50).
Expected Result: Multiple consecutive invalid logins return 401 Unauthorized with {"detail":"Invalid username or password"}. Immediately after, a valid login succeeds with 200 OK and a 32-char token (no lockout).
Actual Result: 4× 401 Unauthorized for wrong password (SS1–SS4). 5th request with correct password → 200 OK with token, expires_in, user_id (SS5). 
Result: ✅ Pass

Steps
1.POST /login with wrong password 4 times:
Body:
```json
{ "username":"rl_1758032074", "password":"Wrong@123" }
```

Expect: 401 and {"detail":"Invalid username or password"} each time.
2.POST /login with correct password:
Body:
```json
{ "username":"rl_1758032074", "password":"oldnew50" }
```

Expect: 200 OK and JSON with 32-char token, expires_in: 86400, user_id.

Sample 200 Response (successful login)
```json
{ "token": "4a80dab23442938a8bbdf061f54a5a7d", "expires_in": 86400, "user_id": 242 }
```
Screenshot
![POST-Login_Regression](./screenshots/Login_Regression.png)

Notes

Current implementation does not enforce lockout; this test documents that behavior. If the requirement is “lock after N failures,” log as an improvement/bug.
