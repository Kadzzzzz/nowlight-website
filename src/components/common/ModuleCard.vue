<template>
  <div
    class="module-item"
    :class="{ 'clickable': !isVideo, 'video-module': isVideo }"
    @click="handleClick"
    @keydown.enter="handleClick"
    :tabindex="isVideo ? -1 : 0"
    :role="isVideo ? null : 'button'"
    :aria-label="isVideo ? null : `Ouvrir les détails de ${module.title}`"
  >
    <!-- Video Module -->
    <div v-if="isVideo && !ecoMode" class="video-container">
      <iframe
        :src="`https://www.youtube.com/embed/${getVideoId(module.videoId)}?si=qiAr-S-BpzndE4jw`"
        :title="module.title"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>

    <!-- Eco Video Placeholder -->
    <div v-else-if="ecoMode && isVideo" class="module-image eco-placeholder-video">
      <div class="eco-placeholder-content">
        <i class="fas fa-video-slash"></i>
        <span>Video Disabled</span>
      </div>
    </div>

    <!-- Regular Module Image -->
    <div v-else class="module-image">
      <img
        v-if="!ecoMode && getFirstModuleImage()"
        :src="getFirstModuleImage()"
        :alt="module.title"
        class="module-preview-image"
      />
      <span v-else class="eco-placeholder-module-index">+</span>
    </div>

    <!-- Module Title -->
    <h3 class="module-title">{{ module.title }}</h3>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  module: {
    type: Object,
    required: true
  },
  isVideo: {
    type: Boolean,
    default: false
  },
  ecoMode: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

const handleClick = () => {
  if (!props.isVideo) {
    emit('click')
  }
}

const getVideoId = (videoId) => {
  if (!videoId) return ''
  // Clean video ID (remove parameters if present)
  return videoId.split('?')[0]
}

const getFirstModuleImage = () => {
  if (!props.module.images || !Array.isArray(props.module.images) || props.module.images.length === 0) {
    return null
  }

  try {
    const imagePath = props.module.images[0]
    return new URL(`../../assets/images/${imagePath}`, import.meta.url).href
  } catch (error) {
    console.error(`Error resolving image URL for "${props.module.images[0]}":`, error)
    return null
  }
}
</script>

<style scoped>
.module-item {
  background-color: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  transition: all var(--transition-speed, 0.3s) ease;
}

.module-item.clickable {
  cursor: pointer;
  transition: transform var(--transition-speed, 0.3s), box-shadow var(--transition-speed, 0.3s);
}

.module-item.clickable:hover,
.module-item.clickable:focus {
  transform: translateY(-8px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
  outline: 2px solid var(--accent-color, #FF8C00);
  outline-offset: 2px;
}

/* Video Container */
.video-container {
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  position: relative;
  background-color: #000;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Module Image */
.module-image {
  width: 100%;
  height: 180px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.module-preview-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
}

.module-item.clickable:hover .module-preview-image {
  transform: scale(1.05);
}

.eco-placeholder-module-index {
  font-size: 2.5rem;
  color: var(--text-light, #666);
  font-weight: bold;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Eco Video Placeholder */
.eco-placeholder-video {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  height: 180px;
}

.eco-placeholder-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  color: white;
}

.eco-placeholder-content i {
  font-size: 2.5rem;
}

/* Module Title */
.module-title {
  padding: 20px;
  font-size: 1.1rem;
  text-align: center;
  margin: 0;
  font-weight: 600;
  color: var(--primary-color, #0a0a0a);
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1.3;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .module-image {
    height: 160px;
  }

  .module-title {
    padding: 15px;
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .module-image {
    height: 140px;
  }

  .eco-placeholder-module-index {
    font-size: 2rem;
  }

  .eco-placeholder-content i {
    font-size: 2rem;
  }
}
</style>