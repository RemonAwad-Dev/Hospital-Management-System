# ================== Patients ==================

class Patients:
    def __init__(self, patient_id, name, age, gender, disease, visit_type="first"):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.visit_type = visit_type

    def show_patient(self):
        return {
            "id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "disease/reason": self.disease,
            "visit type": self.visit_type,
        }

patients = [
    Patients(1, "ali", 30, "male", "flu"),
    Patients(2, "sara", 25, "female", "fever"),
]
patient_id_counter = len(patients) + 1
waiting = []

def add_patient():
    global patient_id_counter
    patient_id = patient_id_counter
    patient_id_counter += 1

    name = input("Enter patient name: ").lower()
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ").lower()
    disease = input("Enter patient disease or reason for coming: ").lower()
    visit_type = input("Enter visit type (first/consultation): ").lower()
    patient = Patients(patient_id, name, age, gender, disease, visit_type)
    patients.append(patient)
    print("Patient added successfully!")

def view_patients():
    for p in patients:
        print(p.show_patient())

def find_patient():
    patient_id = int(input("Enter patient id: "))
    for patient in patients:
        if patient.show_patient()["id"] == patient_id:
            print(patient.show_patient())
            break
    else:
        print("Patient not found")


def update_patient():
    patient_id = int(input("Enter patient id to update: "))
    for p in patients:
        if p.show_patient()["id"] == patient_id:
            choice = input("What do you want to update (disease/visit type)? ").lower()
            if choice == "disease":
                new_disease = input("Enter new disease: ")
                p.disease = new_disease
            elif choice == "visit type":
                new_visit_type = input("Enter new visit type: ")
                p.visit_type = new_visit_type
            else:
                print("Invalid input")
                return
            print("Patient updated successfully!")
            break
    else:
        print("Patient not found!")


def remove_patient():
    patient_id = int(input("Enter patient id to remove: "))
    for p in patients:
        if p.show_patient()["id"] == patient_id:
            patients.remove(p)
            print("Patient removed successfully!")
            break
    else:
        print("Patient not found")


def add_to_waiting():
    patient_id=int(input("Enter patient id to add to waiting: "))
    for p in patients:
        if p.show_patient()["id"]==patient_id:
            if p not in waiting:
                waiting.append(p)
                print("Patient added to waiting list")
                return
            else:
                print("Patient already in waiting list")
                return
    print("Patient not found")

def remove_from_waiting():
    if waiting:
        removed_patient = waiting.pop(0)
        print(f"Patient removed from waiting list: {removed_patient.name}")
    else:
        print("Waiting list is empty")

def emergency_addition():
    patient_id=int(input("Enter patient id to add to the front of the waiting list: "))
    for p in patients:
        if p.show_patient()["id"]==patient_id:
            if p not in waiting:
                waiting.insert(0,p)
                print("Patient added to the front of waiting list")
                return
            else:
                print("Patient already in waiting list")
                return
    print("Patient not found")

def view_waiting_list():
    if not waiting:
        print("Waiting list is empty")
        return
    for w in waiting:
        print(w.show_patient())

# ================== Doctors ==================

class Doctors:
    def __init__(self, doctor_id, name, specialty, years_of_experience, available_days):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.years_of_experience = years_of_experience
        self.available_days = available_days

    def show_doctor(self):
        return {
            "id": self.doctor_id,
            "name": self.name,
            "specialty": self.specialty,
            "years of experience": self.years_of_experience,
            "available_days": self.available_days,
        }

doctors = [
    Doctors(1, "ahmed", "cardiology", 10, ["monday", "wednesday"]),
    Doctors(2, "mona", "pediatrics", 7, ["tuesday", "thursday"]),
]
doctor_id_counter = len(doctors) + 1

