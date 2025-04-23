from scapy.all import sniff, ARP, DNSQR, TCP, Raw, IP  
from collections import defaultdict  #para contar respuestas ARP eficientemente
import re  #buscar patrones en texto (epico)

#diccionario para contar respuestas ARP por IP origen
arp_replies = defaultdict(int)  #si una clave no existe, se inicializa en 0

#funcion que se ejecuta por cada paquete capturado
def packet_callback(pkt):

    #deteccion de ARP Spoofing (suplantamiento de identidad de direcciones MAC!) 
    if pkt.haslayer(ARP) and pkt[ARP].op == 2:  #si un paquete tiene una capa ARP ,si es una ARP respuesta (op=2 es "is-at")
        src_ip = pkt[ARP].psrc  #ip origen de la respuesta
        arp_replies[src_ip] += 1  #incrementamos el contador para esta IP
        
        #si una IP manda mas de 5 respuestas ARP, es sospechoso (rarito)
        if arp_replies[src_ip] > 5:
            print(f"[ALERTA] Posible ARP Spoofing desde {src_ip}")


    #detecta si se va informacion sensible en http
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):  #si es un paquete TCP con datos
        payload = pkt[Raw].load.decode(errors="ignore")  #decodificar el contenido
        
        #buscamos metodos HTTP POST o GET
        if "POST" in payload or "GET" in payload:
            #regex para buscar campos de usuario/email
            user_match = re.search(r"(username|user|email).{0,10}=", payload, re.I)
            #regex para buscar campos de contrasenia
            pass_match = re.search(r"(password|pass).{0,10}=", payload, re.I)
            
            #si se encuentra patrones 
            if user_match or pass_match:
                print("[ALERTA] Posibles credenciales encontradas en tráfico HTTP:")
                print(payload[:300])  #mostrar solo los primeros 300 caracteres


    #deteccion de consultas DNS a dominios "inusuales"
    if pkt.haslayer(DNSQR):  #si es una consulta DNS
        domain = pkt[DNSQR].qname.decode()  #dominio consultao y guardado
        
        #alertamos si el dominio NO termina en .com, .net o .org
        if not domain.endswith(".com") and not domain.endswith(".net") and not domain.endswith(".org"):
            print(f"[ALERTA] Consulta DNS sospechosa: {domain}")


print("Sniffeando... CTRL+C para salir!")

#prn: cuando agarra un paquete lo analizamos y vemos si cumple alguna de las funciones
#store=False: No guardar paquetes en memoria (mejora el rendimiento)
sniff(prn=packet_callback, store=False)