import uuid

class UserStorage:
    # In-memory storage using a dictionary (hashmap)
    users = {}

    @classmethod
    def get_all_users(cls):
        """Return a list of all users."""
        return list(cls.users.values())

    @classmethod
    def get_user(cls, user_id):
        """Retrieve a user by their ID."""
        return cls.users.get(str(user_id))

    @classmethod
    def create_user(cls, user_data):
        """Create a new user and store it in memory."""
        user_id = uuid.uuid4()  # Generate a unique UUID for the user
        user = {
            'id': user_id,
            'name': user_data['name'],
            'email': user_data['email'],
            'age': user_data['age']
        }
        cls.users[str(user_id)] = user  # Store the user in the dictionary
        return user

    @classmethod
    def update_user(cls, user_id, user_data):
        """Update an existing user."""
        user = cls.get_user(user_id)
        if user:
            user.update(user_data)  # Update the user's data
            return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        """Delete a user by their ID."""
        if str(user_id) in cls.users:
            del cls.users[str(user_id)]
            return True
        return False