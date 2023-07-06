from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Fuentes(models.Model):
    programa_ID = models.IntegerField(primary_key=True)
    nombre_Programa = models.CharField(max_length=1000)
    class Areas(models.TextChoices):
        CYT = "CYT", _("Ciencia y tecnología")
        CUL = "CUL", _("Cultura")
        ECO = "ECO", _("Economía")
        EDU = "EDU", _("Educación")
        MAM = "MAM", _("Medio ambiente")
        MOV = "MOV", _("Movilidad")
        SAL = "SAL", _("Salud")
        SEG = "SEG", _("Seguridad pública")
        TUR = "TUR", _("Turismo")
        VIV = "VIV", _("Vivienda")
        OTR = "OTR", _("Otro")
    area_Tematica = models.CharField(
        max_length=3,
        choices=Areas.choices
    )
    nombre_Institucion = models.CharField(max_length=1000)
    descripcion_Fondo = models.CharField(max_length=1000)
    class Origen(models.TextChoices):
        INT = "INT", _("Internacional")
        GUB = "GUB", _("Gubernamental")
        PRI = "PRI", _("Privado")
        OTR = "OTR", _("Otro")
    origen = models.CharField(
        max_length=3,
        choices=Origen.choices
    )
    class Grupo_Atn(models.TextChoices):
        AYD = "AYD", _("Artistas y diseñadores")
        EST = "EST", _("Estudiantes")
        PED = "PED", _("Personal docente")
        INV = "INV", _("Investigadores, inventores y científicos")
        PG = "PG", _("Población general")
        PYC = "PYC", _("Productores y campesinos")
        PM = "PM", _("Personas mayores")
        MUJ = "MUJ", _("Mujeres")
        JOV = "JOV", _("Jóvenes")
        PCD = "PCD", _("Personas con discapacidad")
        POB = "POB", _("Personas en situación de pobreza")
        IND = "IND", _("Indígenas")
        DEP = "DEP", _("Deportistas")
        OTR = "OTR", _("Otro")
    grupo_De_Atencion = models.CharField(
        max_length=3,
        choices=Grupo_Atn.choices
    )
    class Tipo_Pob(models.TextChoices):
        AUT = "AUT", _("Autoridades")
        EMP = "EMP", _("Empresas o emprendedores")
        ONG = "ONG", _("Organizaciones no gubernamentales")
        PF = "PF", _("Personas físicas")
        PM = "PM", _("Personas morales")
        ND = "ND", _("No disponible")
        OTR = "OTR", _("Otro")
    tipo_De_Poblacion= models.CharField(
        max_length=3,
        choices=Tipo_Pob.choices
    )
    requerimientos = models.CharField(max_length=1000)
    class Apoyos(models.TextChoices):
        AT = "AT", _("Asistencia técnica")
        CP = "CP", _("Capacitación")
        CR = "CR", _("Crédito")
        EC = "EC", _("Económico")
        EN = "EN", _("En especie")
        ND = "ND", _("No disponible")
        OT = "OT", _("Otro")
    tipo_Apoyo = models.CharField(
        max_length=2,
        choices=Apoyos.choices
    )
    descripcion_Apoyo = models.CharField(max_length=1000)
    importe = models.IntegerField(null = True)
    maximo = models.BooleanField(null = True)
    #TODO: Monedas como textfield
    moneda = models.CharField(max_length=3)
    class Periodos(models.TextChoices):
        DI = "DI", _("Diaria")
        SE = "SE", _("Semanal")
        QU = "QU", _("Quincenal")
        ME = "ME", _("Mensual")
        BI = "BI", _("Bimestral")
        TR = "TR", _("Trimestral")
        SM = "SM", _("Semestral")
        AN = "AN", _("Anual")
        PU = "PU", _("Pago único")
        OT = "OT", _("Otro")
    periodicidad = models.CharField(
        max_length=2,
        choices=Periodos.choices
    )
    convocatoria_Inicio = models.DateField(null = True)
    convocatoria_Cierre = models.DateField(null = True)
    activo = models.BooleanField(null = True)
    contacto = models.CharField(max_length=1000, default="Contacto",null = True)
    website = models.URLField(null = True)
    email = models.EmailField(null = True)
    telefono = models.CharField(max_length=1000,null = True)