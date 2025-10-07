import os
import boto3

def manage_rds_instances(instance_ids, aws_access_key, aws_secret_access_key):
    """
    Gestiona instancias de RDS: si están disponibles las apaga,
    y si están detenidas las enciende.
    """
    rds = boto3.client(
        'rds',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key
    )

    for instance_id in instance_ids:
        try:
            # Obtener el estado actual de la instancia
            response = rds.describe_db_instances(DBInstanceIdentifier=instance_id)
            status = response['DBInstances'][0]['DBInstanceStatus']

            if status == 'available':
                rds.stop_db_instance(DBInstanceIdentifier=instance_id)
                print(f"Instancia {instance_id} apagada correctamente.")
            elif status == 'stopped':
                rds.start_db_instance(DBInstanceIdentifier=instance_id)
                print(f"Instancia {instance_id} encendida correctamente.")
            else:
                print(f"La instancia {instance_id} se encuentra en estado: {status}. No se realizará ninguna acción.")
        except Exception as e:
            print(f"Error al gestionar la instancia {instance_id}: {str(e)}")

# Obtener credenciales y lista de instancias desde variables de entorno
aws_access_key = os.environ.get('AWS_ACCESS_KEY')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
rds_instances_env = os.environ.get('RDS_INSTANCES')

if aws_access_key and aws_secret_access_key and rds_instances_env:
    # Convertir la cadena de IDs en lista
    rds_instances = rds_instances_env.split(',')

    # Llamar a la función para gestionar las instancias
    manage_rds_instances(rds_instances, aws_access_key, aws_secret_access_key)
else:
    print("No se encontraron las variables de entorno necesarias.")
