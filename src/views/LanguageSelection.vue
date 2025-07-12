<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-800 flex items-center justify-center relative overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute top-20 left-20 w-72 h-72 bg-orange-500 rounded-full filter blur-3xl"></div>
      <div class="absolute bottom-20 right-20 w-96 h-96 bg-blue-500 rounded-full filter blur-3xl"></div>
    </div>

    <!-- Main Content -->
    <div class="relative z-10 text-center max-w-md w-full mx-4">
      <!-- Logo/Title -->
      <div class="mb-12">
        <h1 class="text-6xl font-bold text-white mb-4 tracking-tight">
          NOWLIGHT
        </h1>
        <div class="w-20 h-1 bg-gradient-to-r from-orange-500 to-orange-600 mx-auto rounded-full"></div>
      </div>

      <!-- Language Selection Card -->
      <div class="bg-white/10 backdrop-blur-xl rounded-2xl border border-white/20 p-8 shadow-2xl">
        <h2 class="text-xl text-white/90 mb-8 font-medium">
          Choisissez votre langue / Choose your language
        </h2>

        <div class="space-y-4">
          <!-- French Button -->
          <button
            @click="selectLanguage('fr')"
            class="w-full group relative overflow-hidden bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 text-white py-4 px-6 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-xl"
          >
            <span class="relative z-10 flex items-center justify-center">
              🇫🇷 Français
            </span>
            <div class="absolute inset-0 bg-gradient-to-r from-white/0 via-white/20 to-white/0 transform -skew-x-12 -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
          </button>

          <!-- English Button -->
          <button
            @click="selectLanguage('en')"
            class="w-full group relative overflow-hidden bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-400 hover:to-orange-500 text-white py-4 px-6 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-xl"
          >
            <span class="relative z-10 flex items-center justify-center">
              🇬🇧 English
            </span>
            <div class="absolute inset-0 bg-gradient-to-r from-white/0 via-white/20 to-white/0 transform -skew-x-12 -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
          </button>
        </div>
      </div>

      <!-- Footer -->
      <p class="text-white/60 text-sm mt-8">
        PROJET D'ÉTUDE • STUDY PROJECT
      </p>
    </div>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="absolute inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50">
      <div class="text-center">
        <div class="w-12 h-12 border-4 border-orange-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-white">Loading...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useLanguageStore } from '../stores/language'

const router = useRouter()
const languageStore = useLanguageStore()
const isLoading = ref(false)

const selectLanguage = async (lang) => {
  isLoading.value = true

  // Simuler un petit délai pour l'effet de chargement
  await new Promise(resolve => setTimeout(resolve, 800))

  languageStore.setLanguage(lang)
  localStorage.setItem('nowlight-language', lang)

  router.push('/home')
}
</script>