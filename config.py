# Global Variables
parameters = ["PM", "SO2"]
units = ["mg/Nm3", "mg/Nm3"]
analyzers = ["analyzer_495","analyzer_767"]
MinMa = [4, 4]
MaxMa= [20, 20]
channels = [0, 1]
maxAbs = [100, 800]
multiplyFactors = [1, 1]

site_id = "site_2972"
plant_name = "M/S ROURKELA STEEL PLANT"
plant_address1 = "Rourkela Rourkela"
plant_address2 = "751002 Odisha"
plant_country = "India"
version = "ver1.0"

station_name = "CEMS_19"
iso_latitude = "20.8653"
iso_longtitude = "85.1842"
fsw = site_id+"_"+station_name+"_"
comport = "/dev/ttyUSB0"

# Grewal AES key
AES256_KEY = "c2l0ZV8yOTcyXnZlcl8xLjBeT1NQQ0Je"

# Site Sunjray Public Key
site_public_key = "MEgCQQCNcQYZH8Ylfss8vqZ9bLytRRp2Mw9o3wF1LabrcG7n8XRQ9IayZlX25s7/\nBPjuBkLw+xsNYU85D00uyZQq0YhnAgMBAAE="

# OSPCB Server Public Key
server_public_key = "MEgCQQCcADcRmHrTtDWsknzx5D64iNdwYscWi0+fI8nh9cO26HtRSeXBnSJuMlJK\nis7qn+lznsbi3DRwYOdM4w/7Z8bhAgMBAAE="

# Site private key
site_private_key = "MIIBPAIBAAJBAI1xBhkfxiV+yzy+pn1svK1FGnYzD2jfAXUtputwbufxdFD0hrJm\nVfbmzv8E+O4GQvD7Gw1hTzkPTS7JlCrRiGcCAwEAAQJAHL4pJRXl6Fy55GBB6R8d\nwIBYfkimCwO2gh+C2jmAvg8mqQ0S08YNQKbzYhfXt/PAPY3IaijiqCN549fS3R8p\n0QIjAPbI4cLCOTO9L+OdWP8DpHEIwb33O18lI1DdrWnj4+UpKx0CHwCSuR9NXNhF\nbHIfW8vtKYV6PnwxsvEcP6IcV7eHZlMCIkzofbL8ZGdDZlFBECMpN24ilH5nNhGI\nuWDSNODzLGqWUeECHgrJ5/5VTGXWcpHRuy4GNpVlkNZKtSYBm9b/sDQZlwIjAIep\na+GVH+5Ihtk3+hLFHCFXLoMHeUNxYGHDqzCDYn3pGkY="


# IP Addresses
sunjray_hostAddress = "103.112.26.250:9093"
ospcb_hostAddress = "ospcb-rtdas.com"
central_hostAddress="110.44.98.203:8085"

# Sunjray Realtime and Delayed urls
sunjray_realtime_url = "http://103.112.26.250:9093/sunjrayServer/realtimeUpload"
sunjray_delayed_url = "http://103.112.26.250:9093/sunjrayServer/delayedUpload"

# OSPCB Realtime and Delayed urls
ospcb_realtime_url = "https://ospcb-rtdas.com/OSPCBRTDASServer/realtimeUpload"
ospcb_delayed_url = "https://ospcb-rtdas.com/OSPCBRTDASServer/delayedUpload"

# Central Realtime and Delayed urls
central_realtime_url = "http://110.44.98.203:8085/jitplServer/realtimeUpload"
central_delayed_url = "http://110.44.98.203:8085/jitplServer/delayedUpload"

# Required directories for project functioning
bkpdir = "BKPFLD"
cpcbdir = "CPCB"
spcbdir = "SPCB"
centraldir = "CENTRAL"

# Required directories in CPCB and SPCB for zipfile storing
rtdir = "Realtime"
dlydir = "Delayed"