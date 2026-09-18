const menu = document.querySelector('.menu-button');
const nav = document.querySelector('.nav');
if (menu && nav) {
  const closeMenu = () => { nav.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); };
  menu.addEventListener('click', () => { const open = nav.classList.toggle('open'); menu.setAttribute('aria-expanded', String(open)); });
  nav.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); menu.focus(); } });
  document.addEventListener('click', e => { if (!e.target.closest('.header')) closeMenu(); });
}
const filters = [...document.querySelectorAll('.filter')];
const cards = [...document.querySelectorAll('[data-categories]')];
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(f => f.setAttribute('aria-pressed', String(f === button)));
  let count = 0;
  cards.forEach(card => { const show = button.dataset.filter === 'All' || card.dataset.categories.split('|').includes(button.dataset.filter); card.hidden = !show; if(show) count++; });
  const status = document.querySelector('.result-count');
  if(status) status.textContent = `${count} completed case ${count === 1 ? 'study' : 'studies'}`;
}));
const rotator = document.querySelector('[data-rotate]');
if(rotator && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){
 const lines=['Reproducible pipelines and trusted BI','Experimentation with sensitivity checks','Customer targeting and growth analytics'];
 let index=0; setInterval(()=>{if(!document.hidden){index=(index+1)%lines.length;rotator.textContent=lines[index];}},4500);
}
