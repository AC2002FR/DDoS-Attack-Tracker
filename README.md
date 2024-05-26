# DDoS Attack Tracker

## Description

🇫🇷 - **DDoS Attack Tracker** est un outil conçu pour suivre et analyser les attaques par déni de service distribué (DDoS). Il utilise Python pour le traitement des données et Cassandra, une base de données NoSQL, pour le stockage. L'objectif principal est de fournir une surveillance en temps réel des attaques DDoS, de stocker les données d'attaque pour une analyse ultérieure, et d'offrir une interface intuitive pour visualiser ces données.

🇬🇧 - **DDoS Attack Tracker** is a tool designed to track and analyze Distributed Denial-of-Service (DDoS) attacks. It uses Python for data processing and Cassandra, a NoSQL database, for storage. The main goal is to provide real-time monitoring of DDoS attacks, store attack data for later analysis, and offer an intuitive interface for visualizing this data.

## Technologies Used

- Python
- Cassandra

## Prerequisites

- Python 3.x
- Cassandra
- pip 

## Installation

1. Clone the repository :
   ```sh
   git clone https://github.com/AC2002FR/ddos-attack-tracker.git
   ```
   
2. Navigate to the project directory :
   ```sh
   cd ddos-attack-tracker
   ```

3. Install the required packages :
   ```sh
   pip install -r requirements.txt
   ```
   
4. Set up Cassandra by creating a keyspace and table :
   ```sh
   CREATE KEYSPACE ddos WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
   USE ddos;
   CREATE TABLE attacks (
       id UUID PRIMARY KEY,
       timestamp TIMESTAMP,
       source_ip TEXT,
       destination_ip TEXT,
       attack_type TEXT
   );
   ```
   
## Usage 

1. Run the DDoS tracker script :
```sh
python ddos_tracker.py
``` 

2. The script will start monitoring and logging DDoS attacks in real-time. 













 
