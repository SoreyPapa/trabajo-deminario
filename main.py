from abc import ABC, abstractmethod
from typing import List


# Clase base Usuario
class Usuario(ABC):
    def __init__(self, nombre: str, email: str):
        self.__nombre = nombre
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @abstractmethod
    def enviar_mensaje(self, mensaje, receptor):
        pass


# Usuario común
class UsuarioComun(Usuario):
    def enviar_mensaje(self, mensaje, receptor):
        print(f"{self.nombre} envía mensaje a {receptor.nombre}: {mensaje.contenido}")
        receptor.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(
            f"{self.nombre} recibió un mensaje de {mensaje.remitente.nombre}: {mensaje.contenido}"
        )


# Administrador
class Administrador(Usuario):
    def enviar_mensaje(self, mensaje, receptor):
        print(
            f"[ADMIN] {self.nombre} envía mensaje a {receptor.nombre}: {mensaje.contenido}"
        )
        receptor.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(
            f"[ADMIN] {self.nombre} recibió un mensaje de {mensaje.remitente.nombre}: {mensaje.contenido}"
        )


# Clase Mensaje
class Mensaje:
    def __init__(self, contenido: str, remitente: Usuario):
        self.__contenido = contenido
        self.__remitente = remitente

    @property
    def contenido(self):
        return self.__contenido

    @property
    def remitente(self):
        return self.__remitente


# Clase RedSocial (agregación)
class RedSocial:
    def __init__(self):
        self.__usuarios: List[Usuario] = []

    def registrar_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.nombre} ({usuario.email})")

    def enviar_mensaje(self, remitente: Usuario, receptor: Usuario, contenido: str):
        mensaje = Mensaje(contenido, remitente)
        remitente.enviar_mensaje(mensaje, receptor)


# Código principal (simulación en el main directamente)
if __name__ == "__main__":
    red = RedSocial()

    # Crear usuarios
    juan = UsuarioComun("Juan", "juan@example.com")
    ana = UsuarioComun("Ana", "ana@example.com")
    admin = Administrador("SuperAdmin", "admin@red.com")

    # Registrar usuarios
    red.registrar_usuario(juan)
    red.registrar_usuario(ana)
    red.registrar_usuario(admin)

    # Envío de mensajes
    red.enviar_mensaje(juan, ana, "Hola Ana, ¿cómo estás?")
    red.enviar_mensaje(admin, juan, "Revisa las normas de la comunidad, por favor.")
