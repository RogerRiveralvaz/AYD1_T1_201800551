# Tarea #2 - Identificar Requerimientos

## Análisis de Requerimientos para Walmart.com

**Universidad San Carlos de Guatemala**  
**Facultad de Ingeniería**  
**Ingeniería en Ciencias y Sistemas**  
**Análisis y Diseño de Sistemas 1**

---

## Introducción

Este documento presenta el análisis de requerimientos funcionales y no funcionales del sitio web de comercio electrónico Walmart.com, identificando los actores principales y modelando las interacciones del sistema mediante un diagrama de casos de uso.

---

## Requerimientos Funcionales

Los requerimientos funcionales describen **qué** debe hacer el sistema Walmart.com:

### RF01 - Registro de Usuario

El sistema debe permitir a nuevos usuarios crear una cuenta proporcionando información personal básica (nombre, email, contraseña, dirección).

### RF02 - Autenticación de Usuario

El sistema debe validar las credenciales de usuarios registrados y permitir el acceso a funcionalidades personalizadas.

### RF03 - Búsqueda de Productos

El sistema debe permitir buscar productos utilizando palabras clave, filtros por categoría, precio, marca, calificaciones y disponibilidad.

### RF04 - Gestión del Carrito de Compras

El sistema debe permitir agregar, eliminar, modificar cantidades y guardar productos en el carrito de compras.

### RF05 - Procesamiento de Pagos

El sistema debe procesar pagos mediante múltiples métodos (tarjetas de crédito/débito, PayPal, Walmart Pay) de forma segura.

### RF06 - Gestión de Pedidos

El sistema debe generar órdenes de compra, enviar confirmaciones por email y permitir el seguimiento del estado del pedido.

### RF07 - Sistema de Reseñas y Calificaciones

El sistema debe permitir a los clientes calificar productos (1-5 estrellas) y escribir reseñas detalladas.

### RF08 - Gestión de Inventario

El sistema debe mostrar disponibilidad en tiempo real, ubicaciones de tiendas físicas y opciones de entrega.

### RF09 - Recomendaciones Personalizadas

El sistema debe sugerir productos basados en el historial de compras, productos visualizados y preferencias del usuario.

### RF10 - Servicio al Cliente

El sistema debe proporcionar chat en vivo, sistema de tickets de soporte y FAQ para resolver consultas de los clientes.

---

## Requerimientos No Funcionales

Los requerimientos no funcionales describen **cómo** debe comportarse el sistema:

### RNF01 - Rendimiento

El sistema debe cargar páginas principales en menos de 2 segundos y procesar búsquedas en menos de 1 segundo bajo condiciones normales.

### RNF02 - Escalabilidad

El sistema debe soportar hasta 100,000 usuarios concurrentes durante eventos de alta demanda (Black Friday, ofertas especiales).

### RNF03 - Disponibilidad

El sistema debe mantener un 99.9% de disponibilidad anual, con un tiempo máximo de inactividad planificada de 4 horas mensuales.

### RNF04 - Seguridad

El sistema debe implementar encriptación SSL/TLS, cumplir con estándares PCI DSS para pagos y proteger datos personales según normativas de privacidad.

### RNF05 - Usabilidad

El sistema debe ser intuitivo para usuarios de todas las edades, con navegación clara y accesibilidad para personas con discapacidades (WCAG 2.1).

### RNF06 - Compatibilidad

El sistema debe funcionar correctamente en los principales navegadores (Chrome, Firefox, Safari, Edge) y ser completamente responsive para dispositivos móviles.

### RNF07 - Mantenibilidad

El código debe ser modular, bien documentado y permitir actualizaciones sin interrumpir el servicio mediante arquitectura de microservicios.

### RNF08 - Confiabilidad

El sistema debe tener mecanismos de backup automático, recuperación ante fallos y redundancia en componentes críticos.

### RNF09 - Capacidad

El sistema debe almacenar información de al menos 10 millones de productos y 50 millones de usuarios registrados.

### RNF10 - Compliance

El sistema debe cumplir con regulaciones de comercio electrónico, leyes de protección de datos (GDPR, CCPA) y estándares de accesibilidad.

---

## Identificación de Actores

### Actores Primarios

- **Cliente**: Usuario que navega, compra productos y gestiona su cuenta
- **Administrador de Tienda**: Gestiona inventario, precios y información de productos
- **Administrador del Sistema**: Supervisa operaciones técnicas y seguridad
- **Empleado de Servicio al Cliente**: Atiende consultas y resuelve problemas

### Actores Secundarios

- **Sistema de Pagos**: Procesa transacciones financieras
- **Sistema de Envíos**: Gestiona logística y tracking de pedidos
- **Proveedores**: Actualizan inventario y información de productos
- **Sistema de Email**: Envía notificaciones y confirmaciones

---

## Conclusiones

El análisis de Walmart.com revela un sistema complejo que debe balancear funcionalidad, rendimiento y seguridad. Los requerimientos identificados abarcan desde operaciones básicas de comercio electrónico hasta características avanzadas como recomendaciones personalizadas y integración con sistemas externos.

La arquitectura debe soportar alta concurrencia, garantizar transacciones seguras y proporcionar una experiencia de usuario excepcional en múltiples dispositivos y plataformas.
