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
            Une solution d'éclairage durable et accessible, utilisant l'énergie humaine pour générer de la lumière instantanément.
          </p>

          <!-- Social Links -->
          <div class="flex space-x-4">
            <a
              href="#"
              class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-orange-500 transition-all duration-300 transform hover:scale-110"
              aria-label="Facebook"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
            </a>
            <a
              href="#"
              class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-blue-500 transition-all duration-300 transform hover:scale-110"
              aria-label="Twitter"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
              </svg>
            </a>
            <a
              href="#"
              class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-pink-500 transition-all duration-300 transform hover:scale-110"
              aria-label="Instagram"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 6.624 5.367 11.99 11.988 11.99s11.99-5.366 11.99-11.99C24.007 5.367 18.641.001 12.017.001zM8.449 16.988c-1.297 0-2.448-.49-3.323-1.295C4.198 14.97 3.66 13.781 3.66 12.496c0-1.284.538-2.473 1.466-3.197.875-.806 2.026-1.295 3.323-1.295s2.448.489 3.323 1.295c.928.724 1.466 1.913 1.466 3.197 0 1.285-.538 2.474-1.466 3.197-.875.805-2.026 1.295-3.323 1.295zm7.046-9.39h-1.327V6.57h1.327v1.029zm-2.205 4.898c0-.825-.221-1.6-.61-2.266-.389-.667-.95-1.197-1.63-1.54-.68-.343-1.434-.518-2.196-.518s-1.516.175-2.196.518c-.68.343-1.241.873-1.63 1.54-.389.666-.61 1.441-.61 2.266 0 .825.221 1.6.61 2.266.389.667.95 1.197 1.63 1.54.68.343 1.434.518 2.196.518s1.516-.175 2.196-.518c.68-.343 1.241-.873 1.63-1.54.389-.666.61-1.441.61-2.266z"/>
              </svg>
            </a>
            <a
              href="#"
              class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-blue-600 transition-all duration-300 transform hover:scale-110"
              aria-label="LinkedIn"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
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
              <span class="text-gray-300 text-sm">projectnowlight@gmail.com</span>
            </div>
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              <span class="text-gray-300 text-sm">69130 Écully, France</span>
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
            © 2025 NowLight. {{ t.footer.rights }}
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