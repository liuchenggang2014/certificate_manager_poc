from google.cloud import certificate_manager_v1

HOSTNAME = "ltapi.goodvm.net"
project_id = "cliu201"
DNS_AUTHORIZATION_ID = "cliuauth1"

def create_dns_authorization():
    # Create a client
    client = certificate_manager_v1.CertificateManagerClient()

    # Initialize request argument(s)
    dns_authorization = certificate_manager_v1.DnsAuthorization()
    dns_authorization.domain = HOSTNAME

    request = certificate_manager_v1.CreateDnsAuthorizationRequest(
        parent=f"projects/{project_id}/locations/global",
        dns_authorization_id=DNS_AUTHORIZATION_ID,
        dns_authorization=dns_authorization,
    )

    # Make the request
    operation = client.create_dns_authorization(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


if __name__ == '__main__':
    create_dns_authorization()
