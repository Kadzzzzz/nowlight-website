<template>
  <section id="hero" class="hero-section">
    <!-- Floating animated points (only in non-eco mode) -->
    <div v-if="!ecoMode" class="floating-elements">
      <div
        v-for="i in 6"
        :key="i"
        class="floating-point"
        :style="getRandomPosition(i)"
      ></div>
    </div>

    <!-- Hero content -->
    <div class="hero-content">
      <!-- Subtitle -->
      <div class="subtitle-container">
        <span class="subtitle">{{ t.hero.subtitle }}</span>
      </div>

      <!-- Main Title -->
      <h1 class="title">{{ t.hero.title }}</h1>

      <!-- Eco Mode Toggle (centered) -->
      <div class="eco-toggle-container">
        <div class="eco-toggle-wrapper">
          <button
            @click="toggleEcoMode"
            class="eco-toggle-btn"
            :class="ecoMode ? 'eco-active' : 'standard-active'"
          >
            <span class="toggle-option" :class="{ active: ecoMode }">
              <i class="fas fa-leaf"></i>
              {{ t.hero.ecoModeOff }}
            </span>
            <span class="toggle-option" :class="{ active: !ecoMode }">
              <i class="fas fa-sun"></i>
              {{ t.hero.ecoModeOn }}
            </span>
          </button>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="scroll-indicator">
      <span>{{ t.hero.scrollDown }}</span>
      <a href="#ambition" @click.prevent="scrollToSection" aria-label="Scroll down">
        <div class="arrow-down"></div>
      </a>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useLanguageStore } from '../../stores/language'

const languageStore = useLanguageStore()
const t = computed(() => languageStore.t)

const props = defineProps({
  ecoMode: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['toggle-eco-mode'])

const toggleEcoMode = () => {
  emit('toggle-eco-mode')
}

const scrollToSection = () => {
  const element = document.getElementById('ambition')
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

// Generate random positions for floating points
const getRandomPosition = (index) => {
  const positions = [
    { top: '20%', left: '10%', animationDelay: '0s' },
    { top: '60%', right: '15%', animationDelay: '2s' },
    { top: '80%', left: '20%', animationDelay: '4s' },
    { top: '30%', right: '30%', animationDelay: '1s' },
    { top: '70%', left: '60%', animationDelay: '3s' },
    { top: '40%', left: '80%', animationDelay: '5s' }
  ]

  return positions[index - 1] || {}
}
</script>

<style scoped>
.hero-section {
  height: 100vh;
  min-height: 600px;
  background-color: var(--primary-color);
  background-image: url('@/assets/images/hero-background.png');
  background-size: cover;
  background-position: center center;
  background-attachment: fixed;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--text-white);
  text-align: center;
  overflow: hidden;
}

.eco-mode .hero-section {
  background-image: none;
  background-color: #222;
  background-attachment: initial;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.5));
  z-index: 1;
}

.eco-mode .hero-section::before {
  background: none;
}

/* Floating animated elements */
.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

.floating-point {
  position: absolute;
  width: 8px;
  height: 8px;
  background-color: var(--accent-color);
  border-radius: 50%;
  opacity: 0.6;
  animation: float-and-glow 6s ease-in-out infinite;
  box-shadow: 0 0 10px var(--accent-color);
}

@keyframes float-and-glow {
  0%, 100% {
    transform: translateY(0px);
    opacity: 0.3;
    box-shadow: 0 0 5px var(--accent-color);
  }
  50% {
    transform: translateY(-20px);
    opacity: 0.8;
    box-shadow: 0 0 20px var(--accent-color);
  }
}

.hero-content {
  position: relative;
  z-index: 2;
  padding: 20px;
  max-width: 4xl;
  width: 100%;
}

/* Subtitle */
.subtitle-container {
  margin-bottom: 20px;
}

