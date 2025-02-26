from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Paciente(Base):
    __tablename__ = 'pacientes'

    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    cedula = Column(String(10), unique=True)
    nombre = Column(String(50))
    apellidos = Column(String(50))
    fecha_nacimiento = Column(Date)
    genero = Column(String(1))
    direccion = Column(String(100))
    telefono = Column(String(15))
    email = Column(String(50))
    tipo_sangre = Column(String(5))
    alergias = Column(Text)

    # Relación con ingresos
    ingresos = relationship("Ingreso", back_populates="paciente")



class Especialidad(Base):
    __tablename__ = 'especialidades'

    id_especialidad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(Text)

    # Relación con médicos
    medicos = relationship("Medico", back_populates="especialidad")



class Medico(Base):
    __tablename__ = 'medicos'

    id_medico = Column(Integer, primary_key=True, autoincrement=True)
    cedula = Column(String(10), unique=True)
    codigo = Column(String(10), unique=True)
    nombre = Column(String(50))
    apellidos = Column(String(50))
    telefono = Column(String(15))
    email = Column(String(50))
    id_especialidad = Column(Integer, ForeignKey('especialidades.id_especialidad'))
    numero_licencia = Column(String(20))
    horario_consulta = Column(String(50))

    # Relaciones
    especialidad = relationship("Especialidad", back_populates="medicos")
    ingresos = relationship("Ingreso", back_populates="medico")



class Habitacion(Base):
    __tablename__ = 'habitaciones'

    id_habitacion = Column(Integer, primary_key=True, autoincrement=True)
    numero_habitacion = Column(String(10))
    numero_cama = Column(Integer)
    tipo_habitacion = Column(String(20))
    disponible = Column(Boolean, default=True)

    # Relación con ingresos
    ingresos = relationship("Ingreso", back_populates="habitacion")



class Ingreso(Base):
    __tablename__ = 'ingresos'

    id_ingreso = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey('pacientes.id_paciente'))
    id_medico = Column(Integer, ForeignKey('medicos.id_medico'))
    id_habitacion = Column(Integer, ForeignKey('habitaciones.id_habitacion'))
    fecha_ingreso = Column(DateTime, default=datetime.now)
    fecha_salida = Column(DateTime, nullable=True)
    diagnostico = Column(Text)
    activo = Column(Boolean, default=True)

    # Relaciones
    paciente = relationship("Paciente", back_populates="ingresos")
    medico = relationship("Medico", back_populates="ingresos")
    habitacion = relationship("Habitacion", back_populates="ingresos")
