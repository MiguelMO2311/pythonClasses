from abc import ABC, abstractmethod
import json
import sqlite3
import smtplib
from email.mime.text import MIMEText
import csv

# Principio de Responsabilidad Única (SRP)
class TextSaver:
    def __init__(self, formatter, destination):
        self.formatter = formatter  # DIP: Dependemos de una abstracción (Formatter)
        self.destination = destination  # DIP: Dependemos de una abstracción (Destination)

    def save(self, text):
        formatted_text = self.formatter.format(text)
        print(f"Texto formateado: {formatted_text}")  # Imprimir texto formateado
        self.destination.save(formatted_text)
        print(f"Texto guardado en {self.destination}")  # Confirmar que el texto se ha guardado

# Principio de Abierto/Cerrado (OCP)
class Formatter(ABC):  # ISP: Interfaz específica para formateadores
    @abstractmethod
    def format(self, text):
        pass

class PlainTextFormatter(Formatter):
    def format(self, text):
        return text

class JsonFormatter(Formatter):
    def format(self, text):
        return json.dumps({"text": text})

class XmlFormatter(Formatter):
    def format(self, text):
        return f"<text>{text}</text>"

class HtmlFormatter(Formatter):
    def format(self, text):
        return f"<html><body><p>{text}</p></body></html>"

class CsvFormatter(Formatter):
    def format(self, text):
        return f"text\n{text}"

# Principio de Sustitución de Liskov (LSP)
class Destination(ABC):  # ISP: Interfaz específica para destinos
    @abstractmethod
    def save(self, text):
        pass

class FileDestination(Destination):
    def __init__(self, filename):
        self.filename = filename

    def save(self, text):
        with open(self.filename, 'w') as file:
            file.write(text)
        print(f"Texto guardado en archivo: {self.filename}")  # Confirmar que el texto se ha guardado en el archivo

class SqlDestination(Destination):
    def __init__(self, db_name):
        self.db_name = db_name

    def save(self, text):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS texts (content TEXT)")
        cursor.execute("INSERT INTO texts (content) VALUES (?)", (text,))
        conn.commit()
        conn.close()
        print(f"Texto guardado en base de datos: {self.db_name}")  # Confirmar que el texto se ha guardado en la base de datos

class EmailDestination(Destination):
    def __init__(self, to_email, from_email, smtp_server, smtp_port=587, username=None, password=None):
        self.to_email = to_email
        self.from_email = from_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def save(self, text):
        try:
            msg = MIMEText(text)
            msg['Subject'] = 'TextSaver Email'
            msg['From'] = self.from_email
            msg['To'] = self.to_email

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                if self.username and self.password:
                    server.login(self.username, self.password)
                server.sendmail(self.from_email, self.to_email, msg.as_string())
            print(f"Texto enviado por email a: {self.to_email}")  # Confirmar que el texto se ha enviado por email
        except Exception as e:
            print(f"Error al enviar el email: {e}")  # Imprimir el error si falla el envío del email

# Principio de Segregación de Interfaces (ISP)
# Ya está implementado mediante el uso de interfaces específicas como Formatter y Destination.

# Principio de Inversión de Dependencias (DIP)
# Ya está implementado mediante la inyección de dependencias en el constructor de TextSaver.

# Ejemplo de uso
text = "Hola, mundo!"
formatter = HtmlFormatter()
destination = FileDestination("output.html")

saver = TextSaver(formatter, destination)
saver.save(text)

formatter = CsvFormatter()
destination = FileDestination("output.csv")

saver = TextSaver(formatter, destination)
saver.save(text)

formatter = JsonFormatter()
destination = SqlDestination("output.db")

saver = TextSaver(formatter, destination)
saver.save(text)

formatter = PlainTextFormatter()
destination = EmailDestination("to@example.com", "from@example.com", "smtp.gmail.com", 587, "your_username", "your_password")

saver = TextSaver(formatter, destination)
saver.save(text)
