
# README - Projet d'Application Web d'Observations de Mammifères en Angleterre

Ce projet consiste en une application web permettant d'afficher des observations de mammifères en Angleterre sur une carte interactive. L'application utilise FastAPI pour accéder à une base de données contenant ces observations et une interface Streamlit pour afficher les données de manière conviviale.

## Instructions d'installation

Pour utiliser cette application, suivez ces étapes d'installation :

1. **Téléchargez le projet :** Clonez ce référentiel Git ou téléchargez-le sous forme de fichier ZIP et décompressez-le.

2. **Décompressez le fichier Mammal :** Assurez-vous d'avoir le fichier de données Mammal et décompressez-le dans le répertoire du projet.

3. **Lancez les containers Docker :** Ouvrez un terminal, naviguez vers le répertoire du projet et exécutez la commande suivante pour lancer les containers Docker :

   ```
   docker-compose up -d
   ```

   Cette commande va construire et démarrer les containers nécessaires pour l'application.

4. **Accédez à l'application :** Une fois que les containers sont en cours d'exécution, ouvrez votre navigateur Web et accédez à l'adresse suivante : [http://localhost:8501](http://localhost:8501)

## Utilisation de l'application

Une fois l'application lancée dans votre navigateur, vous pouvez effectuer les actions suivantes :

- **Afficher les observations de mammifères :** Utilisez les options de l'interface pour sélectionner les animaux dont vous souhaitez afficher les observations sur la carte.

- **Naviguer sur la carte :** Utilisez les outils de zoom et de déplacement sur la carte pour explorer les différentes observations.

- **Obtenir des détails sur les observations :** Cliquez sur les marqueurs de la carte pour obtenir des informations détaillées sur chaque observation.

