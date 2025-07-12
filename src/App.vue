<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useLanguageStore } from './stores/language'

const languageStore = useLanguageStore()

onMounted(() => {
  // Initialiser la langue depuis le localStorage
  const savedLang = localStorage.getItem('nowlight-language')
  if (savedLang) {
    languageStore.setLanguage(savedLang)
  } else {
    // Détecter la langue du navigateur
    const browserLang = navigator.language.split('-')[0]
    if (browserLang === 'fr' || browserLang === 'en') {
      languageStore.setLanguage(browserLang)
    }
  }
})
</script>

<style>
/* Styles globaux déjà dans style.css */
</style>