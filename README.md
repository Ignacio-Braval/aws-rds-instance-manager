# AWS RDS Instance Manager 🚀

Script en Python para **automatizar el encendido y apagado de instancias de Amazon RDS** según su estado actual.

---

## Descripción
Este proyecto permite:
- Apagar automáticamente instancias RDS que están en estado `available`.
- Encender automáticamente instancias RDS que están en estado `stopped`.
- Registrar en consola las acciones realizadas y errores ocurridos.

Ideal para **ahorro de costos**, automatización de entornos de desarrollo o integración en pipelines CI/CD.

---

## Tecnologías
- Python 3.x
- [Boto3](https://boto3.amazonaws.com/) (AWS SDK para Python)
- Variables de entorno para manejo seguro de credenciales

---

## Configuración

1. Crear un archivo `.env` en la raíz del proyecto basado en `.env.example`:

```bash
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
RDS_INSTANCES=db1,db2,db3
