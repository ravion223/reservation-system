# In your app directory, create a directory named 'management'
# Inside 'management', create another directory named 'commands'
# Inside 'commands', create a Python file named 'create_rooms.py'

# File: create_rooms.py
import random
from string import ascii_uppercase
from django.core.management.base import BaseCommand
from hotel.models import Room

class Command(BaseCommand):
    help = 'Create rooms'

    def handle(self, *args, **kwargs):
        # 50 countries
        countries = [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", 
            "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", 
            "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
            "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", 
            "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", 
            "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", 
            "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic"
            # Add more countries as needed
        ]

        # 50 unique descriptions
        descriptions = [
            "This is a cozy room suitable for small meetings.",
            "Spacious room with natural lighting.",
            "A modern conference room with state-of-the-art equipment.",
            "Comfortable room for workshops and seminars.",
            "Executive boardroom with a stunning view.",
            "Elegant space for corporate events.",
            "Versatile room perfect for training sessions.",
            "Intimate setting for business negotiations.",
            "Inspiring environment for creative brainstorming.",
            "Professional setup for presentations.",
            # Add more descriptions as needed
        ]

        for i in range(50):
            room_letter = random.choice(ascii_uppercase)  # Random uppercase letter
            room_number = random.randint(1, 99)  # Generate random room number between 1 and 99
            room_name = f"{room_letter}-{room_number}"  # Combine letter and number
            capacity = random.randint(1, 10)  # Generate random capacity not more than 10
            country = random.choice(countries)  # Random country
            description = random.choice(descriptions)  # Random description

            # Create the room
            Room.objects.create(
                number=room_name,
                capacity=capacity,
                location=country,
                description=description
            )

        self.stdout.write(self.style.SUCCESS('Rooms created successfully.'))
