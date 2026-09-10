# Especificación de Casos de Uso (CRUD)

Este documento detalla la estructura CRUD (Create, Read, Update, Delete) para cada una de las entidades del sistema.

---

## 1. Entidad: Cliente

| Operación | ID Caso de Uso | Nombre del Caso de Uso | Descripción |
| :--- | :--- | :--- | :--- |
| **Create** | `CU-05` | Registrar Cliente | Permite dar de alta a un nuevo cliente en el sistema con sus datos básicos. |
| **Read** | `CU-06` | Consultar Cliente | Permite buscar y ver la información detallada de un cliente registrado. |
| **Update** | `CU-07` | Actualizar Cliente | Permite modificar la información personal y de contacto del cliente. |
| **Delete** | `CU-08` | Inactivar Cliente | Permite realizar un borrado lógico (inactivación) de un cliente en la base de datos. |

---

## 2. Entidad: Cuenta (`CuentaAhorros` / `CuentaCorriente`)

| Operación | ID Caso de Uso | Nombre del Caso de Uso | Descripción |
| :--- | :--- | :--- | :--- |
| **Create** | `CU-09` | Registrar Cuenta | Permite la apertura y vinculación de una nueva cuenta bancaria a un cliente. |
| **Read** | `CU-02` / `CU-10` | Consultar Cuenta / Saldo | Permite consultar el saldo disponible, sobregiro y datos de la cuenta. |
| **Update** | `CU-11` | Actualizar Estado / Cupo | Permite actualizar el cupo de sobregiro o el estado de la cuenta. |
| **Delete** | `CU-12` | Cancelar Cuenta | Permite el cierre definitivo o inactivación de la cuenta bancaria. |

---

## 3. Entidad: Factura

| Operación | ID Caso de Uso | Nombre del Caso de Uso | Descripción |
| :--- | :--- | :--- | :--- |
| **Create** | `CU-13` | Registrar / Emitir Factura | Genera una nueva obligación de pago asociada a un cliente o servicio. |
| **Read** | `CU-04` / `CU-14` | Consultar Factura | Permite buscar y visualizar el detalle de cobros y montos de una factura. |
| **Update** | `CU-15` | Actualizar Factura | Permite la corrección de datos o estados antes de su recaudo. |
| **Delete** | `CU-16` | Anular Factura | Permite la anulación lógica de una factura emitida por inconsistencias. |

---

## 4. Entidad: Pago

| Operación | ID Caso de Uso | Nombre del Caso de Uso | Descripción |
| :--- | :--- | :--- | :--- |
| **Create** | `CU-01` / `CU-17` | Registrar Pago | Procesa la transacción debitando de la cuenta e imputando a la factura. |
| **Read** | `CU-03` / `CU-18` | Consultar Comprobante | Genera y muestra la confirmación de la transacción realizada. |
| **Update** | `CU-19` | Actualizar Observaciones | Permite adjuntar notas o referencias de auditoría a la transacción. |
| **Delete** | `CU-20` | Revertir Pago | Ejecuta una transacción de reverso (delete lógico) sobre un pago procesado. |

---

## Notas de Implementación

- **Borrado Lógico:** Las operaciones clasificadas como *Delete* (`CU-08`, `CU-12`, `CU-16`, `CU-20`) no eliminan registros físicos en la base de datos; cambian el estado del registro a `Inactivo`, `Anulado` o `Revertido` para mantener la trazabilidad.
- **Trazabilidad:** Cada operación *Create*, *Update* y *Delete* debe registrar automáticamente la fecha, hora y el usuario/sistema que ejecutó la acción.