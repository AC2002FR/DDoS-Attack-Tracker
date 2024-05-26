# ddos_tracker.py

import time
import uuid
from cassandra.cluster import Cluster

def log_attack(session, source_ip, destination_ip, attack_type) :
    """
    🇫🇷 - Enregistre une attaque DDoS dans la base de données Cassandra.
    Arguments :
    - session : la session Cassandra pour exécuter les requêtes.
    - source_ip : l'adresse IP source de l'attaque.
    - destination_ip : l'adresse IP cible de l'attaque.
    - attack_type : le type d'attaque DDoS.
    
    🇬🇧 - Logs a DDoS attack into the Cassandra database.
    Arguments :
    - session : the Cassandra session to execute queries.
    - source_ip : the source IP address of the attack.
    - destination_ip : the target IP address of the attack.
    - attack_type : the type of DDoS attack.
    """
    query = """
    INSERT INTO attacks (id, timestamp, source_ip, destination_ip, attack_type)
    VALUES (%s, %s, %s, %s, %s)
    """
    session.execute(query, (uuid.uuid4(), time.time(), source_ip, destination_ip, attack_type))

def main():
    """
    🇫🇷 - Fonction principale qui initialise la connexion à Cassandra et simule la réception de données d'attaque DDoS.
    🇬🇧 - Main function that initializes the connection to Cassandra and simulates receiving DDoS attack data.
    """
    cluster = Cluster(['127.0.0.1'])  # Adresse IP du cluster Cassandra / IP address of the Cassandra cluster
    session = cluster.connect('ddos')  # Connexion à la keyspace 'ddos' / Connect to 'ddos' keyspace

    print("DDoS Tracker démarré... / DDoS Tracker started...")

    while True:
        # Simuler la réception de données d'attaque DDoS / Simulate receiving DDoS attack data
        source_ip = "192.168.1.1"
        destination_ip = "192.168.1.2"
        attack_type = "SYN Flood"
        
        log_attack(session, source_ip, destination_ip, attack_type)
        print(f"Attaque DDoS enregistrée : {source_ip} -> {destination_ip}, Type : {attack_type}")
        print(f"DDoS attack logged: {source_ip} -> {destination_ip}, Type: {attack_type}")
        
        time.sleep(5)  # Attendre 5 secondes avant de recevoir la prochaine attaque / Wait 5 seconds before receiving the next attack

if __name__ == "__main__" :
    main()

