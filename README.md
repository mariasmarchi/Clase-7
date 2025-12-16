SELENIUM TEST SUITE - README
=============================

Este proyecto contiene una suite de pruebas automatizadas con Selenium y Pytest para validar funcionalidades clave de una tienda online (SauceDemo).

Estructura del Proyecto
-----------------------

EntregaSELENIUM/
├── page/                  # Page Objects (LoginPage, CartPage, CheckoutPage, etc.)
│   ├── login_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── inventory_page.py
│
├── test/                  # Casos de prueba
│   ├── test_login_page.py
│   ├── test_busqueda.py
│   ├── test_carrito.py
│   ├── test_checkoutProd.py
│   └── test_checkoutProd_Neg.py
│
├── data/                  # Archivos CSV con datos de prueba
│   └── data_login.csv
│
├── reporte/               # Reportes HTML y capturas de pantalla
│   ├── reporte.html
│   └── *.png
│
├── conftest.py            # Fixtures de Selenium y configuración de Pytest
└── README.txt             # Documentación del proyecto

Casos de Prueba
---------------

1. test_login_page.py
   - Login parametrizado con datos desde CSV
   - Verifica login exitoso y login fallido

2. test_busqueda.py
   - Verifica que un producto específico esté visible en el inventario

3. test_carrito.py
   - Agrega un producto al carrito y valida su presencia

4. test_checkoutProd.py
   - Flujo completo de compra: login → agregar producto → carrito → checkout → confirmación

5. test_checkoutProd_Neg.py
   - Intenta finalizar compra sin productos en el carrito (flujo negativo)

Ejecución de Pruebas
--------------------

Para ejecutar todos los tests y generar un reporte HTML:

    pytest --html=reporte/reporte.html --self-contained-html

Para ejecutar un test específico:

    pytest test/test_checkoutProd.py

Requisitos
----------

- Python 3.10+
- Google Chrome instalado
- Paquetes:

    pip install selenium pytest pytest-html webdriver-manager

Notas Finales
-------------

- Se utiliza el patrón Page Object Model para mantener el código organizado y reutilizable.
- Las capturas de pantalla se guardan automáticamente en la carpeta `reporte/` ante fallos.
- El archivo `data_login.csv` permite probar múltiples combinaciones de usuario/clave.
- El flujo de checkout incluye validaciones positivas y negativas.

