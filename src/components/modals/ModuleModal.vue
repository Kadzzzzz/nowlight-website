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
          <!-- Images Gallery - Design amélioré -->
          <div v-if="module.images && module.images.length > 0" class="mb-8">
            <!-- Mode normal : afficher les images avec numérotation -->
            <div v-if="!ecoMode" class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div
                v-for="(image, index) in module.images"
                :key="index"
                class="relative group cursor-pointer bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100"
                @click="openImageViewer(index)"
              >
                <img
                  :src="`/src/assets/images/${image}`"
                  :alt="`${module.title} - Image ${index + 1}`"
                  class="w-full h-48 object-cover"
                  @error="handleImageError"
                >
                <!-- Numérotation de l'image en bas à droite -->
                <div class="absolute bottom-3 right-3 bg-black/70 text-white text-sm font-medium px-2 py-1 rounded shadow-lg">
                  {{ index + 1 }}
                </div>
                <!-- Overlay au hover -->
                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
                  <svg class="w-10 h-10 text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Mode éco : placeholder pour les images -->
            <div v-else class="eco-images-placeholder">
              <div class="flex flex-col items-center justify-center text-center p-8 border-2 border-dashed border-gray-300 rounded-lg bg-gray-50">
                <div class="w-16 h-16 bg-gray-300 rounded-full flex items-center justify-center mb-4">
                  <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 002 2v12a2 2 0 002 2z"></path>
                  </svg>
                </div>
                <p class="text-gray-600 font-medium">{{ module.images.length }} image(s) disponible(s)</p>
                <p class="text-sm text-gray-500 italic mt-2">Images désactivées en mode éco</p>
              </div>
            </div>
          </div>

          <!-- Description avec design amélioré -->
          <div v-if="module.description" class="prose-custom max-w-none">
            <div v-html="formatDescription(module.description)" @click="handleDescriptionClick"></div>
          </div>

          <!-- Placeholder si pas de contenu -->
          <div v-if="!module.description && (!module.images || module.images.length === 0)" class="text-center py-12">
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

    <!-- Image Viewer - TAILLE CORRIGÉE ET FERMETURE AMÉLIORÉE -->
    <div v-if="selectedImageIndex !== null" class="absolute inset-0 bg-black/90 flex items-center justify-center z-10" @click.stop="closeImageViewer">
      <div class="relative w-full h-full p-8 flex items-center justify-center">
        <img
          :src="`/src/assets/images/${module.images[selectedImageIndex]}`"
          :alt="`${module.title} - Image ${selectedImageIndex + 1}`"
          class="max-w-[90%] max-h-[90%] object-contain"
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
          @click.stop="closeImageViewer"
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
  },
  ecoMode: {
    type: Boolean,
    default: false
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
      // Convertir les listes - SANS points
      .replace(/^• (.*$)/gim, '<div class="list-item-no-bullet">$1</div>')
      // Convertir les références d'images CLIQUABLES
      .replace(/\[Img:(\d+), Txt:"([^"]+)"\]/g, '<span class="image-reference" data-image-index="$1" style="color: #f97316; font-weight: 600; cursor: pointer; text-decoration: underline;">($2)</span>')
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

// NOUVELLE FONCTION pour gérer les clics sur les références d'images
const handleDescriptionClick = (event) => {
  if (event.target.classList.contains('image-reference')) {
    const imageIndex = parseInt(event.target.getAttribute('data-image-index')) - 1 // -1 car les indices commencent à 1 dans le texte
    if (imageIndex >= 0 && imageIndex < props.module.images.length) {
      openImageViewer(imageIndex)
    }
  }
}

// Gestion des touches clavier - CORRIGÉE
const handleKeydown = (event) => {
  if (selectedImageIndex.value !== null) {
    if (event.key === 'Escape') {
      closeImageViewer() // Ferme seulement le viewer d'image
    } else if (event.key === 'ArrowLeft') {
      previousImage()
    } else if (event.key === 'ArrowRight') {
      nextImage()
    }
  } else if (event.key === 'Escape') {
    closeModal() // Ferme la modale seulement si pas dans le viewer
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
/* Styles personnalisés pour le contenu des modules */
.prose-custom {
  line-height: 1.7;
  color: #374151;
}

/* Titres avec traits de séparation orange */
.prose-custom :deep(h2) {
  color: #1f2937;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 2rem 0 1.5rem 0;
  padding-bottom: 0.75rem;
  border-bottom: 3px solid #f97316;
  position: relative;
}

.prose-custom :deep(h2::after) {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #f97316, #fb923c);
}

.prose-custom :deep(h3) {
  color: #f97316;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 1.5rem 0 1rem 0;
}

/* Paragraphes */
.prose-custom :deep(p) {
  margin-bottom: 1.25rem;
  text-align: justify;
}

/* Style pour les éléments de liste personnalisés */
.prose-custom :deep(.list-item) {
  position: relative;
  padding-left: 1.5rem;
  margin-bottom: 0.75rem;
  line-height: 1.6;
  color: #374151;
}

.prose-custom :deep(.list-item::before) {
  content: '•';
  color: #f97316;
  font-weight: normal;
  position: absolute;
  left: 0;
  font-size: 0.9em;
  top: 0.1em;
}

/* Listes standards (au cas où) */
.prose-custom :deep(ul) {
  list-style: none;
  margin: 1.5rem 0;
  padding-left: 0;
}

.prose-custom :deep(li) {
  position: relative;
  padding-left: 1.5rem;
  margin-bottom: 0.75rem;
  line-height: 1.6;
}

.prose-custom :deep(li::before) {
  content: '•';
  color: #f97316;
  font-weight: normal;
  position: absolute;
  left: 0;
  font-size: 0.9em;
  top: 0.1em;
}

/* Texte en gras */
.prose-custom :deep(strong) {
  color: #1f2937;
  font-weight: 600;
}

/* Références d'images stylisées */
.prose-custom :deep(.image-reference) {
  color: #f97316 !important;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  background: linear-gradient(135deg, #fef3e2, #fed7aa);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid #fdba74;
  transition: all 0.2s ease;
}

.prose-custom :deep(.image-reference:hover) {
  background: linear-gradient(135deg, #fed7aa, #fdba74);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(249, 115, 22, 0.3);
}

/* Liens externes */
.prose-custom :deep(a[target="_blank"]) {
  color: #2563eb;
  text-decoration: underline;
  transition: color 0.2s ease;
}

.prose-custom :deep(a[target="_blank"]:hover) {
  color: #1d4ed8;
}

/* Anciens styles pour compatibilité */
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
  padding-left: 0;
}
</style>