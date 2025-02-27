from database import SessionLocal, engine
from models import Paciente, Especialidad, Medico, Habitacion, Ingreso, Base
from datetime import datetime, date


def seed_database():
    db = SessionLocal()

    try:
        # Insertar Pacientes
        pacientes = [
            Paciente(cedula='1703456789', nombre='Juan', apellidos='Pérez Sánchez', fecha_nacimiento=date(1985, 5, 12),
                     genero='M', direccion='Av. 10 de Agosto N34-56, Quito', telefono='0991234567',
                     email='juan.perez@email.com', tipo_sangre='O+', alergias='Penicilina'),
            Paciente(cedula='1704567890', nombre='María', apellidos='González López',
                     fecha_nacimiento=date(1990, 7, 22),
                     genero='F', direccion='Calle Toledo 123, Guayaquil', telefono='0987654321',
                     email='maria.gonzalez@email.com', tipo_sangre='A+', alergias='Ninguna'),
            Paciente(cedula='1705678901', nombre='Carlos', apellidos='Rodríguez Vega',
                     fecha_nacimiento=date(1978, 3, 15),
                     genero='M', direccion='Av. Amazonas E5-12, Quito', telefono='0998765432',
                     email='carlos.rodriguez@email.com', tipo_sangre='B-', alergias='Aspirina, Látex'),
            Paciente(cedula='1706789012', nombre='Ana', apellidos='Martínez Rivas', fecha_nacimiento=date(1995, 11, 30),
                     genero='F', direccion='Calle Rocafuerte 567, Cuenca', telefono='0992345678',
                     email='ana.martinez@email.com', tipo_sangre='AB+', alergias='Sulfamidas'),
            Paciente(cedula='1707890123', nombre='Luis', apellidos='Sánchez Mera', fecha_nacimiento=date(1982, 8, 5),
                     genero='M', direccion='Av. 9 de Octubre 432, Guayaquil', telefono='0986543210',
                     email='luis.sanchez@email.com', tipo_sangre='O-', alergias='Ninguna'),
            Paciente(cedula='1708901234', nombre='Elena', apellidos='Flores Torres', fecha_nacimiento=date(1988, 1, 17),
                     genero='F', direccion='Calle Venezuela 789, Quito', telefono='0993456789',
                     email='elena.flores@email.com', tipo_sangre='A-', alergias='Mariscos'),
            Paciente(cedula='1709012345', nombre='Pedro', apellidos='López Guerra', fecha_nacimiento=date(1975, 9, 25),
                     genero='M', direccion='Av. Patria E4-56, Quito', telefono='0984567890',
                     email='pedro.lopez@email.com', tipo_sangre='B+', alergias='Polen'),
            Paciente(cedula='1700123456', nombre='Laura', apellidos='Torres Mora', fecha_nacimiento=date(1992, 4, 8),
                     genero='F', direccion='Calle Larga 234, Cuenca', telefono='0995678901',
                     email='laura.torres@email.com', tipo_sangre='AB-', alergias='Ninguna'),
            Paciente(cedula='1701234567', nombre='Diego', apellidos='Castro Vela', fecha_nacimiento=date(1980, 12, 3),
                     genero='M', direccion='Av. Kennedy 123, Guayaquil', telefono='0983456789',
                     email='diego.castro@email.com', tipo_sangre='O+', alergias='Penicilina, Ibuprofeno'),
            Paciente(cedula='1702345678', nombre='Sofía', apellidos='Vega Luna', fecha_nacimiento=date(1993, 6, 20),
                     genero='F', direccion='Calle Reina Victoria N27-45, Quito', telefono='0997890123',
                     email='sofia.vega@email.com', tipo_sangre='A+', alergias='Nueces')
        ]
        db.add_all(pacientes)
        db.commit()

        # Insertar Especialidades
        especialidades = [
            Especialidad(nombre='Cardiología',
                         descripcion='Especialidad médica que se ocupa del estudio, diagnóstico y tratamiento de las enfermedades del corazón y del sistema circulatorio.'),
            Especialidad(nombre='Dermatología',
                         descripcion='Especialidad médica encargada del estudio de la estructura y función de la piel, así como de las enfermedades que la afectan.'),
            Especialidad(nombre='Pediatría',
                         descripcion='Especialidad médica que estudia al niño y sus enfermedades. Se ocupa del desarrollo del niño, su crecimiento y la pubertad.'),
            Especialidad(nombre='Traumatología',
                         descripcion='Especialidad médica dedicada al estudio de las lesiones del aparato locomotor.'),
            Especialidad(nombre='Neurología',
                         descripcion='Especialidad médica que trata los trastornos del sistema nervioso.'),
            Especialidad(nombre='Gastroenterología',
                         descripcion='Especialidad médica que se ocupa de las enfermedades del aparato digestivo.'),
            Especialidad(nombre='Oftalmología',
                         descripcion='Especialidad médica que estudia las enfermedades del ojo y sus tratamientos.'),
            Especialidad(nombre='Ginecología',
                         descripcion='Especialidad médica y quirúrgica que trata las enfermedades del sistema reproductor femenino.'),
            Especialidad(nombre='Urología',
                         descripcion='Especialidad médico-quirúrgica que se ocupa del estudio, diagnóstico y tratamiento de las patologías que afectan al aparato urinario.'),
            Especialidad(nombre='Oncología',
                         descripcion='Especialidad médica que estudia y trata las neoplasias, tumores benignos y malignos.')
        ]
        db.add_all(especialidades)
        db.commit()

        # Insertar Médicos
        medicos = [
            Medico(cedula='1710000001', codigo='MED001', nombre='Roberto', apellidos='Jiménez Vargas',
                   telefono='0991122334', email='roberto.jimenez@clinica.com', id_especialidad=1,
                   numero_licencia='LIC12345', horario_consulta='Lunes y Miércoles 8:00-14:00'),
            Medico(cedula='1710000002', codigo='MED002', nombre='Carmen', apellidos='Alvarado Ruiz',
                   telefono='0992233445', email='carmen.alvarado@clinica.com', id_especialidad=2,
                   numero_licencia='LIC23456', horario_consulta='Martes y Jueves 9:00-15:00'),
            Medico(cedula='1710000003', codigo='MED003', nombre='Fernando', apellidos='Morales Paz',
                   telefono='0993344556', email='fernando.morales@clinica.com', id_especialidad=3,
                   numero_licencia='LIC34567', horario_consulta='Lunes a Viernes 8:00-12:00'),
            Medico(cedula='1710000004', codigo='MED004', nombre='Adriana', apellidos='Campos Vera',
                   telefono='0994455667', email='adriana.campos@clinica.com', id_especialidad=4,
                   numero_licencia='LIC45678', horario_consulta='Miércoles y Viernes 14:00-20:00'),
            Medico(cedula='1710000005', codigo='MED005', nombre='Gabriel', apellidos='Herrera Luna',
                   telefono='0995566778', email='gabriel.herrera@clinica.com', id_especialidad=5,
                   numero_licencia='LIC56789', horario_consulta='Lunes, Miércoles y Viernes 10:00-16:00'),
            Medico(cedula='1710000006', codigo='MED006', nombre='Martha', apellidos='Ortiz Conde',
                   telefono='0996677889', email='martha.ortiz@clinica.com', id_especialidad=6,
                   numero_licencia='LIC67890', horario_consulta='Martes y Jueves 8:00-17:00'),
            Medico(cedula='1710000007', codigo='MED007', nombre='Andrés', apellidos='Mendoza Silva',
                   telefono='0997788990', email='andres.mendoza@clinica.com', id_especialidad=7,
                   numero_licencia='LIC78901', horario_consulta='Lunes a Viernes 8:00-12:00'),
            Medico(cedula='1710000008', codigo='MED008', nombre='Patricia', apellidos='Delgado Reyes',
                   telefono='0998899001', email='patricia.delgado@clinica.com', id_especialidad=8,
                   numero_licencia='LIC89012', horario_consulta='Martes y Jueves 14:00-20:00'),
            Medico(cedula='1710000009', codigo='MED009', nombre='Hector', apellidos='Vargas Cruz',
                   telefono='0999900112', email='hector.vargas@clinica.com', id_especialidad=9,
                   numero_licencia='LIC90123', horario_consulta='Lunes, Miércoles y Viernes 9:00-15:00'),
            Medico(cedula='1710000010', codigo='MED010', nombre='Valeria', apellidos='Romero Vidal',
                   telefono='0990011223', email='valeria.romero@clinica.com', id_especialidad=10,
                   numero_licencia='LIC01234', horario_consulta='Lunes a Viernes 14:00-18:00'),
            Medico(cedula='1710000011', codigo='MED011', nombre='Javier', apellidos='Núñez Bravo',
                   telefono='0991122334', email='javier.nunez@clinica.com', id_especialidad=1,
                   numero_licencia='LIC11111', horario_consulta='Martes y Jueves 8:00-14:00'),
            Medico(cedula='1710000012', codigo='MED012', nombre='Diana', apellidos='Paredes Mena',
                   telefono='0992233445', email='diana.paredes@clinica.com', id_especialidad=3,
                   numero_licencia='LIC22222', horario_consulta='Lunes, Miércoles y Viernes 14:00-20:00')
        ]
        db.add_all(medicos)
        db.commit()

        # Insertar Habitaciones
        habitaciones = [
            Habitacion(numero_habitacion='101', numero_cama=1, tipo_habitacion='Individual', disponible=True),
            Habitacion(numero_habitacion='102', numero_cama=1, tipo_habitacion='Individual', disponible=False),
            Habitacion(numero_habitacion='103', numero_cama=1, tipo_habitacion='Individual', disponible=True),
            Habitacion(numero_habitacion='104', numero_cama=1, tipo_habitacion='Individual', disponible=False),
            Habitacion(numero_habitacion='105', numero_cama=1, tipo_habitacion='Individual', disponible=True),
            Habitacion(numero_habitacion='201', numero_cama=1, tipo_habitacion='Doble', disponible=True),
            Habitacion(numero_habitacion='201', numero_cama=2, tipo_habitacion='Doble', disponible=False),
            Habitacion(numero_habitacion='202', numero_cama=1, tipo_habitacion='Doble', disponible=True),
            Habitacion(numero_habitacion='202', numero_cama=2, tipo_habitacion='Doble', disponible=True),
            Habitacion(numero_habitacion='203', numero_cama=1, tipo_habitacion='Doble', disponible=False),
            Habitacion(numero_habitacion='203', numero_cama=2, tipo_habitacion='Doble', disponible=False),
            Habitacion(numero_habitacion='301', numero_cama=1, tipo_habitacion='Suite', disponible=True),
            Habitacion(numero_habitacion='302', numero_cama=1, tipo_habitacion='Suite', disponible=False),
            Habitacion(numero_habitacion='303', numero_cama=1, tipo_habitacion='Suite', disponible=True),
            Habitacion(numero_habitacion='401', numero_cama=1, tipo_habitacion='UCI', disponible=False),
            Habitacion(numero_habitacion='402', numero_cama=1, tipo_habitacion='UCI', disponible=False),
            Habitacion(numero_habitacion='403', numero_cama=1, tipo_habitacion='UCI', disponible=True),
            Habitacion(numero_habitacion='404', numero_cama=1, tipo_habitacion='UCI', disponible=True),
            Habitacion(numero_habitacion='501', numero_cama=1, tipo_habitacion='Pediatría', disponible=True),
            Habitacion(numero_habitacion='502', numero_cama=1, tipo_habitacion='Pediatría', disponible=False)
        ]
        db.add_all(habitaciones)
        db.commit()

        # Insertar Ingresos
        ingresos = [
            Ingreso(id_paciente=1, id_medico=1, id_habitacion=2, fecha_ingreso=datetime(2024, 1, 15, 8, 30, 0),
                    fecha_salida=datetime(2024, 1, 20, 11, 15, 0), diagnostico='Hipertensión arterial descontrolada',
                    activo=False),
            Ingreso(id_paciente=2, id_medico=8, id_habitacion=7, fecha_ingreso=datetime(2024, 1, 18, 14, 45, 0),
                    fecha_salida=datetime(2024, 1, 25, 10, 0, 0), diagnostico='Embarazo de alto riesgo', activo=False),
            Ingreso(id_paciente=3, id_medico=9, id_habitacion=10, fecha_ingreso=datetime(2024, 1, 22, 9, 15, 0),
                    fecha_salida=datetime(2024, 1, 24, 16, 30, 0), diagnostico='Infección urinaria', activo=False),
            Ingreso(id_paciente=4, id_medico=2, id_habitacion=11, fecha_ingreso=datetime(2024, 1, 28, 18, 20, 0),
                    fecha_salida=datetime(2024, 2, 5, 12, 45, 0), diagnostico='Dermatitis severa', activo=False),
            Ingreso(id_paciente=5, id_medico=6, id_habitacion=15, fecha_ingreso=datetime(2024, 2, 1, 7, 50, 0),
                    fecha_salida=datetime(2024, 2, 10, 9, 30, 0), diagnostico='Hemorragia digestiva', activo=False),
            Ingreso(id_paciente=6, id_medico=5, id_habitacion=16, fecha_ingreso=datetime(2024, 2, 5, 22, 10, 0),
                    fecha_salida=datetime(2024, 2, 15, 14, 20, 0), diagnostico='Accidente cerebrovascular',
                    activo=False),
            Ingreso(id_paciente=7, id_medico=4, id_habitacion=13, fecha_ingreso=datetime(2024, 2, 10, 11, 30, 0),
                    fecha_salida=datetime(2024, 2, 12, 13, 45, 0), diagnostico='Fractura de tibia', activo=False),
            Ingreso(id_paciente=1, id_medico=1, id_habitacion=20, fecha_ingreso=datetime(2024, 2, 15, 16, 40, 0),
                    fecha_salida=None, diagnostico='Control de hipertensión', activo=True),
            Ingreso(id_paciente=8, id_medico=7, id_habitacion=10, fecha_ingreso=datetime(2024, 2, 18, 8, 15, 0),
                    fecha_salida=datetime(2024, 2, 20, 10, 30, 0), diagnostico='Glaucoma', activo=False),
            Ingreso(id_paciente=9, id_medico=9, id_habitacion=11, fecha_ingreso=datetime(2024, 2, 20, 14, 25, 0),
                    fecha_salida=datetime(2024, 2, 25, 9, 10, 0), diagnostico='Cálculos renales', activo=False),
            Ingreso(id_paciente=10, id_medico=8, id_habitacion=2, fecha_ingreso=datetime(2024, 2, 22, 15, 50, 0),
                    fecha_salida=None, diagnostico='Control ginecológico', activo=True),
            Ingreso(id_paciente=3, id_medico=10, id_habitacion=16, fecha_ingreso=datetime(2024, 2, 25, 19, 5, 0),
                    fecha_salida=None, diagnostico='Sospecha de tumor hepático', activo=True),
            Ingreso(id_paciente=2, id_medico=3, id_habitacion=20, fecha_ingreso=datetime(2024, 2, 26, 10, 30, 0),
                    fecha_salida=None, diagnostico='Fiebre alta en menor', activo=True),
            Ingreso(id_paciente=5, id_medico=6, id_habitacion=7, fecha_ingreso=datetime(2024, 2, 27, 8, 45, 0),
                    fecha_salida=None, diagnostico='Úlcera gástrica', activo=True),
            Ingreso(id_paciente=1, id_medico=11, id_habitacion=2, fecha_ingreso=datetime(2024, 1, 5, 9, 20, 0),
                    fecha_salida=datetime(2024, 1, 8, 14, 30, 0), diagnostico='Arritmia cardíaca', activo=False),
            Ingreso(id_paciente=4, id_medico=2, id_habitacion=7, fecha_ingreso=datetime(2024, 1, 10, 11, 15, 0),
                    fecha_salida=datetime(2024, 1, 12, 16, 45, 0), diagnostico='Reacción alérgica severa',
                    activo=False),
            Ingreso(id_paciente=7, id_medico=4, id_habitacion=11, fecha_ingreso=datetime(2024, 1, 25, 15, 40, 0),
                    fecha_salida=datetime(2024, 1, 28, 10, 20, 0), diagnostico='Esguince de tobillo', activo=False),
            Ingreso(id_paciente=3, id_medico=12, id_habitacion=13, fecha_ingreso=datetime(2024, 2, 8, 12, 30, 0),
                    fecha_salida=datetime(2024, 2, 11, 9, 15, 0), diagnostico='Neumonía infantil', activo=False),
            Ingreso(id_paciente=8, id_medico=7, id_habitacion=2, fecha_ingreso=datetime(2024, 2, 14, 16, 50, 0),
                    fecha_salida=datetime(2024, 2, 16, 11, 30, 0), diagnostico='Conjuntivitis severa', activo=False),
            Ingreso(id_paciente=2, id_medico=8, id_habitacion=10, fecha_ingreso=datetime(2024, 1, 8, 10, 25, 0),
                    fecha_salida=datetime(2024, 1, 10, 15, 40, 0), diagnostico='Control de rutina prenatal',
                    activo=False)
        ]
        db.add_all(ingresos)
        db.commit()

        print("La base de datos fue poblada exitosamente!")

    except Exception as e:
        print(f"Error al poblar la base de datos: {e}")
        db.rollback()

    finally:
        db.close()

