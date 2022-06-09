1. create DNS Autorizty by 

```
❯ python3 create_dns_authorization_sync.py
Waiting for operation to complete...
name: "projects/cliu201/locations/global/dnsAuthorizations/cliuauth1"
create_time {
  seconds: 1654771775
  nanos: 200550635
}
update_time {
  seconds: 1654771775
  nanos: 200550635
}
domain: "ltapi.goodvm.net"
dns_resource_record {
  name: "_acme-challenge.ltapi.goodvm.net."
  type_: "CNAME"
  data: "cbdc3ff3-57bf-4bb0-8493-d7da2968f03e.9.authorize.certificatemanager.goog."
}
```

2. create the CNAME by step1's output: dns_resource_record
- name: _acme-challenge.ltapi.goodvm.net.
- type: CNAME
- value: cbdc3ff3-57bf-4bb0-8493-d7da2968f03e.9.authorize.certificatemanager.goog

3. create certification/map/mapEntry 

4. Attach the certificate map to the https target proxy