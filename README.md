---
## 🛍️ Custom Nike Air Force 1 E-Commerce Website

An e-commerce platform built with **Django** and **PostgreSQL**, offering customers the ability to purchase **customized Nike Air Force 1 sneakers**. This site provides a seamless shopping experience, including **order management, secure payments**, and **shipment tracking** powered by **The Courier Guy API**.
---

### 📋 Features

- **User Authentication**:
  - Secure login and registration.
  - User profiles with order history.
- **Product Customization**:
  - Choose different colors, patterns, and accessories for Nike Air Force 1 sneakers.
- **Product Management**:
  - Admin dashboard to add, edit, or delete products.
- **Order Tracking**:
  - Real-time tracking through **The Courier Guy’s API**.
- **Payment Integration**:
  - Secure payments with popular gateways (e.g., PayFast, Stripe).
- **PostgreSQL Database**:
  - Robust and scalable data management.
- **Mobile-Friendly UI**:
  - Fully responsive design for a smooth shopping experience on all devices.

---

### 🚀 Getting Started

#### Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **Django 4.x**
- **PostgreSQL**
- **Virtualenv** (recommended for virtual environment setup)

#### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/nike-air-force-1-store.git
   cd nike-air-force-1-store
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**

   - Create a new PostgreSQL database and user.
   - Add your database credentials to `settings.py` or use **environment variables**:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_db_name',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Website**  
   Visit `http://127.0.0.1:8000/` in your browser.

---

### 🔗 Integrating The Courier Guy API

1. **API Setup**:

   - Register for an API key from **The Courier Guy** [here](https://www.thecourierguy.co.za/).
   - Add the API key to your environment variables:
     ```bash
     export COURIER_API_KEY='your_api_key'
     ```

2. **Shipment Tracking Integration**:

   - Use the API to fetch tracking updates by calling the endpoint:

     ```python
     import requests

     def track_shipment(tracking_number):
         url = f'https://api.thecourierguy.co.za/v1/track/{tracking_number}'
         headers = {'Authorization': f'Bearer {COURIER_API_KEY}'}
         response = requests.get(url, headers=headers)
         return response.json()
     ```

---

### 🧑‍💻 Project Structure

```
nike-air-force-1-store/
│
├── manage.py            # Django management script
├── requirements.txt     # List of dependencies
├── .env                 # Environment variables
├── db.sqlite3           # Local development database
│
├── store/               # Main Django app
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, Images
│   ├── models.py        # Database models
│   ├── views.py         # Views logic
│   └── urls.py          # URL routes
│
└── README.md            # Project documentation
```

---

### 🛠️ Technologies Used

- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Payment Gateways**: PayFast / Stripe
- **Shipment API**: The Courier Guy
- **Frontend**: HTML, CSS, Bootstrap

---

### 🐛 Troubleshooting

- **Database Connection Error**:  
  Ensure PostgreSQL is installed and the database credentials are correct.
- **Missing Dependencies**:  
  Run `pip install -r requirements.txt` again if any dependencies are missing.
- **API Authentication Issues**:  
  Double-check your **API key** and ensure it is added to the environment variables.

---

### 🙌 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

### 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

### 📞 Contact

If you have any questions, feel free to reach out at:  
📧 **Email**: matidza46@gmail.com  
📱 **Phone**:

---

Let me know if you’d like to make any changes or add more details!
