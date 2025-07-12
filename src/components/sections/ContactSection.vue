<template>
  <section id="contact" class="content-section contact-section">
    <div class="container">
      <div class="section-content layout-split reverse">
        <!-- Contact Information -->
        <div class="text-content">
          <h2>{{ t.contact.title }}</h2>
          <div class="contact-items">
            <div class="contact-item">
              <div class="contact-icon">
                <i class="fas fa-envelope"></i>
              </div>
              <div class="contact-info">
                <h3>{{ t.contact.email }}</h3>
                <p><a href="mailto:projectnowlight@gmail.com">projectnowlight@gmail.com</a></p>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon">
                <i class="fas fa-phone"></i>
              </div>
              <div class="contact-info">
                <h3>{{ t.contact.phone }}</h3>
                <p><a href="tel:0783796492">07 83 79 64 92</a></p>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon">
                <i class="fas fa-map-marker-alt"></i>
              </div>
              <div class="contact-info">
                <h3>{{ t.contact.address }}</h3>
                <p>36 Av. Guy de Collongue, 69130 Écully</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Image -->
        <div class="media-content">
          <div class="contact-image-container" v-if="!ecoMode">
            <img
              src="@/assets/images/contact-image.png"
              alt="Contact NowLight"
              class="contact-image"
            />
          </div>
          <div class="eco-placeholder-media" v-else>
            <div class="flex flex-col items-center justify-center text-center p-8">
              <div class="w-16 h-16 bg-gray-300 rounded-full flex items-center justify-center mb-4">
                <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
              </div>
              <p class="text-gray-600 font-medium">{{ t.contact.title }}</p>
              <p class="text-sm text-gray-500 italic mt-2">Image désactivée en mode éco</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Campus Image -->
      <div class="campus-image-container" v-if="!ecoMode">
        <img
          src="@/assets/images/contact-campus.jpg"
          alt="Campus de Centrale Lyon"
          class="campus-image"
        />
      </div>
      <div class="eco-placeholder-campus" v-else>
        <div class="flex flex-col items-center justify-center text-center p-8">
          <div class="w-16 h-16 bg-gray-300 rounded-full flex items-center justify-center mb-4">
            <svg class="w-8 h-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
            </svg>
          </div>
          <p class="text-gray-600 font-medium">Campus de Centrale Lyon</p>
          <p class="text-sm text-gray-500 italic mt-2">Image désactivée en mode éco</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useLanguageStore } from '../../stores/language'

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
.contact-section {
  background-color: var(--secondary-color, #f8f8f8);
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

/* Text Content */
.text-content h2 {
  font-size: 2.2rem;
  font-weight: 700;
  color: var(--primary-color, #0a0a0a);
  margin-bottom: 1rem;
  position: relative;
}

.text-content h2::after {
  content: '';
  display: block;
  width: 70px;
  height: 4px;
  background-color: var(--accent-color, #FF8C00);
  margin-top: 15px;
  margin-bottom: 25px;
}

/* Contact Items */
.contact-items {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.contact-icon {
  width: 50px;
  height: 50px;
  background-color: var(--accent-color, #FF8C00);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: transform var(--transition-speed, 0.3s), box-shadow var(--transition-speed, 0.3s);
}

.contact-icon i {
  color: white;
  font-size: 1.2rem;
}

.contact-item:hover .contact-icon {
  transform: translateY(-3px);
  box-shadow: 0 8px 15px rgba(255, 140, 0, 0.3);
}

.contact-info h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--primary-color, #0a0a0a);
  margin-bottom: 5px;
}

.contact-info p {
  color: var(--text-light, #666);
  margin-bottom: 0;
  font-size: 1rem;
}

.contact-info a {
  color: var(--text-light, #666);
  text-decoration: none;
  transition: color var(--transition-speed, 0.3s);
}

.contact-info a:hover {
  color: var(--accent-color, #FF8C00);
  text-decoration: underline;
}

/* Media Content */
.contact-image-container {
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  background-color: #e0e0e0;
  height: 100%;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.contact-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 10px;
  transition: transform var(--transition-speed, 0.3s);
}

.contact-image:hover {
  transform: scale(1.02);
}

/* Campus Image */
.campus-image-container {
  margin-top: 60px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  background-color: #e0e0e0;
}

.campus-image {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 10px;
  transition: transform var(--transition-speed, 0.3s);
}

.campus-image:hover {
  transform: scale(1.02);
}

/* Eco Mode Placeholders */
.eco-placeholder-media,
.eco-placeholder-campus {
  border: 2px dashed #d1d5db;
  border-radius: 10px;
  background-color: #f9fafb;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.eco-placeholder-campus {
  margin-top: 60px;
  min-height: 200px;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .contact-item {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .contact-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto;
  }

  .contact-icon i {
    font-size: 1.5rem;
  }

  .text-content h2 {
    font-size: 1.8rem;
    text-align: center;
  }

  .text-content h2::after {
    margin-left: auto;
    margin-right: auto;
  }

  .campus-image-container {
    margin-top: 40px;
  }
}

@media (max-width: 480px) {
  .contact-items {
    gap: 25px;
  }

  .contact-icon {
    width: 50px;
    height: 50px;
  }

  .contact-icon i {
    font-size: 1.2rem;
  }

  .text-content h2 {
    font-size: 1.6rem;
  }
}
</style>