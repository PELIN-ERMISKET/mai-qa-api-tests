## BUG-001: Username Case Sensitivity Not Enforced

Severity: High
Category: Validation / Security

Description:
The API allows creation of usernames that differ only by letter case (e.g., John_Doe vs john_doe). This can cause account duplication, authentication confusion, and potential security loopholes.

Steps to Reproduce:

1.Create a user with username john_doe.

2.Create another user with username John_Doe.

3.Observe the response.

Expected Result:
The API should reject the second request with an error such as "Username already exists", treating usernames as case-insensitive.

Actual Result:
The API accepts both requests, allowing two distinct users with john_doe and John_Doe.

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