def add_doctor():
    global doctor_id_counter
    doctor_id = doctor_id_counter
    doctor_id_counter += 1

    name = input("Enter doctor name: ").lower()
    specialty = input("Enter doctor specialty: ").lower()
    years_of_experience = int(input("Enter doctor's years of experience: "))
    available_days = input("Enter doctor's available days: ").split()
    doctor = Doctors(doctor_id, name, specialty, years_of_experience, available_days)
    doctors.append(doctor)
    print("Doctor added successfully!")

def find_doctor():
    doctor_id = int(input("Enter doctor id: "))
    for d in doctors:
        if d.show_doctor()["id"] == doctor_id:
            print(d.show_doctor())
            return
    print("Doctor not found")

def remove_doctor():
    doctor_id = int(input("Enter doctor id to remove: "))
    for d in doctors:
        if d.show_doctor()["id"] == doctor_id:
            doctors.remove(d)
            print("Doctor removed successfully!")
            return
    print("Doctor not found")

def update_doctor():
    doctor_id = int(input("Enter doctor id to update: "))
    for d in doctors:
        if d.show_doctor()["id"] == doctor_id:
            choice = input("What do you want to update (specialty/experience/available days)? ").lower()
            if choice == "specialty":
                d.specialty = input("Enter new specialty: ").strip()
            elif choice == "experience":
                d.years_of_experience = int(input("Enter new years of experience: "))
            elif choice == "available days":
                d.available_days = input("Enter new available days: ").split()
            else:
                print("Invalid input")
                return
            print("Doctor updated successfully!")
            return
    print("Doctor not found!")

def check_doctor_availability():
    doctor_id = int(input("Enter doctor id to check availability: "))
    for d in doctors:
        if d.show_doctor()["id"] == doctor_id:
            print(f"Doctor {d.name} is available on {' '.join(d.available_days)}")
            return
    print("Doctor not found")

# ================== Pharmacy ==================

class Pharmacy:
    def __init__(self, medicine_id, medicine_name, medicine_price, expiry_date, size):
        self.medicine_id = medicine_id
        self.medicine_name = medicine_name
        self.medicine_price = medicine_price
        self.expiry_date = expiry_date
        self.size = size

    def show_medicine(self):
        return {
            "id": self.medicine_id,
            "name": self.medicine_name,
            "price": self.medicine_price,
            "expiry_date": self.expiry_date,
            "size": self.size
        }

medicines = [
    Pharmacy(1, "paracetamol", 20, "01/01/2026", "small"),
    Pharmacy(2, "ibuprofen", 35, "01/06/2025", "large"),
]
medicine_id_counter = len(medicines) + 1

def add_medicine():
    global medicine_id_counter
    medicine_id = medicine_id_counter
    medicine_id_counter += 1

    medicine_name = input("Enter medicine name : ").lower().strip()
    medicine_price = int(input("Enter medicine price: "))
    expiry_date = input("Enter medicine Expiry date (DD/MM/YYYY): ")
    size = input("Enter medicine size (Large/Small): ").lower().strip()
    medicine = Pharmacy(medicine_id, medicine_name, medicine_price, expiry_date, size)
    medicines.append(medicine)
    print("Medicine added successfully!")

def update_medicine():
    medicine_id = int(input("Enter medicine id: "))
    for f in medicines:
        if f.show_medicine()["id"] == medicine_id:
            choice = input("What do you want to update (price/expiry date): ").lower().strip()
            if choice == "price":
                f.medicine_price = int(input("Enter new price: "))
            elif choice == "expiry date":
                f.expiry_date = input("Enter new expiry date (DD/MM/YYYY): ")
            else:
                print("Invalid choice!")
                return
            print("Medicine updated successfully!")
            return
    print("Medicine id not found.")

def remove_medicine():
    medicine_id = int(input("Enter medicine id: "))
    for f in medicines:
        if f.show_medicine()["id"] == medicine_id:
            medicines.remove(f)
            print("Medicine removed successfully!")
            return
    print("Medicine id not found")

# ================== Nurses ==================

