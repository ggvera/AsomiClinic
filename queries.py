from sqlalchemy import func, desc
from database import SessionLocal
from models import *
from functools import wraps
from contextlib import contextmanager


@contextmanager
def session_scope():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with session_scope() as session:
            return func(session, *args, **kwargs)

    return wrapper


@with_session
def get_list_doctor(session):
    medicos = (
        session.query(
            Medico.cedula,
            Medico.codigo,
            Medico.nombre,
            Medico.apellidos,
            Especialidad.nombre.label('especialidad')
        )
        .join(Especialidad, Medico.id_especialidad == Especialidad.id_especialidad)
        .order_by(Medico.apellidos)
        .all()
    )

    print("\n=== LISTADO DE MÉDICOS ===")
    header = f"{'Cédula':<15}{'Código':<10}{'Nombre':<15}{'Apellidos':<20}{'Especialidad':<20}"
    print("-" * 80)
    print(header)
    print("-" * 80)

    for medico in medicos:
        print(
            f"{medico.cedula:<15}{medico.codigo:<10}{medico.nombre:<15}{medico.apellidos:<20}{medico.especialidad:<20}")


@with_session
def get_list_registered_patients(session):
    pacientes = (
        session.query(
            Paciente.cedula,
            Paciente.nombre,
            Paciente.apellidos
        )
        .join(Ingreso, Paciente.id_paciente == Ingreso.id_paciente)
        .order_by(Paciente.apellidos)
        .distinct()
        .all()
    )

    print("\n=== LISTADO DE PACIENTES REGISTRADOS ===")
    header = f"{'Cédula':<15}{'Nombre':<15}{'Apellidos':<20}"
    print("-" * 50)
    print(header)
    print("-" * 50)

    for paciente in pacientes:
        print(f"{paciente.cedula:<15}{paciente.nombre:<15}{paciente.apellidos:<20}")



@with_session
def get_list_care_provided_doctor(session):
    results = (
        session.query(
            Medico.nombre,
            Medico.apellidos,
            Medico.codigo,
            func.count(Ingreso.id_medico).label('Total_Atenciones')
        )
        .select_from(Medico)
        .outerjoin(Ingreso, Medico.id_medico == Ingreso.id_medico)
        .group_by(Medico.id_medico, Medico.nombre, Medico.apellidos, Medico.codigo)
        .order_by(desc(func.count(Ingreso.id_medico)))
        .all()
    )

    print("\n=== TOTAL DE ATENCIONES REALIZADAS POR CADA MEDICO ===")
    header = f"{'Nombre':<15}{'Apellidos':<20}{'Código':<10}{'Total Atenciones':<15}"
    print("-" * 60)
    print(header)
    print("-" * 60)

    for result in results:
        print(f"{result.nombre:<15}{result.apellidos:<20}{result.codigo:<10}{result.Total_Atenciones:<15}")


@with_session
def get_list_all_patient_income(session):
    results = (
        session.query(
            Paciente.cedula,
            Paciente.nombre,
            Paciente.apellidos,
            func.count(Ingreso.id_paciente).label('Total_ingresos')
        )
        .select_from(Paciente)
        .outerjoin(Ingreso, Paciente.id_paciente == Ingreso.id_paciente)
        .group_by(Paciente.id_paciente, Paciente.cedula, Paciente.nombre, Paciente.apellidos)
        .all()
    )

    print("\n=== TOTAL DE INGRESOS POR PACIENTE ===")
    header = f"{'Cédula':<15}{'Nombre':<15}{'Apellidos':<20}{'Ingresos':<10}"
    print("-" * 60)
    print(header)
    print("-" * 60)

    for result in results:
        print(f"{result.cedula:<15}{result.nombre:<15}{result.apellidos:<20}{result.Total_ingresos:<10}")

@with_session
def get_three_specialties_with_most_requests(session):
    results = (
        session.query(
            Especialidad.nombre.label('Especialidad_con_mayor_solicitud'),
            func.count(Ingreso.id_medico).label('Numero_de_solicitudes')
        )
        .join(Medico, Medico.id_especialidad == Especialidad.id_especialidad)
        .join(Ingreso, Medico.id_medico == Ingreso.id_medico)
        .group_by(Especialidad.id_especialidad, Especialidad.nombre)
        .order_by(desc(func.count(Ingreso.id_medico)))
        .limit(3)
        .all()
    )

    print("\n=== TRES ESPECIALIDADES MÁS SOLICITADAS ===")
    header = f"{'Especialidad':<30}{'Número de Solicitudes':<20}"
    print("-" * 60)
    print(header)
    print("-" * 60)

    for i, result in enumerate(results, 1):
        print(f"{i}. {result.Especialidad_con_mayor_solicitud:<28}{result.Numero_de_solicitudes:<20}")



@with_session
def get_doctor_with_the_highest_income(session):
    results = (
        session.query(
            Medico.nombre,
            Medico.apellidos,
            Medico.codigo,
            Especialidad.nombre.label('especialidad'),
            func.count(Ingreso.id_medico).label('Numero_de_ingresos')
        )
        .join(Ingreso, Medico.id_medico == Ingreso.id_medico)
        .join(Especialidad, Medico.id_especialidad == Especialidad.id_especialidad)
        .group_by(Medico.id_medico, Medico.nombre, Medico.apellidos, Medico.codigo, Especialidad.nombre)
        .order_by(desc(func.count(Ingreso.id_medico)))
        .limit(1)
        .first()
    )

    if results:
        print("\n=== DOCTOR CON MAYOR NÚMERO DE INGRESOS ===")
        header = f"{'Nombre':<15}{'Apellidos':<20}{'Código':<10}{'Especialidad':<20}{'Ingresos':<10}"
        print("-" * 75)
        print(header)
        print("-" * 75)
        print(
            f"{results.nombre:<15}{results.apellidos:<20}{results.codigo:<10}{results.especialidad:<20}{results.Numero_de_ingresos:<10}")
    else:
        print("\nNo hay ingresos registrados en el sistema.")