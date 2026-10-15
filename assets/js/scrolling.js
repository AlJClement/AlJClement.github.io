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
