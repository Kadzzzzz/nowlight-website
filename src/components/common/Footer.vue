<template>
  <footer class="bg-gradient-to-r from-gray-900 to-black text-white">
    <!-- Main Footer Content -->
    <div class="container mx-auto px-6 py-12">
      <div class="grid md:grid-cols-4 gap-8">
        <!-- Logo & Description -->
        <div class="md:col-span-2">
          <h3 class="text-3xl font-bold mb-4 bg-gradient-to-r from-white to-orange-400 bg-clip-text text-transparent">
            NowLight
          </h3>
          <p class="text-gray-300 mb-6 max-w-md leading-relaxed">
            Une solution d'éclairage durable et accessible, utilisant l'énergie humaine pour générer de la lumière.
          </p>

          <!-- Social Links -->
          <div class="flex space-x-4">
            <a
              href="https://www.linkedin.com/in/jeremy-luccioni-695365bb/"
              target="_blank"
              rel="noopener noreferrer"
              class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-blue-600 transition-all duration-300 transform hover:scale-110"
              aria-label="LinkedIn"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
            </a>
            <a
              href="https://github.com/Kadzzzzz/nowlight-website"
              target="_blank"
              rel="noopener noreferrer"
              class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-gray-700 transition-all duration-300 transform hover:scale-110"
              aria-label="GitHub"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-lg font-semibold mb-4 text-orange-400">Navigation</h4>
          <ul class="space-y-2">
            <li>
              <a href="#ambition" class="text-gray-300 hover:text-white transition-colors duration-300">
                {{ t.nav.ambition }}
              </a>
            </li>
            <li>
              <a href="#conception" class="text-gray-300 hover:text-white transition-colors duration-300">
                {{ t.nav.conception }}
              </a>
            </li>
            <li>
              <a href="#engagements" class="text-gray-300 hover:text-white transition-colors duration-300">
                {{ t.nav.engagements }}
              </a>
            </li>
            <li>
              <a href="#contact" class="text-gray-300 hover:text-white transition-colors duration-300">
                {{ t.nav.contact }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div>
          <h4 class="text-lg font-semibold mb-4 text-orange-400">Contact</h4>
          <div class="space-y-3">
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
              </svg>
              <span class="text-gray-300 text-sm">jeremy.luccioni@etu.ec-lyon.fr</span>
            </div>
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              <span class="text-gray-300 text-sm">Centrale Lyon, 36 Av. Guy de Collongue, 69130 Écully</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="border-t border-gray-800">
      <div class="container mx-auto px-6 py-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="text-gray-400 text-sm mb-4 md:mb-0">
            © 2025 NowLight
          </div>

          <!-- Language Selector (Small) -->
          <div class="flex items-center space-x-4">
            <span class="text-gray-400 text-sm">Language:</span>
            <button
              @click="changeLanguage('fr')"
              class="text-gray-300 hover:text-white transition-colors duration-300 text-sm"
              :class="{ 'text-orange-400': currentLanguage === 'fr' }"
            >
              🇫🇷 FR
            </button>
            <span class="text-gray-600">|</span>
            <button
              @click="changeLanguage('en')"
              class="text-gray-300 hover:text-white transition-colors duration-300 text-sm"
              :class="{ 'text-orange-400': currentLanguage === 'en' }"
            >
              🇬🇧 EN
            </button>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { useLanguageStore } from '../../stores/language'

const languageStore = useLanguageStore()
const t = computed(() => languageStore.t)
const currentLanguage = computed(() => languageStore.currentLanguage)

const changeLanguage = (lang) => {
  languageStore.setLanguage(lang)
}
</script>