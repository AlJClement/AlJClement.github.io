// Highlight the section currently in view without moving keyboard focus.
const navigationLinks = [...document.querySelectorAll('.topbar nav a')];
const sections = [...document.querySelectorAll('main > section[id]')];
function updateNavigation() {
  const topbarHeight = document.querySelector('.topbar').getBoundingClientRect().height;
  document.documentElement.style.setProperty('--bar-height', `${topbarHeight}px`);
  let current = sections[0];
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= topbarHeight + 100) current = section;
  }
  if (Math.ceil(window.innerHeight + window.scrollY) >= document.documentElement.scrollHeight - 2) current = sections[sections.length - 1];
  for (const link of navigationLinks) {
    if (new URL(link.href).hash === `#${current.id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}
let pending = false;
window.addEventListener('scroll', () => {
  if (!pending) {
    pending = true;
    requestAnimationFrame(() => { updateNavigation(); pending = false; });
  }
}, { passive: true });
window.addEventListener('resize', updateNavigation);
updateNavigation();

// Photo carousel: stop for focus, hover, hidden tabs, or reduced motion.
for (const carousel of document.querySelectorAll('.slideshow')) {
  const slides = [...carousel.querySelectorAll('.slideshow-slide')];
  if (slides.length < 2) continue;
  const controls = carousel.querySelector('.slideshow-controls');
  const pauseButton = controls.querySelector('[data-slide="pause"]');
  const status = controls.querySelector('.slideshow-status');
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;
  let paused = motion.matches;
  let hovered = false;
  let timer;
  function show(next, announce = false) {
    slides[index].hidden = true;
    index = (next + slides.length) % slides.length;
    slides[index].hidden = false;
    status.setAttribute('aria-live', announce ? 'polite' : 'off');
    status.textContent = `${index + 1} / ${slides.length}`;
  }
  function schedule() {
    clearInterval(timer);
    pauseButton.textContent = paused ? 'Play slideshow' : 'Pause slideshow';
    if (!paused && !hovered && !document.hidden && !carousel.contains(document.activeElement)) {
      timer = setInterval(() => show(index + 1), Number(carousel.dataset.interval));
    }
  }
  controls.hidden = false;
  controls.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;
    if (button.dataset.slide === 'pause') paused = !paused;
    else show(index + (button.dataset.slide === 'next' ? 1 : -1), true);
    schedule();
  });
  carousel.addEventListener('mouseenter', () => { hovered = true; schedule(); });
  carousel.addEventListener('mouseleave', () => { hovered = false; schedule(); });
  carousel.addEventListener('focusin', schedule);
  carousel.addEventListener('focusout', () => setTimeout(schedule, 0));
  carousel.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      show(index + (event.key === 'ArrowRight' ? 1 : -1), true);
    }
  });
  document.addEventListener('visibilitychange', schedule);
  motion.addEventListener('change', () => { paused = motion.matches; schedule(); });
  schedule();
}
