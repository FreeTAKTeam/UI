"""
Module for generating RSA key pairs and self-signed certificates.
"""

import datetime
import pathlib

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

CERT_NAME = "cert.pem"
KEY_NAME = "key.pem"
BASE_PATH = pathlib.Path("/opt/fts/fts_ui")

def generate_rsa_key_pair() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    """
    Generate a RSA key pair and return the private and public keys.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    return private_key, private_key.public_key()


def generate_self_signed_cert(common_name: str, public_key: rsa.RSAPublicKey, private_key: rsa.RSAPrivateKey):
    """
    Generate a self-signed certificate with the given common name and public key.
    """
    subject = issuer = x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, common_name)
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        public_key
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=10 * 365)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName("localhost"), x509.DNSName("127.0.0.1")]),
        critical=False,
    ).sign(private_key, hashes.SHA256())
    return cert


def generate_certificates() -> tuple[pathlib.Path, pathlib.Path]:
    """
    Generate a self-signed certificate and private key, and return their paths.
    """
    cert_path = BASE_PATH / CERT_NAME
    key_path = BASE_PATH / KEY_NAME
    if not BASE_PATH.exists():
        BASE_PATH.mkdir(parents=True, exist_ok=True)

    if cert_path.exists() and key_path.exists():
        return pathlib.Path(CERT_NAME), pathlib.Path(KEY_NAME)

    private_key, public_key = generate_rsa_key_pair()

    cert = generate_self_signed_cert("localhost", public_key, private_key)

    with open(cert_path, "wb") as cf:
        cf.write(cert.public_bytes(serialization.Encoding.PEM))

    with open(key_path, "wb") as kf:
        kf.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))

    return cert_path, key_path