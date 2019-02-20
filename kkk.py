from obspy import read_inventory

inv = read_inventory("http://www.orfeus-eu.org/fdsnws/station/1/query?format=sc3ml&station=HGN&level=response&channel=BHZ&location=01")
print inv
