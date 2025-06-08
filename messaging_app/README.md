# Messaging API Documentation

## 📌 Overview

This API provides a backend for a messaging application. It includes features such as user registration and authentication, conversation creation between users, and sending/retrieving messages within those conversations.

---

## 🔐 Authentication

* Authentication is handled using **JWT (JSON Web Tokens)**.
* Obtain tokens via `/api/auth/login/` and use the `access` token in the Authorization header for all protected endpoints.

**Example:**

```http
Authorization: Bearer <access_token>
```

---

## 🚀 Endpoints

### 👤 User Authentication

| Method | Endpoint              | Description                               |
| ------ | --------------------- | ----------------------------------------- |
| `POST` | `/api/auth/register/` | Register a new user                       |
| `POST` | `/api/auth/login/`    | Login user and return JWT tokens          |
| `POST` | `/api/auth/refresh/`  | Refresh JWT token                         |
| `GET`  | `/api/auth/profile/`  | Retrieve the authenticated user's profile |

### 💬 Conversations

| Method          | Endpoint               | Description                                         |
| --------------- | ---------------------- | --------------------------------------------------- |
| `GET`           | `/conversations/`      | List all conversations the user is in               |
| `POST`          | `/conversations/`      | Create a new conversation (provide participant IDs) |
| `GET`           | `/conversations/{id}/` | Get details of a specific conversation              |
| `PUT` / `PATCH` | `/conversations/{id}/` | Update a conversation (if supported)                |
| `DELETE`        | `/conversations/{id}/` | Delete a conversation (if supported)                |

**POST Example Body:**

```json
{
  "participants": ["user_id_1", "user_id_2"]
}
```

### 📨 Messages (Nested under Conversations)

| Method          | Endpoint                                          | Description                              |
| --------------- | ------------------------------------------------- | ---------------------------------------- |
| `GET`           | `/conversations/{conversation_id}/messages/`      | List all messages in a conversation      |
| `POST`          | `/conversations/{conversation_id}/messages/`      | Send a new message in a conversation     |
| `GET`           | `/conversations/{conversation_id}/messages/{id}/` | Get a specific message                   |
| `PUT` / `PATCH` | `/conversations/{conversation_id}/messages/{id}/` | Update a specific message (if supported) |
| `DELETE`        | `/conversations/{conversation_id}/messages/{id}/` | Delete a message                         |

**POST Example Body:**

```json
{
  "content": "Hey, how are you?"
}
```

---

## 🧪 Testing the API

1. Register a user via `/api/auth/register/`
2. Log in with the same credentials using `/api/auth/login/` and store the access token.
3. Use that token in the `Authorization` header to access protected routes like conversations or messages.

---

## ⚙️ Tech Stack

* Python 3.12
* Django & Django REST Framework
* JWT Authentication via SimpleJWT
* RESTful routing via DRF Routers (including nested routers)

---

## 📫 Contact

If you have questions or encounter bugs, feel free to open an issue or contact the developer.

---

## 📝 License

This project is open-source and available under the MIT License.
