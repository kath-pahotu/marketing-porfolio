const menuButton=document.querySelector('.menu-toggle');
const navigation=document.querySelector('#navigation');
menuButton?.addEventListener('click',()=>{const expanded=menuButton.getAttribute('aria-expanded')==='true';menuButton.setAttribute('aria-expanded',String(!expanded));navigation.classList.toggle('open',!expanded);});
navigation?.addEventListener('click',event=>{if(event.target.closest('a')){navigation.classList.remove('open');menuButton.setAttribute('aria-expanded','false');}});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&navigation?.classList.contains('open')){navigation.classList.remove('open');menuButton.setAttribute('aria-expanded','false');menuButton.focus();}});
const filters=document.querySelectorAll('[data-filter]');
const cases=document.querySelectorAll('.work-grid [data-category]');
filters.forEach(button=>button.addEventListener('click',()=>{const category=button.dataset.filter;filters.forEach(item=>{const active=item===button;item.classList.toggle('active',active);item.setAttribute('aria-pressed',String(active));});let count=0;cases.forEach(item=>{const show=category==='All work'||item.dataset.category===category;item.hidden=!show;if(show)count++;});document.querySelector('.result-count').textContent=`${count} case ${count===1?'study':'studies'}`;}));

filters.forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.library-group').forEach(group=>{group.hidden=!group.querySelector('.work-card:not([hidden])');});}));
