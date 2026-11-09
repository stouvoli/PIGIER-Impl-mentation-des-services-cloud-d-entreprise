import json
import os
import boto3
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "prod/master1/app"
    region_name = os.environ.get("AWS_REGION", "eu-north-1")

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    return json.loads(response['SecretString'])

if __name__ == "__main__":
    secrets = get_secret()
    db_pass = secrets.get('db_password')
    print(f"[CONNEXION BD] Authentification validée avec le mot de passe récupéré ({len(db_pass)} caractères).")
    del db_pass
    del secrets
EOF
