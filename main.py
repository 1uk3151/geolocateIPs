import maxminddb
from scapy.all import *
from kmltemplate import KMLTemplate

geodatabase = "/home/luke/geolocateIP/GeoLite2-City_20231124/GeoLite2-City.mmdb"
pcap = "/home/luke/geolocateIP/udemy.pcap"
kml_output = "/home/luke/geolocateIP/udemy.kml"

kmltemplate = KMLTemplate(kml_output)


def get_iplist(pcap_file):
    pcap_data = rdpcap(pcap_file)
    ip_list = []
    for i in range(len(pcap_data)):
        pkt = pcap_data[i]
        try:
            ip_list.append(pkt[IP].src)
            ip_list.append(pkt[IP].dst)
        except:
            pass
    return ip_list


def get_coor(ip_address):
    with maxminddb.open_database(geodatabase) as reader:
        try:
            ip_loc = reader.get(ip_address)
            latitude = ip_loc["location"]["latitude"]
            longitude = ip_loc["location"]["longitude"]
            coor_tuple = (ip_address, latitude, longitude)
        except:
            pass
    return coor_tuple


def main():
    ip_list = get_iplist(pcap)
    coor_list = []
    for ip in ip_list:
        try:
            coor_list.append(get_coor(ip))
        except:
            pass
    kmltemplate.kml_heading()
    for coor in coor_list:
        kmltemplate.kml_coordinates(coor[0], coor[1], coor[2])
    kmltemplate.kml_ending()


if __name__ == "__main__":
    main()
