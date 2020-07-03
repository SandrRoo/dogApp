class Owner:
	'''
	Owner information.
	Includes first name, last name, full address, phome mumber, and email address.
	'''

	def __init__(self, owner_id, first_name, last_name, address_line_1, address_line_2, state, country, zip_code, phone_number, email_address, notes = None):
		self.owner_id = owner_id
		self.first_name = first_name
		self.last_name = last_name
		self.address_line_1 = address_line_1
		self.address_line_2 = address_line_2
		self.state = state
		self.country = country
		self.zip_code = zip_code
		self.phone_number = phone_number
		self.email_address = email_address
		self.notes = notes

	def update_info(first_name, last_name, address_line_1, address_line_2, state, country, zip_code, phone_number, email_address, notes = None):
		self.first_name = first_name
		self.last_name = last_name
		self.address_line_1 = address_line_1
		self.address_line_2 = address_line_2
		self.state = state
		self.country = country
		self.zip_code = zip_code
		self.phone_number = phone_number
		self.email_address = email_address
		self.notes = notes


	
