import firebase_admin
from firebase_admin import credentials, firestore, auth
import time

# Initialize Firestore and Firebase Authentication
cred = credentials.Certificate("../serviceAccountKey.json") 
firebase_admin.initialize_app(cred)

db = firestore.client()

### User Authentication
def register_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print(f"User {email} registered successfully! UID: {user.uid}")
    except Exception as e:
        print(f"Error: {e}")

def login_user(email, password):
    # Firebase Admin SDK does not support authentication login.
    print(f"Use Firebase SDK in frontend to log in user {email} with password {password}")

def logout_user(email):
    """ Logout the user (client-side only) """
    print(f"✅ {email} logged out successfully!")


### CRUD Operations for Products
def add_product(product_id, name, description, price, user_id):
    """ Add product to Firestore under 'products' collection """
    doc_ref = db.collection("products").document(product_id)
    doc_ref.set({
        "name": name,
        "description": description,
        "price": price,
        "user_id": user_id  # Link product to user
    })
    print(f"Product '{name}' added successfully!")

def get_all_products():
    """ Retrieve and display all products """
    products = db.collection("products").stream()
    print("\n--- Product List ---")
    for product in products:
        data = product.to_dict()
        print(f"{product.id}: {data['name']} - ${data['price']} (Owner: {data['user_id']})")

def update_product(product_id, new_name=None, new_price=None):
    """ Update product details """
    doc_ref = db.collection("products").document(product_id)
    update_data = {}
    if new_name:
        update_data["name"] = new_name
    if new_price:
        update_data["price"] = new_price
    if update_data:
        doc_ref.update(update_data)
        print(f"Product '{product_id}' updated successfully!")

def delete_product(product_id):
    """ Delete a product """
    db.collection("products").document(product_id).delete()
    print(f"Product '{product_id}' deleted successfully!")

### Real-time Notifications
def listen_for_changes():
    """ Listen for real-time Firestore updates """
    def on_snapshot(col_snapshot, changes, read_time):
        print("\n🔔 Firestore Update Detected:")
        for change in changes:
            if change.type.name == 'ADDED':
                print(f"New Product Added: {change.document.id}")
            elif change.type.name == 'MODIFIED':
                print(f"Product Updated: {change.document.id}")
            elif change.type.name == 'REMOVED':
                print(f"Product Deleted: {change.document.id}")

    col_query = db.collection("products")
    col_query.on_snapshot(on_snapshot)

### Example Usage
if __name__ == "__main__":
    # Register and Authenticate Users
    register_user("omaje1223@gmail.com", "password123")

    # Perform CRUD operations
    add_product("p1", "Laptop", "Gaming Laptop", 1500.00, "user@example.com")
    add_product("p2", "Headphones", "Noise Cancelling", 250.00, "jonathaman27@gmail.com")
    add_product("p3", "Smartphone", "Latest Model", 800.00, "joel@gmail.com")
    add_product("p4", "Tablet", "Powerful Tablet", 500.00, "user@example.com")

    get_all_products()

    update_product("p1", new_price=1800.00)
    update_product("p2", new_name="Earphones")
    delete_product("p3")

    # Listen for real-time changes (Run this separately)
    listen_for_changes()

    # Keep the script running to receive updates
   
    time.sleep(1)

    