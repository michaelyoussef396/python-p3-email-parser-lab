# your code goes here!import re
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the string by commas or spaces
        addresses = re.split(r'[,\s]+', self.email_addresses)
        # Remove any empty strings
        addresses = [email for email in addresses if email]
        # Return unique addresses, sorted alphabetically
        return sorted(set(addresses))
