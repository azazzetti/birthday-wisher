# birthday-wisher
Automates sending birthday emails using Python, Pandas for data handling, and smtplib for email delivery.

English Description
Automated Birthday Wisher in Python

This project automates the process of sending birthday emails using Python. It reads from a CSV file containing birthday information and matches today's date with any entry. If a match is found, a birthday email is sent using randomly selected letter templates, personalized with the recipient's name.

Features:
CSV Data Handling: Birthdays are stored in a birthdays.csv file, which the program reads to find any birthdays matching today’s date.
Randomized Email Templates: The program randomly selects one of three letter templates, replacing the placeholder [NAME] with the birthday person's name.
Automated Email Sending: Using smtplib, the program sends an email through a Gmail SMTP server to wish the person a happy birthday.

Technologies:
	Python: Core programming language.
	Pandas: For handling and reading the CSV file.
	smtplib: For email handling and sending through an SMTP server.

_____________________________________________________________________________________________________________________________________________________________________________________

Descripción en Castellano
Aplicación Automatizada para Enviar Felicitaciones de Cumpleaños en Python

Este proyecto automatiza el envío de correos electrónicos de cumpleaños utilizando Python. Lee de un archivo CSV que contiene la información de los cumpleaños y coincide la fecha de hoy con cualquier entrada. Si encuentra una coincidencia, envía un correo de felicitación utilizando plantillas de cartas seleccionadas aleatoriamente y personalizadas con el nombre del destinatario.

Funcionalidades:
Gestión de datos CSV: Los cumpleaños se almacenan en un archivo birthdays.csv, que el programa lee para encontrar coincidencias con la fecha actual.
Plantillas de correos aleatorias: El programa selecciona aleatoriamente una de las tres plantillas de cartas y reemplaza el marcador [NAME] por el nombre de la persona que cumple años.
Envío automatizado de correos: Utilizando smtplib, el programa envía un correo electrónico a través del servidor SMTP de Gmail para felicitar al destinatario.

Tecnologías:
	Python: Lenguaje de programación principal.
	Pandas: Para la manipulación y lectura del archivo CSV.
	smtplib: Para manejar y enviar correos electrónicos a través de un servidor SMTP.
