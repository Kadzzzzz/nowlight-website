# NowLight Website

Un site web moderne pour le projet NowLight, développé avec Vue.js 3, Tailwind CSS et Vite.

## 🚀 Installation

### Prérequis
- Node.js 18+ 
- npm ou yarn

### Étapes d'installation

```bash
# 1. Cloner ou télécharger le projet
git clone <your-repo> nowlight-website
cd nowlight-website

# 2. Installer les dépendances
npm install

# 3. Copier vos fichiers de traduction
# Remplacez src/locales/fr.json par votre fichier fr.json complet
# Remplacez src/locales/en.json par votre fichier en.json complet

# 4. Ajouter vos images
# Copiez toutes vos images dans src/assets/images/

# 5. Démarrer le serveur de développement
npm run dev
```

Le site sera accessible sur `http://localhost:5173`

## 🏗️ Architecture

```
src/
├── main.js                 # Point d'entrée de l'application
├── App.vue                 # Composant racine
├── style.css               # Styles globaux avec Tailwind
├── views/                  # Pages principales
│   ├── LanguageSelection.vue
│   └── Home.vue
├── components/
│   ├── common/             # Composants réutilisables
│   │   ├── Navigation.vue
│   │   ├── ModuleCard.vue
│   │   └── Footer.vue
│   ├── sections/           # Sections de la page d'accueil
│   │   ├── HeroSection.vue
│   │   ├── AmbitionSection.vue
│   │   ├── ConceptionSection.vue
│   │   ├── EngagementsSection.vue
│   │   └── ContactSection.vue
│   └── modals/             # Modales
│       └── ModuleModal.vue
├── stores/                 # État global (Pinia)
│   └── language.js
├── locales/                # Fichiers de traduction
│   ├── fr.json
│   └── en.json
└── assets/                 # Ressources statiques
    └── images/
```

## 🌐 Fonctionnalités

### ✅ Implémentées
- Interface multilingue (FR/EN) avec sélection au démarrage
- Design responsive et moderne
- Navigation fluide avec scroll smooth
- Section Hero avec toggle mode éco/standard
- Section Ambition avec animations
- Section Conception avec modules cliquables
- Section Engagements avec icônes animées
- Section Contact avec formulaire fonctionnel
- Modales pour afficher les détails des modules
- Support vidéos YouTube intégrées
- Galerie d'images avec navigation
- Footer complet avec liens sociaux
- Animations et effets visuels modernes

### 🎨 Design
- Palette de couleurs orange/bleu/noir
- Effets de glassmorphism et backdrop-blur
- Animations CSS fluides
- Gradients et effets de lumière
- Design dark/light selon les sections
- Micro-interactions sur hover

### 📱 Responsive
- Mobile First approach
- Breakpoints: mobile, tablet, desktop
- Navigation mobile avec hamburger menu
- Modales optimisées pour mobile
- Images adaptatives

## 🛠️ Scripts disponibles

```bash
# Développement
npm run dev          # Serveur de développement

# Production
npm run build        # Build pour production
npm run preview      # Prévisualiser le build

# Docker
docker build -t nowlight-website .
docker run -p 80:80 nowlight-website
```

## 📁 Fichiers importants à personnaliser

### 1. Traductions (OBLIGATOIRE)
```bash
src/locales/fr.json  # Remplacer par votre fichier fr.json complet
src/locales/en.json  # Remplacer par votre fichier en.json complet
```

### 2. Images (OBLIGATOIRE)
```bash
src/assets/images/   # Ajouter toutes vos images de modules
```

### 3. Configuration
```bash
src/stores/language.js       # Configuration des langues
src/components/sections/     # Personnaliser le contenu des sections
```

## 🔧 Personnalisation

### Couleurs
Modifiez `tailwind.config.js` pour changer la palette :
```javascript
colors: {
  'nowlight': {
    'orange': { /* vos couleurs */ }
  }
}
```

### Contenu
- Modifiez les fichiers dans `src/components/sections/` pour le contenu
- Ajustez `src/stores/language.js` pour la gestion des langues
- Personnalisez `src/components/modals/ModuleModal.vue` pour l'affichage des modules

### Images
- Placez toutes vos images dans `src/assets/images/`
- Les noms doivent correspondre à ceux dans vos fichiers JSON
- Formats supportés: JPG, PNG, SVG

## 🐳 Déploiement Docker

Le projet inclut un Dockerfile optimisé pour la production :

```bash
# Build
docker build -t nowlight-website .

# Run
docker run -p 80:80 nowlight-website
```

### Via Git (recommandé)
```bash
# Sur votre serveur
git clone <your-repo>
cd nowlight-website
docker build -t nowlight-website .
docker run -d -p 80:80 --name nowlight nowlight-website
```

## 🤝 Développement

### Structure des composants
- Utilisez la Composition API de Vue 3
- Styles avec Tailwind CSS uniquement
- Store Pinia pour l'état global
- Vue Router pour la navigation

### Conventions
- Noms de composants en PascalCase
- Props avec validation TypeScript-style
- Émission d'événements explicites
- Code commenté en français

## 📞 Support

Pour toute question technique :
- Vérifiez que Node.js 18+ est installé
- Vérifiez que les fichiers de traduction sont corrects
- Vérifiez que les images sont dans le bon dossier
- Consultez la console du navigateur pour les erreurs

## 📝 Licence

© 2025 NowLight. Tous droits réservés.