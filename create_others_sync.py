from google.cloud import certificate_manager_v1

HOSTNAME = "ltapi.goodvm.net"
project_id = "cliu201"
DNS_AUTHORIZATION_ID = "cliuauth1"
CA_ID = "cert-100"
CA_MAP_ID = "ca-map-ltapi"
CA_MAP_ENTRY_ID = "ca-map-ltmap-entry1"

# Create a client
client = certificate_manager_v1.CertificateManagerClient()

def sample_create_certificate():


    # Initialize request argument(s)
    my_certificate = certificate_manager_v1.Certificate(
        managed = certificate_manager_v1.Certificate.ManagedCertificate(
        domains=[HOSTNAME],
        dns_authorizations = [f"projects/{project_id}/locations/global/dnsAuthorizations/{DNS_AUTHORIZATION_ID}"]),)
    # my_certificate.managed = certificate_manager_v1.Certificate.ManagedCertificate(
    #     domains=[HOSTNAME],
    #     dns_authorizations = [DNS_AUTHORIZATION_ID])
    

    # Initialize request argument(s)
    request = certificate_manager_v1.CreateCertificateRequest(
        parent=f"projects/{project_id}/locations/global",
        certificate_id=CA_ID,
        certificate = my_certificate,
    )

    # Make the request
    operation = client.create_certificate(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print("########################Certificate Created#########################\n")
    print(response)

def create_certificate_map():
    # Initialize request argument(s)
    request = certificate_manager_v1.CreateCertificateMapRequest(
        parent=f"projects/{project_id}/locations/global",
        certificate_map_id=CA_MAP_ID,
    )

    # Make the request
    operation = client.create_certificate_map(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print("########################Certificate Mapping Created#########################\n")
    print(response)

def create_certificate_map_entry():
    # Create a client
    client = certificate_manager_v1.CertificateManagerClient()

    # Initialize request argument(s)
    certificate_map_entry = certificate_manager_v1.CertificateMapEntry()
    certificate_map_entry.hostname = HOSTNAME
    certificate_map_entry.certificates = [f"projects/{project_id}/locations/global/certificates/{CA_ID}"]

    request = certificate_manager_v1.CreateCertificateMapEntryRequest(
        parent=f"projects/{project_id}/locations/global/certificateMaps/{CA_MAP_ID}",
        certificate_map_entry_id=CA_MAP_ENTRY_ID,
        certificate_map_entry=certificate_map_entry,
    )

    # Make the request
    operation = client.create_certificate_map_entry(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print("########################Certificate Mapping Entry Created#########################\n")
    print(response)

if __name__ == '__main__':
    # sample_create_certificate()
    # create_certificate_map()
    create_certificate_map_entry()