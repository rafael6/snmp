#Excersise 2, week 1.

__author__ = 'rafael'

from snmp_helper import snmp_get_oid, snmp_extract

community_string = '******'
oids = {'sysName': '1.3.6.1.2.1.1.5.0', 'sysDescr': '1.3.6.1.2.1.1.1.0'}
snmp_ports = [****, ****]
ip_addr = '*******'


def extract_data(node, oid):
    """Returns an OID object from a given device and SNMP OID."""
    return snmp_extract(snmp_get_oid(node, oid))


def main():
    """Create an SNMP devices and retrieves a specific OID object from lists"""
    for port in snmp_ports:
        device = (ip_addr, community_string, port)
        print 'BELOP INFORMATION FOR SOCKET %s:%d\n'% (ip_addr, port)
        print 'HOSTNAME:\n%s\n' % extract_data(device, oids['sysName'])
        print 'DESCRIPTION:\n%s\n' % extract_data(device, oids['sysDescr'])

if __name__ == "__main__":
    main()
