<template>
  <div class="app" :class="{ 'eco-mode': ecoMode }">
    <!-- Navigation -->
    <Navigation />

    <main>
      <!-- Hero Section -->
      <HeroSection :eco-mode="ecoMode" @toggle-eco-mode="toggleEcoMode" />

      <!-- Ambition Section -->
      <AmbitionSection :eco-mode="ecoMode" />

      <!-- Conception Section -->
      <ConceptionSection :eco-mode="ecoMode" @open-module="openModule" />

      <!-- Engagements Section -->
      <EngagementsSection :eco-mode="ecoMode" />

      <!-- Contact Section -->
      <ContactSection :eco-mode="ecoMode" />
    </main>

    <!-- Footer -->
    <Footer />

    <!-- Module Modal -->
    <Teleport to="body">
      <ModuleModal
        v-if="selectedModule"
        :module="selectedModule"
        :eco-mode="ecoMode"
        @close="closeModule"
      />
    </Teleport>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>Chargement...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import Navigation from '../components/common/Navigation.vue'
import HeroSection from '../components/sections/HeroSection.vue'
import AmbitionSection from '../components/sections/AmbitionSection.vue'
import ConceptionSection from '../components/sections/ConceptionSection.vue'
import EngagementsSection from '../components/sections/EngagementsSection.vue'
import ContactSection from '../components/sections/ContactSection.vue'
import Footer from '../components/common/Footer.vue'
import ModuleModal from '../components/modals/ModuleModal.vue'

const selectedModule = ref(null)
const isLoading = ref(true)
const ecoMode = ref(false)

const toggleEcoMode = () => {
  ecoMode.value = !ecoMode.value
  localStorage.setItem('nowlight-ecoMode', ecoMode.value.toString())
}

const openModule = (module) => {
  selectedModule.value = module
  document.body.style.overflow = 'hidden'
}

const closeModule = () => {
  selectedModule.value = null
  document.body.style.overflow = 'auto'
}

onMounted(() => {
  // Charger les préférences
  const savedEcoMode = localStorage.getItem('nowlight-ecoMode')
  if (savedEcoMode === 'true') {
    ecoMode.value = true
  }

  // Simuler un chargement initial
  setTimeout(() => {
    isLoading.value = false
  }, 1000)
})
</script>

<style>
/* Variables CSS globales */
:root {
  --primary-color: #0a0a0a;
  --secondary-color: #f8f8f8;
  --accent-color: #FF8C00;
  --text-color: #333;
  --text-light: #666;
  --text-white: #ffffff;
  --border-color: #ddd;
  --heading-font: 'Poppins', sans-serif;
  --body-font: 'Lato', sans-serif;
  --transition-speed: 0.3s;
  --box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  --header-height: 70px;
}

/* Reset et styles de base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  font-family: var(--body-font);
  line-height: 1.7;
  color: var(--text-color);
  background-color: var(--secondary-color);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body.no-scroll {
  overflow: hidden;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 25px;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--heading-font);
  font-weight: 700;
  line-height: 1.3;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

h2 {
  font-size: 2.2rem;
}

h3 {
  font-size: 1.5rem;
}

p {
  margin-bottom: 1.2rem;
  color: var(--text-light);
}

a {
  text-decoration: none;
  color: var(--accent-color);
  transition: color var(--transition-speed);
}

a:hover {
  color: darkorange;
}

button {
  cursor: pointer;
  border: none;
  outline: none;
  background: none;
  font-family: inherit;
  transition: background-color var(--transition-speed), color var(--transition-speed), transform var(--transition-speed);
}

img, iframe {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Utility Classes */
.content-section {
  padding: 80px 0;
  border-bottom: 1px solid var(--border-color);
}

.content-section:last-of-type {
  border-bottom: none;
}

.section-content {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.layout-split {
  display: grid;
  grid-template-columns: 1fr;
  gap: 50px;
  align-items: center;
}

.layout-split.reverse .text-content {
  order: 2;
}

.layout-split.reverse .media-content {
  order: 1;
}

@media (min-width: 768px) {
  .layout-split {
    grid-template-columns: 1fr 1fr;
  }

  .layout-split.reverse .text-content {
    order: initial;
  }

  .layout-split.reverse .media-content {
    order: initial;
  }
}

.text-content h2::after {
  content: '';
  display: block;
  width: 70px;
  height: 4px;
  background-color: var(--accent-color);
  margin-top: 15px;
  margin-bottom: 25px;
}

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: var(--primary-color);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
  animation: fadeOut 0.5s ease-out 1s forwards;
}

.loading-content {
  text-align: center;
  color: var(--text-white);
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid var(--accent-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes fadeOut {
  to {
    opacity: 0;
    visibility: hidden;
  }
}

/* Eco Mode Styles */
.eco-mode {
  filter: grayscale(30%);
}

.eco-mode * {
  animation-duration: 0s !important;
  animation-delay: 0s !important;
  transition-duration: 0.1s !important;
}

.eco-mode .hero-section {
  background-attachment: initial !important;
}

.eco-mode .floating-elements {
  display: none;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 0 20px;
  }

  .content-section {
    padding: 60px 0;
  }

  h2 {
    font-size: 1.8rem;
  }

  .layout-split {
    gap: 30px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 15px;
  }

  .content-section {
    padding: 40px 0;
  }

  h2 {
    font-size: 1.6rem;
  }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  .hero-section {
    background-attachment: initial;
  }
}

/* Focus Styles */
button:focus,
a:focus,
input:focus,
textarea:focus {
  outline: 2px solid var(--accent-color);
  outline-offset: 2px;
}

/* High Contrast Mode */
@media (prefers-contrast: high) {
  :root {
    --text-color: #000;
    --text-light: #333;
    --border-color: #000;
    --accent-color: #0066cc;
  }
}

/* Print Styles */
@media print {
  .loading-overlay,
  .floating-elements {
    display: none;
  }

  .hero-section {
    background-image: none;
    background-color: white;
    color: black;
    height: auto;
    padding: 40px 0;
  }

  .hero-section::before {
    display: none;
  }

  .content-section {
    padding: 20px 0;
  }
}
</style>