class Nurses:
    def __init__(self, nurse_id, name, age, gender, specialty, nurse_shift, working_hours, available_days):
        self.nurse_id = nurse_id
        self.name = name
        self.age = age
        self.gender = gender
        self.specialty = specialty
        self.nurse_shift = nurse_shift
        self.working_Hours = working_hours
        self.available_days = available_days

    def show_nurse(self):
        return {
            "id": self.nurse_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "specialty": self.specialty,
            "nurse_shift": self.nurse_shift,
            "working_Hours": self.working_Hours,
            "available_days": self.available_days,
        }

nurses = [
    Nurses(1, "laila", 28, "female", "icu nurse", "morning", 8, ["sunday", "monday"]),
    Nurses(2, "omar", 35, "male", "surgical nurse", "night", 10, ["tuesday", "friday"]),
]
nurse_id_counter = len(nurses) + 1

def add_nurse():
    global nurse_id_counter
    nurse_id = nurse_id_counter
    nurse_id_counter += 1

    name = input("Enter nurse name: ").strip().lower()
    age = int(input("Enter nurse age: "))
    gender = input("Enter nurse gender (male/female): ").lower().strip()
    specialty = input("Enter nurse specialty: ").lower().strip()
    nurse_shift = input("Enter nurse shift (morning/night/evening): ").lower().strip()
    working_hours = int(input("Enter nurse working hours: "))
    available_days = input("Enter nurse available days (separated by space): ").strip().lower().split()

    nurse = Nurses(nurse_id, name, age, gender, specialty, nurse_shift, working_hours, available_days)
    nurses.append(nurse)
    print("Nurse added successfully!")


def update_nurse():
    nurse_id = int(input("Enter nurse id: "))
    for f in nurses:
        if f.show_nurse()["id"] == nurse_id:
            choice = input(
                "What do you want to update (specialty/nurse_shift/working_Hours/available_days): ").lower().strip()

            if choice == "specialty":
                new_specialty = input(f"Enter new specialty {choice}: ").strip().lower()
                f.specialty = new_specialty
                print("Nurse updated successfully!")
                break
            elif choice == "nurse_shift":
                new_nurse_shift = input(f"Enter new nurse shift {choice}: ").strip().lower()
                f.nurse_shift = new_nurse_shift
                print("Nurse updated successfully!")
                break
            elif choice == "working_hours":
                new_working_hours = int(input(f"Enter new working hours {choice}: "))
                f.working_Hours = new_working_hours
                print("Nurse updated successfully!")
                break
            elif choice == "available_days":
                new_available_days = input(f"Enter new available days {choice}: ").strip().lower()
                f.available_days = new_available_days
                print("Nurse updated successfully!")
                break
            else:
                print("Invalid choice!")
                break
    else:
        print("Nurse id not found.")


def remove_nurse():
    nurse_id = int(input("Enter nurse id: "))
    for f in nurses:
        if f.show_nurse()["id"] == nurse_id:
            nurses.remove(f)
            print("Nurse removed successfully!")
            break
    else:
        print("Nurse id not found.")


def show_available_days():
    nurse_id = int(input("Enter nurse id: "))
    for f in nurses:
        if f.show_nurse()["id"] == nurse_id:
            print(f"Nurse {f.name} is available on {' '.join(f.available_days)}")
            break
    else:
        print("Nurse id not found.")


# ================== Appointments & Billing ==================

