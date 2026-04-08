from scapy.all import IP, UDP, DNS, DNSQR, sr1

# 1. Craft the layers: IP (Target) / UDP (Port 53) / DNS (Query)
dns_query = IP(dst="8.8.8.8") / \
            UDP(dport=53) / \
            DNS(rd=1, qd=DNSQR(qname="example.com"))

# 2. Send the packet and wait for one answer
response = sr1(dns_query, verbose=0)

# 3. View the response
if response:
    print(response[DNS].summary())

# status = is_alive()
#             if(status==True):
#                 try:
#                     # Check for commands
#                     response = requests.post(f"{SERVER_URL}/ping")
#                     print(response.json())     
#                 except Exception as e:
#                     pass
#                 time.sleep(10) # Poll every 10 seconds