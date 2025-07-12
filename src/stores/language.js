import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// Import des traductions (ces fichiers doivent être copiés depuis vos documents)
import frTranslations from '../locales/fr.json'
import enTranslations from '../locales/en.json'

export const useLanguageStore = defineStore('language', () => {
  const currentLanguage = ref('fr')

  const translations = {
    fr: frTranslations,
    en: enTranslations
  }

  const t = computed(() => {
    return translations[currentLanguage.value] || translations.fr
  })

  const setLanguage = (lang) => {
    if (translations[lang]) {
      currentLanguage.value = lang
      localStorage.setItem('nowlight-language', lang)

      // Mettre à jour la langue du document
      document.documentElement.lang = lang
    }
  }

  const getCurrentLanguage = computed(() => currentLanguage.value)

  const getAvailableLanguages = () => {
    return Object.keys(translations)
  }

  const getLanguageFlag = (lang) => {
    const flags = {
      fr: '🇫🇷',
      en: '🇬🇧'
    }
    return flags[lang] || '🌐'
  }

  const getLanguageName = (lang) => {
    const names = {
      fr: 'Français',
      en: 'English'
    }
    return names[lang] || lang.toUpperCase()
  }

  return {
    currentLanguage: getCurrentLanguage,
    t,
    setLanguage,
    getAvailableLanguages,
    getLanguageFlag,
    getLanguageName
  }
})