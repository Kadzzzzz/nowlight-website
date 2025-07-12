<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center p-4" @click="closeModal">
    <!-- Backdrop -->
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>

    <!-- Modal -->
    <div
      class="relative bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden"
      @click.stop
    >
      <!-- Header -->
      <div class="flex items-center justify-between p-6 border-b border-gray-200 bg-gradient-to-r from-orange-50 to-orange-100">
        <h2 class="text-2xl font-bold text-gray-800">{{ module.title }}</h2>
        <button
          @click="closeModal"
          class="w-10 h-10 bg-white rounded-full flex items-center justify-center hover:bg-gray-50 transition-colors duration-200 shadow-sm"
        >
          <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>

      <!-- Content -->
      <div class="overflow-y-auto max-h-[calc(90vh-80px)]">
        <!-- Video Content -->
        <div v-if="isVideo" class="p-6">
          <div class="aspect-video bg-black rounded-lg overflow-hidden">
            <iframe
              v-if="module.videoId"
              :src="getYoutubeEmbedUrl(module.videoId)"
              class="w-full h-full"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            ></iframe>
            <div v-else class="w-full h-full flex items-center justify-center text-white">
              <div class="text-center">
                <svg class="w-16 h-16 mx-auto mb-4 opacity-50" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M8 5v14l11-7z"/>
                </svg>
                <p>Vidéo non disponible</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Module Content -->
        <div v-else class="p-6">
          <!-- Images Gallery -->
          <div v-if="module.images && module.images.length > 0" class="mb-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div
                v-for="(image, index) in module.images"
                :key="index"
                class="relative group cursor-pointer"
                @click="openImageViewer(index)"
              >
                <img
                  :src="`/src/assets/images/${image}`"
                  :alt="`${module.title} - Image ${index + 1}`"
                  class="w-full h-48 object-cover rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300"
                  @error="handleImageError"
                >
                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 rounded-lg flex items-center justify-center">
                  <svg class="w-8 h-8 text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- Description -->
          <div v-if="module.description" class="prose prose-lg max-w-none">
            <div v-html="formatDescription(module.description)"></div>
          </div>

          <!-- Placeholder si pas de contenu -->
          <div v-else class="text-center py-12">
            <div class="w-16 h-16 bg-gray-200 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
              </svg>
            </div>
            <p class="text-gray-500">Contenu en cours de développement</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Image Viewer -->
    <div v-if="selectedImageIndex !== null" class="absolute inset-0 bg-black/90 flex items-center justify-center z-10" @click="closeImageViewer">
      <div class="relative max-w-5xl max-h-full p-4">
        <img
          :src="`/src/assets/images/${module.images[selectedImageIndex]}`"
          :alt="`${module.title} - Image ${selectedImageIndex + 1}`"
          class="max-w-full max-h-full object-contain"
          @click.stop
        >

        <!-- Navigation -->
        <div v-if="module.images.length > 1" class="absolute inset-y-0 left-0 flex items-center">
          <button
            @click.stop="previousImage"
            class="w-12 h-12 bg-white/20 hover:bg-white/30 rounded-full flex items-center justify-center ml-4 transition-colors duration-200"
          >
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
            </svg>
          </button>
        </div>

        <div v-if="module.images.length > 1" class="absolute inset-y-0 right-0 flex items-center">
          <button
            @click.stop="nextImage"
            class="w-12 h-12 bg-white/20 hover:bg-white/30 rounded-full flex items-center justify-center mr-4 transition-colors duration-200"
          >
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
            </svg>
          </button>
        </div>

        <!-- Close button -->
        <button
          @click="closeImageViewer"
          class="absolute top-4 right-4 w-10 h-10 bg-white/20 hover:bg-white/30 rounded-full flex items-center justify-center transition-colors duration-200"
        >
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  module: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['close'])

const selectedImageIndex = ref(null)

const isVideo = computed(() => props.module.type === 'video')

const closeModal = () => {
  emit('close')
}

const getYoutubeEmbedUrl = (videoId) => {
  // Nettoyer l'ID de la vidéo (enlever les paramètres si présents)
  const cleanId = videoId.split('?')[0]
  return `https://www.youtube.com/embed/${cleanId}?autoplay=1&rel=0`
}

const formatDescription = (description) => {
  if (!description) return ''

  return description
      // Convertir les titres markdown
      .replace(/### (.*)/g, '<h3 class="text-xl font-bold mt-6 mb-3 text-gray-800">$1</h3>')
      .replace(/## (.*)/g, '<h2 class="text-2xl font-bold mt-8 mb-4 text-gray-800">$1</h2>')
      // Convertir le texte en gras
      .replace(/\*\*(.*?)\*\*/g, '<strong class="font-semibold text-gray-900">$1</strong>')
      // Convertir l'italique
      .replace(/\*(.*?)\*/g, '<em class="italic">$1</em>')
      // Convertir les listes
      .replace(/^• (.*$)/gim, '<li class="ml-4 mb-2">$1</li>')
      // Convertir les références d'images [Img:X, Txt:"Y"]
      .replace(/\[Img:(\d+), Txt:"([^"]+)"\]/g, '<span class="text-orange-600 font-medium">($2)</span>')
      // Convertir les liens
      .replace(/\*\*\*(.*?)\*\*\*/g, '<a href="$1" target="_blank" class="text-blue-600 hover:text-blue-800 underline">$1</a>')
      // Convertir les retours à la ligne
      .replace(/\n\n/g, '</p><p class="mb-4">')
      .replace(/\n/g, '<br>')
      // Envelopper dans des paragraphes
      .replace(/^(.+)/, '<p class="mb-4">$1')
      .replace(/(.+)$/, '$1</p>')
}

const openImageViewer = (index) => {
  selectedImageIndex.value = index
}

const closeImageViewer = () => {
  selectedImageIndex.value = null
}

const previousImage = () => {
  if (selectedImageIndex.value > 0) {
    selectedImageIndex.value--
  } else {
    selectedImageIndex.value = props.module.images.length - 1
  }
}

const nextImage = () => {
  if (selectedImageIndex.value < props.module.images.length - 1) {
    selectedImageIndex.value++
  } else {
    selectedImageIndex.value = 0
  }
}

const handleImageError = (event) => {
  // En cas d'erreur de chargement d'image, masquer l'élément
  event.target.style.display = 'none'
}

// Gestion des touches clavier
const handleKeydown = (event) => {
  if (selectedImageIndex.value !== null) {
    if (event.key === 'Escape') {
      closeImageViewer()
    } else if (event.key === 'ArrowLeft') {
      previousImage()
    } else if (event.key === 'ArrowRight') {
      nextImage()
    }
  } else if (event.key === 'Escape') {
    closeModal()
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.prose {
  max-width: none;
}

.prose h2 {
  border-bottom: 2px solid #f97316;
  padding-bottom: 0.5rem;
}

.prose h3 {
  color: #f97316;
}

.prose ul {
  list-style: none;
  padding-left: 0;
}

.prose li {
  position: relative;
  padding-left: 1.5rem;
}

.prose li::before {
  content: '•';
  color: #f97316;
  font-weight: bold;
  position: absolute;
  left: 0;
}
</style>