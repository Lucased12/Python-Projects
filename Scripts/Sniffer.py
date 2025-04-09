# Github: https://github.com/Lucased12

from scapy.all import sniff
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP, TCP
#con sniff capturamos paquetes de red, httpRequest solicitud, ip y tcp tambien las capas del paquete

def mostrarPaquete(paquete):
    if paquete.haslayer(HTTPRequest):
        http_layer = paquete[HTTPRequest]  #miramos la capa http
        ip_layer = paquete[IP]             #quien envio la solicitud
        
        #DECODE! 
        metodo = http_layer.Method.decode()  #ej: GET, POST
        host = http_layer.Host.decode()      
        path = http_layer.Path.decode()      #ej: /search?q=example
        url = f"http://{host}{path}"         

        print(f"[+] {ip_layer.src} → {metodo} {url}")

print("Sniffeando trafico HTTP... (Ctrl+C para detener)")
sniff(filter="tcp port 80", prn=mostrarPaquete, store=False)
#sniff para capturar paquetes, filter lo dice el nombre, prn llama la funcion, store evita guardar paquetes en memoria

#en caso de alguien estar leyendo esto, ando aprendiendo (^.^).