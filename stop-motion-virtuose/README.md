# Stop Motion Virtuose

<p align="center"><img src="icons/icon-512.png" width="140" alt="Icône Stop Motion Virtuose"></p>

Un petit studio de création de films en **stop motion**, pensé pour les enfants et les ados.
Tout fonctionne dans le navigateur, sans installation et sans compte.

## Fonctionnalités

- **Tournage photo par photo** avec la caméra de l'ordinateur, de la tablette ou du téléphone
- **Calque** : la dernière photo s'affiche en transparence pour bien placer ses personnages
- **Formats** paysage ou portrait, choisis à la création du film
- **Fond vert** : pipette pour choisir la couleur à effacer, vues Résultat / Masque / Original, réglages fins (tolérance, douceur, nettoyage, bords, reflets)
- **Images de fond** : décors fixes ou animés, ou tes propres images depuis ta galerie
- **Effets spéciaux** : explosions, BD, nature, magie, effets de caméra
- **Vitesse de lecture** réglable (4 à 24 images par seconde), lecture en boucle, plein écran
- **Annuler** la dernière photo ou la dernière suppression (Ctrl+Z)
- **Doublage** au micro une fois le tournage terminé
- **Export** : vidéo (avec la voix), images PNG en .zip, sauvegarde du projet ; partage direct sur téléphone
- **Projets** : rechercher, renommer, dupliquer, exporter, supprimer
- **Paramètres** : français / anglais, thème clair ou sombre, son, miroir, grille
- Rubrique **Apprendre** : les bases du stop motion, le fond vert, le doublage et les grands films

## Utilisation

Ouvre simplement `index.html` dans un navigateur récent (Chrome, Edge, Safari ou Firefox).
Le navigateur demandera l'autorisation d'utiliser la caméra et le micro.

## Mettre en ligne avec GitHub Pages

1. Crée un dépôt sur GitHub et envoie le contenu de ce dossier à la racine.
2. Va dans **Settings → Pages**.
3. Dans **Source**, choisis **Deploy from a branch**, puis la branche `main` et le dossier `/ (root)`.
4. Après une minute, l'appli est disponible à l'adresse `https://<ton-pseudo>.github.io/<nom-du-depot>/`.

En ligne (HTTPS), la caméra et le micro fonctionnent aussi sur téléphone, et on peut ajouter l'appli à l'écran d'accueil : elle utilise alors l'icône du dossier `icons`.

## Données

Les films sont enregistrés **uniquement dans le navigateur** de l'appareil utilisé (IndexedDB).
Rien n'est envoyé sur internet. Pour changer d'appareil, utilise **Exporter → Sauvegarde du projet**, puis **Importer** sur l'autre appareil.

## Structure

```
index.html        l'application complète (HTML, CSS et JavaScript)
manifest.json     informations pour l'installation sur l'écran d'accueil
icons/            icônes de l'application
```

Une connexion internet sert seulement à charger la police Fredoka et la bibliothèque JSZip (export .zip).
