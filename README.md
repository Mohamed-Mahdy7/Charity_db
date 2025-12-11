# Charity Management System – Backend (Django & Django REST Framework)

This project is a complete backend system for a **Charity Organization Website**, implemented using **Python (Django + DRF)**.  
It includes full database design, authentication, multilingual support preparation, and donation system structure.

---

## **Project Overview**

This backend powers a charity website that manages:

- Projects & fundraising campaigns  
- Donations (linked to projects & payment method)  
- Volunteers  
- Articles & news  
- Admin accounts with permissions  
- Public pages (About, Contact, etc.)  
- Highly structured database  
- Optimized API performance  
- Secure authentication using JWT

---

## **Tech Stack**

| Layer | Technology |
|------|------------|
| Backend Framework | **Django 5 + Django REST Framework** |
| Authentication | **Djoser + JWT (SimpleJWT)** |
| Database | MySQL|
| Media Handling | Django Media Storage |
| API Format | REST / JSON |

---

# **Database Structure (Models)**

The project contains the following main modules:

### **Users / Admins**
- Username  
- Email  
- Password  
- Role (Admin / Staff)  
- Permissions  
- Created/Updated timestamps  

### **Projects**
- Title (AR/EN)
- Description (AR/EN)
- Target Amount & Collected Amount
- Status (Active / Completed / Paused)
- Start date – End date
- Cover image
- Multiple project photos

### **Donations**
- Donor name (optional)
- Amount
- Payment method
- Donation status
- Related project (FK)

### **Volunteers**
- Name  
- Phone  
- Skills  
- Participation type  
- Status  

### **Articles / News**
- Title  
- Content  
- Image  
- Publish date  

### **Project Photos**
- Photo  
- FK → Project  

---

# **Authentication System**

Authentication is implemented using:

### ✔ **Djoser**
Handles:
- Registration
- Activation
- User management

### ✔ **JWT Authentication**
Using:  
```
djangorestframework-simplejwt
```

Provides:
- access token  
- refresh token  
- Auto token refresh  
- Secured, stateless API authentication  

### **Authentication Endpoints Provided by Djoser + JWT**

| Endpoint | Description |
|----------|-------------|
| `POST /register/` | Register |
| `POST /login/` | Login |
| `POST /auth/jwt/refresh/` | Refresh token |
| `POST /auth/jwt/verify/` | Verify token |

---

# 🚀 **Project Structure**

```
charity_backend/
│
├── charity/                # Project root
│   ├── settings.py         # Settings + JWT + Djoser config
│   ├── urls.py             # Main URLs
│   ├── wsgi.py
│
├── users/                  # Authentication App
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│
├── projects/               # Projects, Photos
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── donations/
│   ├── models.py
│   ├── serializers.py
│
├── volunteers/
│   ├── models.py
│   ├── serializers.py
│
├── articles/
│   ├── models.py
│   ├── serializers.py
│
├── main/
│   ├── models.py
│   ├── serializers.py
│
└── README.md
```

---

# ⚙️ **Settings (Authentication Setup)**

### Install Required Packages

```
pip install djangorestframework
pip install djoser
pip install djangorestframework-simplejwt
pip install psycopg2
```

### Add to `settings.py`

```python
INSTALLED_APPS = [
    'rest_framework',
    'djoser',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'core',
    'projects',
    'donations',
    'volunteers',
    'articles',
    'main',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

DJOSER = {
    "USER_CREATE_PASSWORD_RETYPE": True,
    "LOGIN_FIELD": "email",
}
```

Add URLs:

```python
# charity/urls.py

path("auth/", include("djoser.urls.jwt")),
```

---

# 🌍 **API Endpoints Overview**

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register/` | Register |
| POST | `/login/` | Login |
| POST | `/auth/jwt/refresh/` | Refresh Token |

---

# **Security & Best Practices**

- JWT-based authentication  
- Input validation using DRF Serializers  
- SQL injection protection (ORM)  
- Safe password hashing  

---


# Summary

In this backend we have:

✔ Full database system  
✔ Authentication (Djoser + JWT)  
✔ Donation system  
✔ Project & volunteers module  
✔ Articles/news handling  
✔ Contact messages API  
✔ Clean, scalable Django architecture  