.subtitle {
  display: inline-block;
  padding: 8px 20px;
  background-color: rgba(255, 140, 0, 0.2);
  border: 1px solid rgba(255, 140, 0, 0.3);
  border-radius: 25px;
  color: rgba(255, 140, 0, 0.9);
  font-size: clamp(0.9rem, 2.5vw, 1.1rem);
  font-weight: 500;
  letter-spacing: 2px;
  text-transform: uppercase;
  backdrop-filter: blur(10px);
  opacity: 0;
  animation: fadeInUp 0.8s ease-out 0.5s forwards;
}

/* Main Title */
.title {
  font-size: clamp(3.5rem, 10vw, 6rem);
  letter-spacing: 5px;
  margin-bottom: 40px;
  opacity: 0;
  animation: fadeInUp 0.8s ease-out 0.7s forwards;
  font-weight: 800;
  color: white !important;
  background: linear-gradient(135deg, #ffffff 0%, #ffac4a 50%, #ff8c00 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none;
}

/* Eco Mode Toggle */
.eco-toggle-container {
  margin-bottom: 40px;
  opacity: 0;
  animation: fadeInUp 0.8s ease-out 0.9s forwards;
}

.eco-toggle-wrapper {
  display: inline-flex;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  border-radius: 50px;
  padding: 4px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.eco-toggle-btn {
  display: flex;
  background: none;
  border: none;
  cursor: pointer;
  border-radius: 50px;
  overflow: hidden;
  position: relative;
}

.toggle-option {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  font-size: 0.95rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease;
  border-radius: 50px;
  position: relative;
  z-index: 1;
}

.toggle-option.active {
  color: white;
  background-color: rgba(255, 140, 0, 0.8);
  box-shadow: 0 4px 15px rgba(255, 140, 0, 0.4);
  transform: translateY(-1px);
}

.toggle-option i {
  font-size: 0.9em;
}

/* Eco mode specific styles */
.eco-mode .subtitle,
.eco-mode .title,
.eco-mode .eco-toggle-container {
  animation: none;
  opacity: 1;
}

/* Scroll indicator */
.scroll-indicator {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
  opacity: 0;
  animation: fadeIn 1s ease-in-out 1.5s forwards;
  text-align: center;
}

.eco-mode .scroll-indicator {
  animation: none;
  opacity: 1;
}

.scroll-indicator span {
  display: block;
  font-size: 0.9rem;
  margin-bottom: 15px;
  color: white;
  font-weight: 500;
}

.arrow-down {
  width: 28px;
  height: 28px;
  border: 2px solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  margin: 0 auto;
  animation: bounce 2.5s infinite ease-in-out;
}

.eco-mode .arrow-down {
  animation: none;
}

.scroll-indicator a {
  color: inherit;
  text-decoration: none;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0) rotate(45deg);
  }
  40% {
    transform: translateY(-10px) rotate(45deg);
  }
  60% {
    transform: translateY(-5px) rotate(45deg);
  }
}

/* Mobile responsive */
@media (max-width: 768px) {
  .hero-content {
    padding: 20px;
  }

  .toggle-option {
    padding: 10px 20px;
    font-size: 0.9rem;
  }

  .subtitle {
    font-size: 0.8rem;
    padding: 6px 16px;
  }
}

@media (max-width: 480px) {
  .title {
    font-size: 2.5rem;
    letter-spacing: 3px;
  }

  .subtitle {
    font-size: 0.75rem;
    letter-spacing: 1px;
  }

  .toggle-option {
    padding: 8px 16px;
    font-size: 0.85rem;
    gap: 6px;
  }

  .eco-toggle-wrapper {
    padding: 3px;
  }
}

/* High contrast mode adjustments */
@media (prefers-contrast: high) {
  .title {
    -webkit-text-fill-color: white;
    background: none;
  }

  .subtitle {
    background-color: rgba(255, 140, 0, 0.4);
    border-color: rgba(255, 140, 0, 0.6);
    color: white;
  }
}
</style>