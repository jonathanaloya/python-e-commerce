# Overview

In this project, I developed an e-commerce platform that integrates with Firebase Firestore, a cloud-based NoSQL database. The goal was to create a scalable and real-time data-driven application that allows users to register, log in, and manage product listings with full CRUD (Create, Read, Update, Delete) functionality.

This software provides a seamless experience for users to add, update, and delete products while keeping data synchronized across multiple devices through Firestore's real-time capabilities. Additionally, real-time notifications inform users of any changes to the database.

This software provides a seamless experience for users to add, update, and delete products while keeping data synchronized across multiple devices through Firestore's real-time capabilities. Additionally, real-time notifications inform users of any changes to the database.

    To use this program:

1. Register a new account using an email and password.

2. Log in with valid credentials to access and manage products.

3. Add new products to the database with relevant details.

4. Update or delete existing product listings.

5. Receive real-time updates whenever changes occur in the product collection.

[Software Demo Video](https://youtu.be/80dL73KdJWU)

# Cloud Database

The project utilizes Firebase Firestore, a cloud-based NoSQL database by Google. Firestore supports real-time data syncing, making it an excellent choice for applications requiring immediate updates across multiple users.

Users Collection: Stores user authentication details such as email and UID.

Products Collection: Contains product listings with attributes such as:

name: Product name

description: Product description

price: Product price

user_id: The owner of the product listing

Real-time Listeners: Listens for changes in the database and notifies users of updates in the product collection.

# Development Environment

        Tools Used:

Programming Language: Python

Cloud Database: Firebase Firestore

Authentication: Firebase Authentication (via Firebase Admin SDK)

        Libraries Used:

firebase-admin for Firestore database operations and authentication

time for handling time delays

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Wikipedia Cloud database](https://en.wikipedia.org/wiki/Cloud_database)
- [Firebase](https://www.youtube.com/watch?v=v_hR4K4auoQ&list=PLl-K7zZEsYLluG5MCVEzXAQ7ACZBCuZgZ)
- [Google Cloud Console](https://console.cloud.google.com/welcome?invt=Abtx3w&project=commanding-fact-450907-e8)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Implement frontend authentication using Firebase Authentication SDK.

- Improve user interface by integrating a web or mobile frontend.

- Add image upload functionality for product listings.

- Enhance error handling for better user experience.

- Implement role-based access control (RBAC) to limit permissions based on user roles.