class Appointments:
    def __init__(self):
        self.appointments = []
        self.bills = []

    def book_appointment(self):
        name = input("Enter patient name: ")
        doctor = input("Enter doctor name: ")
        date = input("Enter appointment date (DD/MM/YYYY): ")
        time = input("Enter appointment time (HH:MM): ")

        appointment = {
            "name": name,
            "doctor": doctor,
            "date": date,
            "time": time
        }
        self.appointments.append(appointment)
        print("\nAppointment booked successfully!\n")

    def view_appointments(self):
        if not self.appointments:
            print("\nNo appointments found.\n")
            return

        print("\n--- Appointments ---")
        for i, app in enumerate(self.appointments, start=1):
            print(f"{i}. {app['name']} - {app['doctor']} - {app['date']} - {app['time']}")
        print()

    def create_bill(self):
        patient = input("Enter patient name: ")
        amount = float(input("Enter total amount: "))
        date = input("Enter bill date (DD/MM/YYYY): ")

        bill = {
            "patient": patient,
            "amount": amount,
            "date": date
        }
        self.bills.append(bill)
        print("\nBill created successfully!\n")

    def view_bills(self):
        if not self.bills:
            print("\nNo bills available.\n")
            return

        print("\n--- Bills ---")
        for i, b in enumerate(self.bills, start=1):
            print(f"{i}. {b['patient']} - {b['amount']} - {b['date']}")
        print()

appointments = Appointments()

# ================== Menus ==================

def patients_menu():
    while True:
        print("\n--- Patients Menu ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. find patient")
        print("4. update patient")
        print("5. remove patient")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            find_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            remove_patient()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

def doctors_menu():
    while True:
        print("\n--- Doctors Menu ---")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Find Doctor")
        print("4. Remove Doctor")
        print("5. Update Doctor")
        print("6. Check Availability")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_doctor()
        elif choice == "2":
            for d in doctors:
                print(d.show_doctor())
        elif choice == "3":
            find_doctor()
        elif choice == "4":
            remove_doctor()
        elif choice == "5":
            update_doctor()
        elif choice == "6":
            check_doctor_availability()
        elif choice == "7":
            break
        else:
            print("Invalid choice! Please try again.")

def nurses_menu():
    while True:
        print("\n--- Nurses Menu ---")
        print("1. Add Nurse")
        print("2. View Nurses")
        print("3. View Patients")
        print("4. update Nurse")
        print("5. remove Nurse")
        print("6. show available days")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_nurse()
        elif choice == "2":
            for n in nurses:
                print(n.show_nurse())
        elif choice == "3":
            view_patients()
        elif choice == "4":
            update_nurse()
        elif choice == "5":
            remove_nurse()
        elif choice == "6":
            show_available_days()
        elif choice == "7":
            break
        else:
            print("Invalid choice! Please try again.")

def medicines_menu():
    while True:
        print("\n--- Medicines Menu ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Remove Medicine")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_medicine()
        elif choice == "2":
            for m in medicines:
                print(m.show_medicine())
        elif choice == "3":
            update_medicine()
        elif choice == "4":
            remove_medicine()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

def appointments_menu():
    while True:
        print("\n--- Appointments & Billing Menu ---")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Create Bill")
        print("4. View Bills")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            appointments.book_appointment()
        elif choice == "2":
            appointments.view_appointments()
        elif choice == "3":
            appointments.create_bill()
        elif choice == "4":
            appointments.view_bills()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

def emergency_department():
    while True:
        print("\n--- Emergency Department ---")
        print("1. Add patient")
        print("2. Remove patient from waiting list")
        print("3. View waiting list")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            condition = input("Is the patient's condition severe or not (yes/no)? ").lower()
            if condition == "yes":
                emergency_addition()
            elif condition == "no":
                add_to_waiting()
            else:
                print("Invalid input")
        elif choice == "2":
            remove_from_waiting()
        elif choice == "3":
            view_waiting_list()
        elif choice == "4":
            break
        else:
            print("Invalid input")

# ================== Main Menu ==================

def main_menu():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Nurses")
        print("4. Manage Medicines")
        print("5. Manage Appointments & Billing")
        print("6. Emergency Department")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patients_menu()
        elif choice == "2":
            doctors_menu()
        elif choice == "3":
            nurses_menu()
        elif choice == "4":
            medicines_menu()
        elif choice == "5":
            appointments_menu()
        elif choice == "6":
            emergency_department()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
main_menu()
