#!/usr/bin/env python3
"""
Générateur d'architecture pour le projet NowLight Vue.js
"""

import os
import json
from pathlib import Path


def create_directory_structure():
    """Crée la structure de dossiers du projet"""

    # Structure des dossiers
    directories = [
        "src",
        "src/components",
        "src/components/common",
        "src/components/sections",
        "src/components/modals",
        "src/stores",
        "src/locales",
        "src/views",
        "src/assets",
        "src/assets/images",
        "src/assets/styles",
        "public"
    ]

    # Créer les dossiers
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Dossier créé: {directory}")


def create_package_json():
    """Crée le fichier package.json"""
    package_json = {
        "name": "nowlight-website",
        "version": "1.0.0",
        "description": "NowLight project website",
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        },
        "dependencies": {
            "vue": "^3.3.0",
            "vue-router": "^4.2.0",
            "pinia": "^2.1.0",
            "@vueuse/core": "^10.0.0"
        },
        "devDependencies": {
            "@vitejs/plugin-vue": "^4.2.0",
            "vite": "^4.3.0",
            "tailwindcss": "^3.3.0",
            "autoprefixer": "^10.4.0",
            "postcss": "^8.4.0"
        }
    }

    with open("package.json", "w", encoding="utf-8") as f:
        json.dump(package_json, f, indent=2, ensure_ascii=False)
    print("✓ Fichier créé: package.json")


def create_vite_config():
    """Crée le fichier vite.config.js"""
    vite_config = """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': '/src'
    }
  }
})
"""

    with open("vite.config.js", "w", encoding="utf-8") as f:
        f.write(vite_config)
    print("✓ Fichier créé: vite.config.js")


def create_tailwind_config():
    """Crée la configuration Tailwind"""
    tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        }
      }
    },
  },
  plugins: [],
}
"""

    with open("tailwind.config.js", "w", encoding="utf-8") as f:
        f.write(tailwind_config)
    print("✓ Fichier créé: tailwind.config.js")


def create_postcss_config():
    """Crée la configuration PostCSS"""
    postcss_config = """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

    with open("postcss.config.js", "w", encoding="utf-8") as f:
        f.write(postcss_config)
    print("✓ Fichier créé: postcss.config.js")


def create_index_html():
    """Crée le fichier index.html"""
    index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>NowLight - Sustainable Lighting Solution</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("✓ Fichier créé: index.html")


def create_style_css():
    """Crée le fichier de styles principal"""
    style_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    line-height: 1.6;
    color: #333;
  }
}

@layer components {
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s ease;
  }

  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }

  .slide-up-enter-active, .slide-up-leave-active {
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
  }

  .slide-up-enter-from {
    opacity: 0;
    transform: translateY(30px);
  }

  .slide-up-leave-to {
    opacity: 0;
    transform: translateY(-30px);
  }
}
"""

    with open("src/style.css", "w", encoding="utf-8") as f:
        f.write(style_css)
    print("✓ Fichier créé: src/style.css")


def copy_locale_files():
    """Copie les fichiers de traduction fournis"""
    print("\n📁 Copiez maintenant vos fichiers de traduction:")
    print("   - Copiez votre fichier fr.json dans: src/locales/fr.json")
    print("   - Copiez votre fichier en.json dans: src/locales/en.json")

    # Créer des fichiers de base si les originaux ne sont pas disponibles
    fr_basic = {
        "nav": {
            "ambition": "Ambition",
            "conception": "Conception",
            "engagements": "Engagements",
            "contact": "Nous Contacter"
        },
        "hero": {
            "subtitle": "PROJET D'ÉTUDE",
            "title": "NOWLIGHT",
            "ecoModeOff": "Mode Éco",
            "ecoModeOn": "Mode Standard",
            "scrollDown": "Défiler vers le bas"
        }
    }

    en_basic = {
        "nav": {
            "ambition": "Ambition",
            "conception": "Design",
            "engagements": "Commitments",
            "contact": "Contact Us"
        },
        "hero": {
            "subtitle": "STUDY PROJECT",
            "title": "NOWLIGHT",
            "ecoModeOff": "Eco Mode",
            "ecoModeOn": "Standard Mode",
            "scrollDown": "Scroll down"
        }
    }

    with open("src/locales/fr.json", "w", encoding="utf-8") as f:
        json.dump(fr_basic, f, indent=2, ensure_ascii=False)

    with open("src/locales/en.json", "w", encoding="utf-8") as f:
        json.dump(en_basic, f, indent=2, ensure_ascii=False)

    print("✓ Fichiers de traduction de base créés (à remplacer par vos fichiers complets)")


def create_dockerfile():
    """Crée le Dockerfile"""
    dockerfile_content = """# Build stage
FROM node:18-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
"""

    with open("Dockerfile", "w", encoding="utf-8") as f:
        f.write(dockerfile_content)
    print("✓ Fichier créé: Dockerfile")


def create_gitignore():
    """Crée le fichier .gitignore"""
    gitignore_content = """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
"""

    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print("✓ Fichier créé: .gitignore")


def create_readme():
    """Crée le fichier README.md"""
    readme_content = """# NowLight Website

Un site web moderne pour le projet NowLight, développé avec Vue.js 3.

## 🚀 Installation

```bash
# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm run dev

# Construire pour la production
npm run build
```

## 🏗️ Architecture

```
src/
├── components/          # Composants réutilisables
│   ├── common/         # Composants communs
│   ├── sections/       # Sections de page
│   └── modals/         # Modales
├── stores/             # État global (Pinia)
├── views/              # Pages principales
├── locales/            # Fichiers de traduction
└── assets/             # Ressources statiques
```

## 🌐 Fonctionnalités

- ✅ Interface multilingue (FR/EN)
- ✅ Design responsive
- ✅ Navigation fluide
- ✅ Modales interactives
- ✅ Mode éco/standard
- ✅ Animations modernes

## 🐳 Docker

```bash
# Construire l'image
docker build -t nowlight-website .

# Lancer le conteneur
docker run -p 80:80 nowlight-website
```

## 📝 Développement

1. Copiez vos fichiers de traduction complets dans `src/locales/`
2. Ajoutez vos images dans `src/assets/images/`
3. Personnalisez les composants selon vos besoins
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✓ Fichier créé: README.md")


def main():
    """Fonction principale"""
    print("🚀 Génération de l'architecture du projet NowLight...\n")

    # Créer la structure
    create_directory_structure()
    print()

    # Créer les fichiers de configuration
    create_package_json()
    create_vite_config()
    create_tailwind_config()
    create_postcss_config()
    create_index_html()
    create_style_css()
    create_dockerfile()
    create_gitignore()
    create_readme()
    copy_locale_files()

    print(f"\n✅ Architecture créée avec succès!")
    print("\n📋 Prochaines étapes:")
    print("1. cd dans le dossier du projet")
    print("2. Copiez vos fichiers fr.json et en.json dans src/locales/")
    print("3. Ajoutez vos images dans src/assets/images/")
    print("4. npm install")
    print("5. npm run dev")
    print("\n🎉 Votre projet sera accessible sur http://localhost:5173")


if __name__ == "__main__":
    main()