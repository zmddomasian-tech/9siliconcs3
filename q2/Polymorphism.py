class Patient:
    def __init__(self, name: str, bill_amount: float):
      self.name = name
      self.bill_amount = float(bill_amount)

    def get_name(self):
      print(f"Patient Name: {self.name}")
      return self. name

    def set_name(self, name: str):
      self.name = name

    def get_bill_amount(self):
      print(f"Original Bill: {self.bill_amount}")
      return self.bill_amount

    def set_bill_amount(self, bill_amount: float):
      self.bill_amount = float(bill_amount)

    def calculate_bill(self):
      print(f"Final  Bill: {self.bill_amount}")
      return self.bill_amount

    def display_patient_type(self):
      print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
      #apply discount
      print(f"Final  Bill: {self.bill_amount  * 0.80}")

    def display_patient_type(self):
      print("Patient Type: Senior Citizen")

class PhilHealthPatient(Patient):
    def calculate_bill(self):
      #apply discount
      print(f"Final  Bill: {self.bill_amount * 0.85}")

    def display_patient_type(self):
      print("Patient Type: PhilHealth Member")
