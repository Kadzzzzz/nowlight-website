<template>
  <!-- Header -->
  <header class="header" :class="{ 'header-scrolled': scrolled }">
    <div class="container header-container">
      <a href="#hero" @click.prevent="scrollToSection('hero')" class="logo">NOWLIGHT</a>

      <!-- Desktop Navigation -->
      <nav class="nav-links">
        <ul>
          <li><a href="#ambition" @click.prevent="scrollToSection('ambition')">{{ t.nav.ambition }}</a></li>
          <li><a href="#conception" @click.prevent="scrollToSection('conception')">{{ t.nav.conception }}</a></li>
          <li><a href="#engagements" @click.prevent="scrollToSection('engagements')">{{ t.nav.engagements }}</a></li>
          <li><a href="#contact" @click.prevent="scrollToSection('contact')">{{ t.nav.contact }}</a></li>
          <li class="language-dropdown">
            <button @click="toggleLanguageDropdown" class="language-btn">
              {{ currentLanguage.toUpperCase() }}
              <span class="dropdown-icon" :class="{ 'open': showLanguageDropdown }">▼</span>
            </button>
            <div v-if="showLanguageDropdown" class="dropdown-content">
              <a @click="selectLanguage('fr')">Français</a>
              <a @click="selectLanguage('en')">English</a>
            </div>
          </li>
        </ul>
      </nav>

      <!-- Mobile Menu Button -->
      <button @click="toggleMobileMenu" class="mobile-menu-btn" :class="{ 'active': mobileMenuOpen }" aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- Mobile Menu -->
  <div class="mobile-menu" :class="{ 'active': mobileMenuOpen }">
    <button @click="toggleMobileMenu" class="mobile-close-btn" aria-label="Close menu">×</button>
    <ul>
      <li><a href="#ambition" @click="scrollToSectionMobile('ambition')">{{ t.nav.ambition }}</a></li>
      <li><a href="#conception" @click="scrollToSectionMobile('conception')">{{ t.nav.conception }}</a></li>
      <li><a href="#engagements" @click="scrollToSectionMobile('engagements')">{{ t.nav.engagements }}</a></li>
      <li><a href="#contact" @click="scrollToSectionMobile('contact')">{{ t.nav.contact }}</a></li>
      <li class="mobile-language-selector">
        <button @click="selectLanguageMobile('fr')" :class="{ active: currentLanguage === 'fr' }">FR</button>
        <span>|</span>
        <button @click="selectLanguageMobile('en')" :class="{ active: currentLanguage === 'en' }">EN</button>
      </li>
    </ul>
  </div>

  <!-- Mobile Menu Overlay -->
  <div v-if="mobileMenuOpen" class="mobile-menu-overlay" @click="toggleMobileMenu"></div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useLanguageStore } from '../../stores/language'

const languageStore = useLanguageStore()
const t = computed(() => languageStore.t)
const currentLanguage = computed(() => languageStore.currentLanguage)

const scrolled = ref(false)
const showLanguageDropdown = ref(false)
const mobileMenuOpen = ref(false)

const handleScroll = () => {
  // Réduction du seuil pour que la navigation apparaisse plus tôt
  scrolled.value = window.scrollY > 50
}

const toggleLanguageDropdown = () => {
  showLanguageDropdown.value = !showLanguageDropdown.value
}

const selectLanguage = (lang) => {
  languageStore.setLanguage(lang)
  showLanguageDropdown.value = false

  // Émettre un événement global pour que les modales se mettent à jour
  window.dispatchEvent(new CustomEvent('language-changed', { detail: { language: lang } }))
}

const selectLanguageMobile = (lang) => {
  languageStore.setLanguage(lang)
  mobileMenuOpen.value = false

  // Émettre un événement global pour que les modales se mettent à jour
  window.dispatchEvent(new CustomEvent('language-changed', { detail: { language: lang } }))
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
  document.body.classList.toggle('no-scroll', mobileMenuOpen.value)
}

const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId)
  if (element) {
    const headerOffset = scrolled.value ? 70 : 0
    const elementPosition = element.getBoundingClientRect().top
    const offsetPosition = elementPosition + window.pageYOffset - headerOffset
    window.scrollTo({ top: offsetPosition, behavior: 'smooth' })
  }
  showLanguageDropdown.value = false
}

const scrollToSectionMobile = (sectionId) => {
  scrollToSection(sectionId)
  setTimeout(() => { mobileMenuOpen.value = false }, 150)
}

const handleClickOutside = (event) => {
  const dropdown = document.querySelector('.language-dropdown')
  if (dropdown && !dropdown.contains(event.target)) {
    showLanguageDropdown.value = false
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  document.addEventListener('click', handleClickOutside)
  handleScroll() // Vérifier l'état initial
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.removeEventListener('click', handleClickOutside)
  document.body.classList.remove('no-scroll')
})
</script>

