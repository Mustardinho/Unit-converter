# Unit Converter Web Application

A lightweight, responsive, full-stack web application that handles conversions between various units of measurement across different categories. Built with Python and Flask, this project demonstrates foundational concepts of server-side web development, the HTTP request-response cycle, and dynamic UI rendering without relying on a database.

## Features

* **Multi-Category Conversion:** Switch seamlessly between Length, Weight, and Temperature conversion tools using an interactive navigation menu.
* **Server-Side Processing:** All mathematical calculations are computed dynamically on the backend server.
* **Smart Data Structures:** Uses normalized base-unit scaling dictionaries to minimize conditional logic and ensure code scalability.
* **State Preservation:** Keeps user-submitted values and unit dropdown choices selected even after the page reloads with the result.
* **Input Validation:** Built-in server-side exception handling catches non-numeric inputs and provides user-friendly error messages without crashing the application.
* **Custom UI:** Designed with a clean, hand-drawn "sketchy" aesthetic using the Gochi Hand typography and modular CSS.

---

## Tech Stack

* **Backend Engine:** Python
* **Web Framework:** Flask
* **Template Engine:** Jinja2 (for dynamic HTML variable injection and conditional UI states)
* **Frontend Design:** HTML5, CSS3

---

## Project Structure

```text
unit-converter-app/
│
├── app.py              # Main Python server, routing system, and conversion logic
├── static/             # Static assets folder
│   └── style.css       # Global stylesheet for the sketchy UI layout
└── templates/          # HTML view templates executed by Jinja2
    ├── length.html     # Frontend interface for length calculations


https://roadmap.sh/projects/unit-converter
    ├── weight.html     # Frontend interface for mass/weight calculations
    └── temp.html       # Frontend interface for temperature conversions
