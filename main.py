from data_management import *
from queries import *
from database import create_database
from queries import (get_list_doctor, get_list_registered_patients, get_list_care_provided_doctor,
                     get_list_all_patient_income, get_three_specialties_with_most_requests,
                     get_doctor_with_the_highest_income)
from seed import seed_database


def specialty_administration_menu():
    while True:
        print("\n==== ADMINISTRACIÓN DE ESPECIALIDADES ====")
        print("1. Registrar nueva especialidad")
        print("2. Listar especialidades")
        print("3. Volver al menú principal")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            name = input("Nombre de la especialidad: ")
            description = input("Descripción (opcional): ")
            register_specialty(name=name, description=description)

        elif option == "2":
            list_specialties()

        elif option == "3":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def doctor_administration_menu():
    while True:
        print("\n==== ADMINISTRACIÓN DE MÉDICOS ====")
        print("1. Registrar nuevo médico")
        print("2. Listar médicos")
        print("3. Volver al menú principal")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            id_number = input("Cédula del médico: ")
            code = input("Código del médico: ")
            first_name = input("Nombre: ")
            last_name = input("Apellidos: ")
            phone = input("Teléfono (opcional): ")
            email = input("Email (opcional): ")
            license_number = input("Número de licencia (opcional): ")
            consultation_schedule = input("Horario de consulta (opcional): ")

            register_doctor_with_specialty_selection(
                id_number=id_number,
                code=code,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                license_number=license_number,
                consultation_schedule=consultation_schedule
            )

        elif option == "2":
            get_list_doctor()

        elif option == "3":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def patient_administration_menu():
    while True:
        print("\n==== ADMINISTRACIÓN DE PACIENTES ====")
        print("1. Registrar nuevo paciente")
        print("2. Listar pacientes registrados")
        print("3. Ver ingresos por paciente")
        print("4. Volver al menú principal")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            id_number = input("Cédula del paciente: ")
            first_name = input("Nombre: ")
            last_name = input("Apellidos: ")

            # Validate and convert date
            while True:
                date_str = input("Fecha de nacimiento (AAAA-MM-DD): ")
                try:
                    birth_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Formato de fecha incorrecto. Use el formato AAAA-MM-DD.")

            gender = input("Género (M/F): ").upper()
            while gender not in ['M', 'F']:
                print("Género inválido. Debe ser M o F.")
                gender = input("Género (M/F): ").upper()

            address = input("Dirección (opcional): ")
            phone = input("Teléfono (opcional): ")
            email = input("Email (opcional): ")
            blood_type = input("Tipo de sangre (opcional): ")
            allergies = input("Alergias (opcional): ")

            register_new_patient(
                id_number=id_number,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                gender=gender,
                address=address,
                phone=phone,
                email=email,
                blood_type=blood_type,
                allergies=allergies
            )

        elif option == "2":
            get_list_registered_patients()

        elif option == "3":
            get_list_all_patient_income()

        elif option == "4":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def room_administration_menu():
    while True:
        print("\n==== ADMINISTRACIÓN DE HABITACIONES ====")
        print("1. Registrar nueva habitación")
        print("2. Listar habitaciones disponibles")
        print("3. Volver al menú principal")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            room_number = input("Número de habitación: ")

            while True:
                try:
                    bed_count = int(input("Número de camas: "))
                    break
                except ValueError:
                    print("Ingrese un número válido.")

            room_type = input("Tipo de habitación (Individual/Doble/Suite): ")

            register_room(
                room_number=room_number,
                bed_count=bed_count,
                room_type=room_type
            )

        elif option == "2":
            list_available_rooms()

        elif option == "3":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def admission_administration_menu():
    while True:
        print("\n==== ADMINISTRACIÓN DE INGRESOS ====")
        print("1. Registrar nuevo ingreso")
        print("2. Registrar salida de paciente")
        print("3. Registrar nuevo paciente e ingreso")
        print("4. Cambiar médico asignado")
        print("5. Volver al menú principal")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            patient_id_number = input("Cédula del paciente: ")
            doctor_code = input("Código del médico: ")

            # List available rooms
            rooms = list_available_rooms()
            if not rooms:
                print("No hay habitaciones disponibles para asignar.")
                continue

            room_number = input("Número de habitación: ")
            diagnosis = input("Diagnóstico: ")

            register_patient_admission(
                patient_id_number=patient_id_number,
                doctor_code=doctor_code,
                room_number=room_number,
                diagnosis=diagnosis
            )

        elif option == "2":
            while True:
                try:
                    admission_id = int(input("ID del ingreso: "))
                    break
                except ValueError:
                    print("Ingrese un número válido.")

            register_patient_discharge(admission_id=admission_id)

        elif option == "3":
            # Collect patient data
            id_number = input("Cédula del paciente: ")
            first_name = input("Nombre: ")
            last_name = input("Apellidos: ")

            # Validate and convert date
            while True:
                date_str = input("Fecha de nacimiento (AAAA-MM-DD): ")
                try:
                    birth_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Formato de fecha incorrecto. Use el formato AAAA-MM-DD.")

            gender = input("Género (M/F): ").upper()
            while gender not in ['M', 'F']:
                print("énero inválido. Debe ser M o F.")
                gender = input("Género (M/F): ").upper()

            address = input("Dirección (opcional): ")
            phone = input("Teléfono (opcional): ")
            email = input("Email (opcional): ")
            blood_type = input("Tipo de sangre (opcional): ")
            allergies = input("Alergias (opcional): ")

            # Collect admission data
            doctor_code = input("Código del médico: ")

            # List available rooms
            rooms = list_available_rooms()
            if not rooms:
                print("No hay habitaciones disponibles para asignar.")
                continue

            room_number = input("Número de habitación: ")
            diagnosis = input("Diagnóstico: ")

            register_patient_and_admission(
                id_number=id_number,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                gender=gender,
                doctor_code=doctor_code,
                room_number=room_number,
                diagnosis=diagnosis,
                address=address,
                phone=phone,
                email=email,
                blood_type=blood_type,
                allergies=allergies
            )

        elif option == "4":
            while True:
                try:
                    admission_id = int(input("ID del ingreso: "))
                    break
                except ValueError:
                    print("Ingrese un número válido.")

            new_doctor_code = input("Código del nuevo médico: ")

            assign_new_doctor_to_admission(
                admission_id=admission_id,
                new_doctor_code=new_doctor_code
            )

        elif option == "5":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def main_menu():
    while True:
        print("\n===== ASOMI - SISTEMA DE GESTIÓN CLÍNICA =====")
        print("1. Administración de especialidades")
        print("2. Administración de médicos")
        print("3. Administración de pacientes")
        print("4. Administración de habitaciones")
        print("5. Administración de ingresos y salidas")
        print("6. Reportes del sistema")
        print("7. Insertar datos iniciales")
        print("8. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            specialty_administration_menu()

        elif option == "2":
            doctor_administration_menu()

        elif option == "3":
            patient_administration_menu()

        elif option == "4":
            room_administration_menu()

        elif option == "5":
            admission_administration_menu()

        elif option == "6":
            reports_menu()

        elif option == "7":
            seed_database()

        elif option == "8":
            print("¡Gracias por utilizar el sistema ASOMI!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def reports_menu():
    while True:
        print("\n==== REPORTES DEL SISTEMA ====")
        print("1. Listar médicos")
        print("2. Listar pacientes registrados")
        print("3. Número de atenciones realizadas por cada medico")
        print("4. Número de ingresos a la clínica por paciente")
        print("5. Listar las tres especialidades más solicitadas")
        print("6. Médico actual con mayor ingreso de pacientes")
        print("7. Volver al menú principal")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            get_list_doctor()

        elif option == "2":
            get_list_registered_patients()

        elif option == "3":
            get_list_care_provided_doctor()

        elif option == "4":
            get_list_all_patient_income()

        elif option == "5":
            get_three_specialties_with_most_requests()

        elif option == "6":
            get_doctor_with_the_highest_income()

        elif option == "7":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def main():
    create_database()
    main_menu()


if __name__ == "__main__":
    main()