<style scoped>
:root {
  --primary-color: #0a0a0a;
  --secondary-color: #f8f8f8;
  --accent-color: #FF8C00;
  --text-color: #333;
  --text-light: #666;
  --text-white: #ffffff;
  --border-color: #ddd;
  --transition-speed: 0.3s;
  --header-height: 70px;
}

/* Header Styles */
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  height: var(--header-height);
  background-color: transparent;
  transition: all var(--transition-speed) ease;
  /* Changement important : commencer visible avec transform: translateY(0) */
  transform: translateY(0);
  display: flex;
  align-items: center;
  opacity: 0;
  pointer-events: none;
}

.header-scrolled {
  background-color: rgba(10, 10, 10, 0.95);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  opacity: 1;
  pointer-events: all;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 25px;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--text-white);
  text-decoration: none;
  transition: color var(--transition-speed);
}

.logo:hover {
  color: var(--accent-color);
}

/* Desktop Navigation */
.nav-links ul {
  display: flex;
  list-style: none;
  gap: 35px;
  margin: 0;
  padding: 0;
}

.nav-links a {
  color: var(--text-white);
  font-weight: 500;
  position: relative;
  padding-bottom: 5px;
  text-decoration: none;
  transition: color var(--transition-speed);
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--accent-color);
  transition: width var(--transition-speed);
}

.nav-links a:hover::after,
.nav-links a.active::after {
  width: 100%;
}

.nav-links a:hover {
  color: var(--accent-color);
}

/* Language Dropdown */
.language-dropdown {
  position: relative;
}

.language-btn {
  color: var(--text-white);
  display: flex;
  align-items: center;
  gap: 5px;
  font-weight: 500;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  cursor: pointer;
  transition: all var(--transition-speed);
  backdrop-filter: blur(10px);
}

.language-btn:hover {
  background: rgba(255, 140, 0, 0.2);
  border-color: rgba(255, 140, 0, 0.4);
}

.dropdown-icon {
  font-size: 0.8rem;
  transition: transform var(--transition-speed);
  display: inline-block;
}

.dropdown-icon.open {
  transform: rotate(180deg);
}

.dropdown-content {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  background-color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  min-width: 120px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  border-radius: 8px;
  overflow: hidden;
  z-index: 1001;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.dropdown-content a {
  color: var(--text-color);
  padding: 12px 18px;
  display: block;
  text-align: left;
  font-size: 0.95rem;
  cursor: pointer;
  transition: background-color var(--transition-speed), color var(--transition-speed);
}

.dropdown-content a:hover {
  background-color: rgba(255, 140, 0, 0.1);
  color: var(--accent-color);
}

/* Mobile Menu Button */
.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 4px;
  padding: 8px;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 1001;
}

.mobile-menu-btn span {
  width: 25px;
  height: 3px;
  background-color: var(--text-white);
  transition: all var(--transition-speed);
  transform-origin: center;
}

.mobile-menu-btn.active span:nth-child(1) {
  transform: rotate(45deg) translate(6px, 6px);
}

.mobile-menu-btn.active span:nth-child(2) {
  opacity: 0;
}

.mobile-menu-btn.active span:nth-child(3) {
  transform: rotate(-45deg) translate(6px, -6px);
}

/* Mobile Menu */
.mobile-menu {
  position: fixed;
  top: 0;
  right: -100%;
  width: 280px;
  height: 100vh;
  background-color: rgba(10, 10, 10, 0.95);
  backdrop-filter: blur(10px);
  z-index: 1000;
  transition: right var(--transition-speed);
  display: flex;
  flex-direction: column;
  padding: 80px 30px 30px;
}

.mobile-menu.active {
  right: 0;
}

.mobile-close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 2rem;
  color: var(--text-white);
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
  line-height: 1;
}

.mobile-menu ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 25px;
  margin: 0;
  padding: 0;
}

.mobile-menu a {
  color: var(--text-white);
  font-size: 1.2rem;
  font-weight: 500;
  text-decoration: none;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: color var(--transition-speed);
}

.mobile-menu a:hover {
  color: var(--accent-color);
}

.mobile-language-selector {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.mobile-language-selector button {
  color: rgba(255, 255, 255, 0.6);
  font-size: 1.1rem;
  font-weight: 500;
  padding: 8px 16px;
  background: none;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  cursor: pointer;
  transition: all var(--transition-speed);
}

.mobile-language-selector button.active {
  color: var(--text-white);
  background-color: var(--accent-color);
  border-color: var(--accent-color);
}

.mobile-language-selector span {
  color: rgba(255, 255, 255, 0.3);
}

.mobile-menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .nav-links {
    display: none;
  }

  .mobile-menu-btn {
    display: flex;
  }
}

@media (max-width: 480px) {
  .mobile-menu {
    width: 100%;
  }

  .container {
    padding: 0 20px;
  }
}
</style>