<template>
  <section id="engagements" class="py-20 bg-gradient-to-br from-gray-900 via-black to-gray-800 text-white">
    <div class="container mx-auto px-6">
      <div class="max-w-6xl mx-auto">
        <!-- Section Header -->
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold mb-6 text-white drop-shadow-lg">
            {{ t.engagements.title }}
          </h2>
          <div class="w-20 h-1 bg-gradient-to-r from-orange-500 to-orange-600 mx-auto rounded-full"></div>
        </div>

        <!-- Engagements Grid -->
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Engagement 1 -->
          <div class="group text-center" data-aos="fade-up" data-aos-delay="100">
            <div class="relative mb-8">
              <!-- Icon Container -->
              <div class="w-20 h-20 bg-gradient-to-br from-orange-500 to-orange-600 rounded-full flex items-center justify-center mx-auto shadow-2xl group-hover:scale-110 transition-transform duration-300">
                <svg class="w-14 h-14 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <circle cx="8" cy="8" r="3.5"/>
                  <circle cx="16" cy="8" r="3.5"/>
                  <circle cx="12" cy="10" r="3"/>
                  <path d="M8 13c-3.5 0-7 1.5-7 5v2h14v-2c0-3.5-3.5-5-7-5z"/>
                  <path d="M16 13c-3.5 0-7 1.5-7 5v2h14v-2c0-3.5-3.5-5-7-5z"/>
                  <path d="M12 15c-3 0-6 1-6 3.5v1.5h12v-1.5c0-2.5-3-3.5-6-3.5z"/>
                </svg>
              </div>

              <!-- Decorative Elements -->
              <div class="absolute -top-2 -right-2 w-4 h-4 bg-blue-400 rounded-full opacity-60 group-hover:animate-ping"></div>
              <div class="absolute -bottom-2 -left-2 w-3 h-3 bg-green-400 rounded-full opacity-60 group-hover:animate-ping" style="animation-delay: 0.5s;"></div>
            </div>

            <h3 class="text-xl font-bold mb-4 text-orange-400 group-hover:text-orange-300 transition-colors duration-300">
              {{ t.engagements.item1.title }}
            </h3>
            <p class="text-gray-300 leading-relaxed group-hover:text-gray-200 transition-colors duration-300">
              {{ t.engagements.item1.description }}
            </p>
          </div>

          <!-- Engagement 2 -->
          <div class="group text-center" data-aos="fade-up" data-aos-delay="200">
            <div class="relative mb-8">
              <!-- Icon Container -->
              <div class="w-20 h-20 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center mx-auto shadow-2xl group-hover:scale-110 transition-transform duration-300">
                <svg class="w-10 h-10 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M17,8C8,10 5.9,16.17 3.82,21.34L5.71,22L6.66,19.7C7.14,19.87 7.64,20 8,20C19,20 22,3 22,3C21,5 14,5.25 9,6.25C4,7.25 2,11.5 2,13.5C2,15.5 3.75,17.25 3.75,17.25C7,8 17,8 17,8Z"/>
                </svg>
              </div>

              <!-- Decorative Elements -->
              <div class="absolute -top-2 -right-2 w-4 h-4 bg-orange-400 rounded-full opacity-60 group-hover:animate-ping"></div>
              <div class="absolute -bottom-2 -left-2 w-3 h-3 bg-blue-400 rounded-full opacity-60 group-hover:animate-ping" style="animation-delay: 0.5s;"></div>
            </div>

            <h3 class="text-xl font-bold mb-4 text-green-400 group-hover:text-green-300 transition-colors duration-300">
              {{ t.engagements.item2.title }}
            </h3>
            <p class="text-gray-300 leading-relaxed group-hover:text-gray-200 transition-colors duration-300">
              {{ t.engagements.item2.description }}
            </p>
          </div>

          <!-- Engagement 3 -->
          <div class="group text-center" data-aos="fade-up" data-aos-delay="300">
            <div class="relative mb-8">
              <!-- Icon Container -->
              <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-blue-600 rounded-full flex items-center justify-center mx-auto shadow-2xl group-hover:scale-110 transition-transform duration-300">
                <svg class="w-10 h-10 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12,2A3,3 0 0,1 15,5V11A3,3 0 0,1 12,14A3,3 0 0,1 9,11V5A3,3 0 0,1 12,2M19,11C19,14.53 16.39,17.44 13,17.93V21H11V17.93C7.61,17.44 5,14.53 5,11H7A5,5 0 0,0 12,16A5,5 0 0,0 17,11H19Z"/>
                </svg>
              </div>

              <!-- Decorative Elements -->
              <div class="absolute -top-2 -right-2 w-4 h-4 bg-green-400 rounded-full opacity-60 group-hover:animate-ping"></div>
              <div class="absolute -bottom-2 -left-2 w-3 h-3 bg-orange-400 rounded-full opacity-60 group-hover:animate-ping" style="animation-delay: 0.5s;"></div>
            </div>

            <h3 class="text-xl font-bold mb-4 text-blue-400 group-hover:text-blue-300 transition-colors duration-300">
              {{ t.engagements.item3.title }}
            </h3>
            <p class="text-gray-300 leading-relaxed group-hover:text-gray-200 transition-colors duration-300">
              {{ t.engagements.item3.description }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Background Effects -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-1/4 left-1/4 w-64 h-64 bg-orange-500/10 rounded-full filter blur-3xl"></div>
      <div class="absolute bottom-1/4 right-1/4 w-80 h-80 bg-blue-500/10 rounded-full filter blur-3xl"></div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useLanguageStore } from '../../stores/language'

const languageStore = useLanguageStore()
const t = computed(() => languageStore.t)
</script>