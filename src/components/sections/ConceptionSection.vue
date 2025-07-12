<template>
  <section id="conception" class="content-section conception-section">
    <div class="container">
      <h2>{{ t.conception.title }}</h2>
      <p class="section-description">{{ t.conception.description }}</p>

      <div class="conception-layout">
        <!-- Prototype Initial -->
        <div class="conception-subsection">
          <h3 class="subsection-title">{{ t.conception.prototypeInitialTitle }}</h3>
          <div class="modules-grid three-items">
            <!-- Module Électronique Initial -->
            <ModuleCard
              :module="getModule('initialElectric')"
              :eco-mode="ecoMode"
              @click="openModule('initialElectric')"
            />

            <!-- Video Tutorial -->
            <ModuleCard
              :module="getModule('initialVideo')"
              :eco-mode="ecoMode"
              :is-video="true"
            />

            <!-- Module Mécanique Initial -->
            <ModuleCard
              :module="getModule('initialMecanic')"
              :eco-mode="ecoMode"
              @click="openModule('initialMecanic')"
            />
          </div>
        </div>

        <!-- Prototype Final -->
        <div class="conception-subsection">
          <h3 class="subsection-title">{{ t.conception.prototypeFinalTitle }}</h3>
          <div class="modules-grid two-items">
            <!-- Module Électronique Final -->
            <ModuleCard
              :module="getModule('finalElectric')"
              :eco-mode="ecoMode"
              @click="openModule('finalElectric')"
            />

            <!-- Video Système -->
            <ModuleCard
              :module="getModule('generationSystem')"
              :eco-mode="ecoMode"
              :is-video="true"
            />
          </div>
        </div>

        <!-- Prototype Optimisé -->
        <div class="conception-subsection">
          <h3 class="subsection-title">{{ t.conception.prototypeOptimiseTitle }}</h3>
          <div class="modules-grid one-item">
            <!-- Module Mécanique Optimisé -->
            <ModuleCard
              :module="getModule('optimizedMecanic')"
              :eco-mode="ecoMode"
              @click="openModule('optimizedMecanic')"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Module Modal -->
    <ModuleModal
      v-if="selectedModule"
      :module="selectedModule"
      :eco-mode="ecoMode"
      @close="closeModule"
    />
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useLanguageStore } from '../../stores/language'
import ModuleCard from '../common/ModuleCard.vue'
import ModuleModal from '../modals/ModuleModal.vue'

const props = defineProps({
  ecoMode: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['open-module'])

const languageStore = useLanguageStore()
const t = computed(() => languageStore.t)

const selectedModule = ref(null)

const getModule = (moduleKey) => {
  return {
    key: moduleKey,
    ...t.value.modules[moduleKey]
  }
}

const openModule = (moduleKey) => {
  const module = getModule(moduleKey)
  selectedModule.value = module
  emit('open-module', module)
  document.body.style.overflow = 'hidden'
}

const closeModule = () => {
  selectedModule.value = null
  document.body.style.overflow = 'auto'
}
</script>

<style scoped>
.conception-section {
  background-color: var(--secondary-color);
}

.conception-section h2 {
  text-align: center;
  font-size: 2.2rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.conception-section h2::after {
  content: '';
  display: block;
  width: 70px;
  height: 4px;
  background-color: var(--accent-color);
  margin: 15px auto 25px;
}

.section-description {
  text-align: center;
  max-width: 700px;
  margin: 0 auto 60px auto;
  color: var(--text-light);
  font-size: 1.1rem;
  line-height: 1.6;
}

.conception-layout {
  margin-top: 40px;
}

.conception-subsection {
  margin-bottom: 80px;
}

.conception-subsection:last-child {
  margin-bottom: 0;
}

.subsection-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  font-weight: 600;
  color: var(--primary-color);
  position: relative;
}

.subsection-title::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  background-color: var(--accent-color);
  margin: 12px auto 0;
}

/* Grilles de modules */
.modules-grid {
  display: grid;
  gap: 40px;
  justify-content: center;
}

.modules-grid.three-items {
  grid-template-columns: repeat(3, minmax(300px, 350px));
  max-width: 1200px;
  margin: 0 auto;
}

.modules-grid.two-items {
  grid-template-columns: repeat(2, minmax(300px, 400px));
  max-width: 900px;
  margin: 0 auto;
}

.modules-grid.one-item {
  grid-template-columns: minmax(300px, 400px);
  justify-content: center;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .modules-grid.three-items {
    grid-template-columns: repeat(3, minmax(280px, 1fr));
    max-width: 1000px;
    gap: 30px;
  }
}

@media (max-width: 992px) {
  .modules-grid.three-items {
    grid-template-columns: repeat(2, minmax(280px, 1fr));
    max-width: 700px;
  }

  .modules-grid.two-items {
    grid-template-columns: repeat(2, minmax(280px, 1fr));
    max-width: 700px;
  }
}

@media (max-width: 768px) {
  .conception-subsection {
    margin-bottom: 60px;
  }

  .subsection-title {
    font-size: 1.8rem;
    margin-bottom: 40px;
  }

  .modules-grid.three-items,
  .modules-grid.two-items,
  .modules-grid.one-item {
    grid-template-columns: 1fr;
    max-width: 400px;
    gap: 25px;
  }

  .section-description {
    margin-bottom: 40px;
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .conception-section h2 {
    font-size: 1.8rem;
  }

  .subsection-title {
    font-size: 1.6rem;
  }

  .modules-grid {
    gap: 20px;
  }
}
</style>