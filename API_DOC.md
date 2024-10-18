---
# 📦 Custom Nike Air Force 1 Store - API Documentation

This API allows clients to interact with the backend of the **Nike Air Force 1 Store**, including **user management, orders, product information, and shipment tracking** via **The Courier Guy’s API**.
---

## 📑 **Base URL**

For local development:

```
http://127.0.0.1:8000/api/v1/
```

In production:

```
https://your-production-url.com/api/v1/
```

---

## 🧑‍💻 **Authentication**

All protected endpoints require **JWT Token Authentication**.

- Obtain a token by logging in:
  ```
  POST /auth/login/
  ```
- Include the token in requests:
  ```bash
  Authorization: Bearer <your_token>
  ```

---

## 🔐 **Authentication Endpoints**

### 1. **Register a New User**

**POST** `/auth/register/`  
Registers a new user.

#### Request Body:

```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "your_secure_password"
}
```

#### Response:

```json
{
  "message": "User registered successfully.",
  "user": {
    "id": 1,
    "username": "johndoe"
  }
}
```

---

### 2. **User Login**

**POST** `/auth/login/`  
Logs in a user and returns a JWT token.

#### Request Body:

```json
{
  "username": "johndoe",
  "password": "your_secure_password"
}
```

#### Response:

```json
{
  "token": "your_jwt_token"
}
```

---

## 🛍️ **Product Endpoints**

### 1. **List All Products**

**GET** `/products/`  
Retrieves a list of all available Nike Air Force 1 sneakers.

#### Response:

```json
[
  {
    "id": 1,
    "name": "Air Force 1 - Red Edition",
    "price": 1500.0,
    "customizable": true
  },
  {
    "id": 2,
    "name": "Air Force 1 - Blue Edition",
    "price": 1600.0,
    "customizable": true
  }
]
```

---

### 2. **Retrieve Product Details**

**GET** `/products/<product_id>/`  
Fetches details of a specific product.

#### Response:

```json
{
  "id": 1,
  "name": "Air Force 1 - Red Edition",
  "description": "Custom red colorway with leather finish.",
  "price": 1500.0,
  "stock": 10,
  "customizable": true
}
```

---

## 📦 **Order Endpoints**

### 1. **Create an Order**

**POST** `/orders/`  
Places a new order.

#### Request Body:

```json
{
  "product_id": 1,
  "quantity": 2,
  "address": "123 Main Street, Johannesburg",
  "payment_method": "PayFast"
}
```

#### Response:

```json
{
  "message": "Order placed successfully.",
  "order_id": 42,
  "status": "Pending"
}
```

---

### 2. **Get Order Details**

**GET** `/orders/<order_id>/`  
Fetches the details of a specific order.

#### Response:

```json
{
  "order_id": 42,
  "product": "Air Force 1 - Red Edition",
  "quantity": 2,
  "total_price": 3000.0,
  "status": "Shipped",
  "tracking_number": "TGC123456"
}
```

---

## 🚚 **Shipment Tracking Endpoint**

### 1. **Track a Shipment**

**GET** `/shipment/track/<tracking_number>/`  
Fetches the current status of a shipment using **The Courier Guy API**.

#### Response:

```json
{
  "tracking_number": "TGC123456",
  "status": "In Transit",
  "last_update": "2024-10-18 10:00:00",
  "estimated_delivery": "2024-10-21"
}
```

---

## 🔄 **Courier API Integration Example**

Here’s how to call **The Courier Guy’s** API within the backend to track a shipment:

```python
import requests
from django.conf import settings

def track_shipment(tracking_number):
    url = f'https://api.thecourierguy.co.za/v1/track/{tracking_number}'
    headers = {'Authorization': f'Bearer {settings.COURIER_API_KEY}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch tracking data"}
```

---

## 📊 **Admin Endpoints**

### 1. **Add a New Product (Admin)**

**POST** `/admin/products/`

#### Request Body:

```json
{
  "name": "Air Force 1 - Green Edition",
  "description": "Custom green colorway.",
  "price": 1700.0,
  "stock": 15,
  "customizable": true
}
```

#### Response:

```json
{
  "message": "Product added successfully.",
  "product_id": 3
}
```

---

## 💳 **Payment Endpoints**

### 1. **Initiate Payment**

**POST** `/payments/`  
Initiates a payment process.

#### Request Body:

```json
{
  "order_id": 42,
  "amount": 3000.0,
  "payment_method": "PayFast"
}
```

#### Response:

```json
{
  "message": "Payment initiated successfully.",
  "payment_status": "Pending"
}
```

---

## 📛 **Error Codes**

| **Status Code** | **Meaning**                            |
| --------------- | -------------------------------------- |
| 200             | OK – Successful Request                |
| 201             | Created – New Resource Added           |
| 400             | Bad Request – Invalid Data             |
| 401             | Unauthorized – Authentication Required |
| 404             | Not Found – Resource Not Found         |
| 500             | Internal Server Error                  |

---

## 📞 **Support**

For questions or support, contact us at:  
📧 **Email**: matidza46@gmail.com  
📱 **Phone**: ---

This API documentation provides everything a developer needs to integrate and use your Django e-commerce platform effectively. Let me know if you'd like any adjustments!
