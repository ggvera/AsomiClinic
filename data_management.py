from models import *

from queries import with_session


@with_session
def register_specialty(session, name, description=None):
    try:
        existing_specialty = session.query(Especialidad).filter_by(nombre=name).first()
        if existing_specialty:
            print(f"Ya existe una especialidad con el nombre '{name}'")
            return None

        new_specialty = Especialidad(
            nombre=name,
            descripcion=description
        )
        session.add(new_specialty)
        session.commit()
        print(f"Especialidad '{name}' registrada correctamente")
        return new_specialty
    except Exception as e:
        session.rollback()
        print(f"Error al registrar especialidad: {str(e)}")
        return None


@with_session
def list_specialties(session):
    specialties = session.query(Especialidad).order_by(Especialidad.nombre).all()

    if not specialties:
        print("No hay especialidades registradas en el sistema")
        return []

    print("\n=== ESPECIALIDADES MÉDICAS DISPONIBLES ===")
    header = f"{'ID':<5}{'Nombre':<20}{'Descripción':<50}"
    print("-" * 75)
    print(header)
    print("-" * 75)

    for spec in specialties:
        description = spec.descripcion if spec.descripcion else "N/A"
        short_description = description[:45] + "..." if len(description) > 45 else description
        print(f"{spec.id_especialidad:<5}{spec.nombre:<20}{short_description:<50}")

    return specialties


