<template>
  <section id="ambition" class="py-20 bg-white">
    <div class="container mx-auto px-6">
      <div class="max-w-6xl mx-auto">
        <!-- Section Header -->
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-800 mb-6">
            {{ t.ambition.title }}
          </h2>
          <div class="w-20 h-1 bg-gradient-to-r from-orange-500 to-orange-600 mx-auto rounded-full"></div>
        </div>

        <!-- Content Grid -->
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <!-- Text Content -->
          <div class="space-y-8">
            <div class="group" :data-aos="!ecoMode ? 'fade-up' : ''" data-aos-delay="100">
              <div class="flex items-start space-x-4">
                <div class="flex-shrink-0 w-8 h-8 bg-orange-100 rounded-full flex items-center justify-center mt-1">
                  <div class="w-3 h-3 bg-orange-500 rounded-full"></div>
                </div>
                <p class="text-lg text-gray-700 leading-relaxed group-hover:text-gray-900 transition-colors duration-300">
                  {{ t.ambition.paragraph1 }}
                </p>
              </div>
            </div>

            <div class="group" :data-aos="!ecoMode ? 'fade-up' : ''" data-aos-delay="200">
              <div class="flex items-start space-x-4">
                <div class="flex-shrink-0 w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mt-1">
                  <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
                </div>
                <p class="text-lg text-gray-700 leading-relaxed group-hover:text-gray-900 transition-colors duration-300">
                  {{ t.ambition.paragraph2 }}
                </p>
              </div>
            </div>

            <div class="group" :data-aos="!ecoMode ? 'fade-up' : ''" data-aos-delay="300">
              <div class="flex items-start space-x-4">
                <div class="flex-shrink-0 w-8 h-8 bg-green-100 rounded-full flex items-center justify-center mt-1">
                  <div class="w-3 h-3 bg-green-500 rounded-full"></div>
                </div>
                <p class="text-lg text-gray-700 leading-relaxed group-hover:text-gray-900 transition-colors duration-300">
                  {{ t.ambition.paragraph3 }}
                </p>
              </div>
            </div>
          </div>

          <!-- Image or Eco Placeholder -->
          <div class="relative" :data-aos="!ecoMode ? 'fade-left' : ''" data-aos-delay="400">
            <!-- Image (only shown when NOT in eco mode) -->
            <div v-if="!ecoMode" class="relative rounded-2xl shadow-xl overflow-hidden">
              <img
                src="../../assets/images/ambition-image.jpg"
                alt="NowLight - Innovation durable"
                class="w-full h-auto object-cover transition-transform duration-300 hover:scale-105"
              />

              <!-- Floating Elements (only in non-eco mode) -->
              <div class="absolute -top-4 -right-4 w-8 h-8 bg-orange-400 rounded-full opacity-60 animate-bounce"></div>
              <div class="absolute -bottom-4 -left-4 w-6 h-6 bg-blue-400 rounded-full opacity-60 animate-bounce"
                   style="animation-delay: 1s;"></div>
            </div>

            <!-- Eco Mode Placeholder -->
            <div v-else class="eco-placeholder-media">
              <div class="flex flex-col items-center justify-center text-center p-8">
                <div class="w-16 h-16 bg-gray-300 rounded-full flex items-center justify-center mb-4">
                  <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                  </svg>
                </div>
                <p class="text-gray-600 font-medium">{{ t.ambition.title }}</p>
                <p class="text-sm text-gray-500 italic mt-2">Image désactivée en mode éco</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import {computed} from 'vue'
import {useLanguageStore} from '../../stores/language'

// Ajout de la prop ecoMode
const props = defineProps({
  ecoMode: {
    type: Boolean,
    default: false
  }
})

const languageStore = useLanguageStore()
const t = computed(() => languageStore.t)
</script>

<style scoped>
.eco-placeholder-media {
  border: 2px dashed #d1d5db;
  border-radius: 1rem;
  background-color: #f9fafb;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Désactivation des animations en mode éco */
.eco-mode .animate-bounce {
  animation: none;
}

.eco-mode .transition-transform {
  transition: none;
}

.eco-mode .hover\:scale-105:hover {
  transform: none;
}
</style>