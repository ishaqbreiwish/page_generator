// Import Alpine.js
import Alpine from 'alpinejs';

// Import aos
import AOS from 'aos';

// Import sticky-js
import Sticky from 'sticky-js';

// Initialize Alpine
window.Alpine = Alpine;
Alpine.start();

AOS.init({
  once: true,
  disable: 'phone',
  duration: 700,
  easing: 'ease-out-cubic',
});

// eslint-disable-next-line no-unused-vars
const sticky = new Sticky('[data-sticky]');

// import component from './components/component';