# Functions for doctor management
@with_session
def register_doctor_with_specialty_selection(session, id_number, code, first_name, last_name,
                                             phone=None, email=None,
                                             license_number=None, consultation_schedule=None):
    try:
        existing_doctor = session.query(Medico).filter_by(cedula=id_number).first()
        if existing_doctor:
            print(f"Ya existe un médico con cédula {id_number}")
            return None

        existing_doctor = session.query(Medico).filter_by(codigo=code).first()
        if existing_doctor:
            print(f"Ya existe un médico con código {code}")
            return None

        specialties = list_specialties()

        if not specialties:
            print("Debe registrar especialidades antes de registrar médicos")
            return None

        while True:
            try:
                specialty_id = int(input("\nSeleccione el ID de la especialidad: "))

                specialty = session.query(Especialidad).filter_by(id_especialidad=specialty_id).first()
                if specialty:
                    break
                else:
                    print(f"No existe una especialidad con ID {specialty_id}")
            except ValueError:
                print("Por favor, ingrese un número válido")

        # Create the doctor
        new_doctor = Medico(
            cedula=id_number,
            codigo=code,
            nombre=first_name,
            apellidos=last_name,
            id_especialidad=specialty_id,
            telefono=phone,
            email=email,
            numero_licencia=license_number,
            horario_consulta=consultation_schedule
        )
        session.add(new_doctor)
        session.commit()

        print("\n=== MÉDICO REGISTRADO CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<50}"
        print("-" * 65)
        print(header)
        print("-" * 65)
        print(f"{'Nombre':<15}{first_name + ' ' + last_name:<50}")
        print(f"{'Cédula':<15}{id_number:<50}")
        print(f"{'Código':<15}{code:<50}")
        print(f"{'Especialidad':<15}{specialty.nombre:<50}")
        return new_doctor
    except Exception as e:
        session.rollback()
        print(f"Error al registrar médico: {str(e)}")
        return None


# Functions for patient management
@with_session
def register_new_patient(session, id_number, first_name, last_name, birth_date, gender,
                         address=None, phone=None, email=None, blood_type=None, allergies=None):
    try:
        existing_patient = session.query(Paciente).filter_by(cedula=id_number).first()
        if existing_patient:
            print(f"Ya existe un paciente con cédula {id_number}")
            return None

        new_patient = Paciente(
            cedula=id_number,
            nombre=first_name,
            apellidos=last_name,
            fecha_nacimiento=birth_date,
            genero=gender,
            direccion=address,
            telefono=phone,
            email=email,
            tipo_sangre=blood_type,
            alergias=allergies
        )
        session.add(new_patient)
        session.commit()

        print("\n=== PACIENTE REGISTRADO CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<50}"
        print("-" * 65)
        print(header)
        print("-" * 65)
        print(f"{'Nombre':<15}{first_name + ' ' + last_name:<50}")
        print(f"{'Cédula':<15}{id_number:<50}")
        print(f"{'Fecha Nac.':<15}{birth_date:<50}")
        print(f"{'Género':<15}{gender:<50}")
        if address:
            print(f"{'Dirección':<15}{address:<50}")
        if phone:
            print(f"{'Teléfono':<15}{phone:<50}")
        return new_patient
    except Exception as e:
        session.rollback()
        print(f"Error al registrar paciente: {str(e)}")
        return None


# Functions for room management
@with_session
def register_room(session, room_number, bed_count, room_type):
    try:
        existing_room = session.query(Habitacion).filter_by(numero_habitacion=room_number).first()
        if existing_room:
            print(f"Ya existe una habitación con número {room_number}")
            return None

        new_room = Habitacion(
            numero_habitacion=room_number,
            numero_cama=bed_count,
            tipo_habitacion=room_type,
            disponible=True
        )
        session.add(new_room)
        session.commit()

        print("\n=== HABITACIÓN REGISTRADA CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<20}"
        print("-" * 35)
        print(header)
        print("-" * 35)
        print(f"{'Número':<15}{room_number:<20}")
        print(f"{'Camas':<15}{bed_count:<20}")
        print(f"{'Tipo':<15}{room_type:<20}")
        print(f"{'Disponible':<15}{'Sí':<20}")
        return new_room
    except Exception as e:
        session.rollback()
        print(f"Error al registrar habitación: {str(e)}")
        return None


@with_session
def list_available_rooms(session):
    rooms = session.query(Habitacion).filter_by(disponible=True).order_by(Habitacion.numero_habitacion).all()

    if not rooms:
        print("No hay habitaciones disponibles en el sistema")
        return []

    print("\n=== HABITACIONES DISPONIBLES ===")
    header = f"{'ID':<5}{'Número':<10}{'Camas':<10}{'Tipo':<20}"
    print("-" * 45)
    print(header)
    print("-" * 45)

    for room in rooms:
        print(f"{room.id_habitacion:<5}{room.numero_habitacion:<10}{room.numero_cama:<10}{room.tipo_habitacion:<20}")

    return rooms


@with_session
def register_patient_admission(session, patient_id_number, doctor_code, room_number, diagnosis):
    try:
        patient = session.query(Paciente).filter_by(cedula=patient_id_number).first()
        if not patient:
            print(f"No existe un paciente con cédula {patient_id_number}")
            return None

        doctor = session.query(Medico).filter_by(codigo=doctor_code).first()
        if not doctor:
            print(f"No existe un médico con código {doctor_code}")
            return None

        room = session.query(Habitacion).filter_by(
            numero_habitacion=room_number,
            disponible=True
        ).first()

        if not room:
            print(f"No hay habitación disponible con número {room_number}")
            return None

        new_admission = Ingreso(
            id_paciente=patient.id_paciente,
            id_medico=doctor.id_medico,
            id_habitacion=room.id_habitacion,
            diagnostico=diagnosis,
            activo=True
        )

        # Update room status
        room.disponible = False

        session.add(new_admission)
        session.commit()

        print("\n=== INGRESO REGISTRADO CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<50}"
        print("-" * 65)
        print(header)
        print("-" * 65)
        print(f"{'Paciente':<15}{patient.nombre + ' ' + patient.apellidos:<50}")
        print(f"{'Médico':<15}{doctor.nombre + ' ' + doctor.apellidos:<50}")
        print(f"{'Habitación':<15}{room.numero_habitacion:<50}")
        print(f"{'Diagnóstico':<15}{diagnosis:<50}")
        print(f"{'Fecha Ingreso':<15}{new_admission.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S'):<50}")

        return new_admission
    except Exception as e:
        session.rollback()
        print(f"Error al registrar ingreso: {str(e)}")
        return None


@with_session
def register_patient_discharge(session, admission_id):
    try:
        admission = session.query(Ingreso).filter_by(id_ingreso=admission_id, activo=True).first()
        if not admission:
            print(f"No existe un ingreso activo con ID {admission_id}")
            return None

        admission.fecha_salida = datetime.now()
        admission.activo = False

        room = session.query(Habitacion).filter_by(id_habitacion=admission.id_habitacion).first()
        if room:
            room.disponible = True

        session.commit()

        patient = session.query(Paciente).filter_by(id_paciente=admission.id_paciente).first()
        duration_days = (admission.fecha_salida - admission.fecha_ingreso).days

        print("\n=== SALIDA REGISTRADA CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<50}"
        print(header)
        print("=" * 65)
        print(f"{'Paciente':<15}{patient.nombre + ' ' + patient.apellidos:<50}")
        print(f"{'Fecha Ingreso':<15}{admission.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S'):<50}")
        print(f"{'Fecha Salida':<15}{admission.fecha_salida.strftime('%Y-%m-%d %H:%M:%S'):<50}")
        print(f"{'Duración':<15}{duration_days} días")

        return admission
    except Exception as e:
        session.rollback()
        print(f"Error al registrar salida: {str(e)}")
        return None


@with_session
def register_patient_and_admission(session, id_number, first_name, last_name, birth_date, gender,
                                   doctor_code, room_number, diagnosis,
                                   address=None, phone=None, email=None, blood_type=None,
                                   allergies=None):
    try:
        existing_patient = session.query(Paciente).filter_by(cedula=id_number).first()
        if existing_patient:
            print(f"Ya existe un paciente con cédula {id_number}")
            return None

        new_patient = Paciente(
            cedula=id_number,
            nombre=first_name,
            apellidos=last_name,
            fecha_nacimiento=birth_date,
            genero=gender,
            direccion=address,
            telefono=phone,
            email=email,
            tipo_sangre=blood_type,
            alergias=allergies
        )
        session.add(new_patient)
        session.flush()

        doctor = session.query(Medico).filter_by(codigo=doctor_code).first()
        if not doctor:
            session.rollback()
            print(f"No existe un médico con código {doctor_code}")
            return None

        room = session.query(Habitacion).filter_by(
            numero_habitacion=room_number,
            disponible=True
        ).first()

        if not room:
            session.rollback()
            print(f"No hay habitación disponible con número {room_number}")
            return None

        new_admission = Ingreso(
            id_paciente=new_patient.id_paciente,
            id_medico=doctor.id_medico,
            id_habitacion=room.id_habitacion,
            diagnostico=diagnosis,
            activo=True
        )

        room.disponible = False

        session.add(new_admission)
        session.commit()

        print("\n=== PACIENTE E INGRESO REGISTRADOS CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<50}"
        print("-" * 65)
        print(header)
        print("-" * 65)
        print(f"{'Paciente':<15}{new_patient.nombre + ' ' + new_patient.apellidos:<50}")
        print(f"{'Cédula':<15}{id_number:<50}")
        print(f"{'Médico':<15}{doctor.nombre + ' ' + doctor.apellidos:<50}")
        print(f"{'Habitación':<15}{room.numero_habitacion:<50}")
        print(f"{'Diagnóstico':<15}{diagnosis:<50}")
        print(f"{'Fecha Ingreso':<15}{new_admission.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S'):<50}")

        return (new_patient, new_admission)
    except Exception as e:
        session.rollback()
        print(f"Error al registrar paciente e ingreso: {str(e)}")
        return None


@with_session
def assign_new_doctor_to_admission(session, admission_id, new_doctor_code):
    try:
        admission = session.query(Ingreso).filter_by(id_ingreso=admission_id, activo=True).first()
        if not admission:
            print(f"No existe un ingreso activo con ID {admission_id}")
            return None

        new_doctor = session.query(Medico).filter_by(codigo=new_doctor_code).first()
        if not new_doctor:
            print(f"No existe un médico con código {new_doctor_code}")
            return None

        previous_doctor = session.query(Medico).filter_by(id_medico=admission.id_medico).first()

        admission.id_medico = new_doctor.id_medico

        session.commit()

        print("\n=== MÉDICO CAMBIADO CORRECTAMENTE ===")
        header = f"{'Campo':<15}{'Valor':<50}"
        print("-" * 65)
        print(header)
        print("-" * 65)
        print(f"{'Ingreso ID':<15}{admission_id:<50}")
        print(f"{'Médico Ant.':<15}{previous_doctor.nombre + ' ' + previous_doctor.apellidos:<50}")
        print(f"{'Nuevo Médico':<15}{new_doctor.nombre + ' ' + new_doctor.apellidos:<50}")

        return admission
    except Exception as e:
        session.rollback()
        print(f"Error al cambiar médico: {str(e)}")
        return None