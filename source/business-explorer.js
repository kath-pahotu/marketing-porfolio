/* One context selector, one insight per business model. */
(() => {
  document.querySelectorAll('.business-explorer').forEach(root => {
    const controls = root.querySelector('.bc-choices');
    if (!controls) return;
    const tabs = [...controls.querySelectorAll('[role="tab"]')];
    const panels = [...root.querySelectorAll('.bc-panel')];
    if (!tabs.length || tabs.some(tab => !panels.some(panel => panel.id === tab.getAttribute('aria-controls')))) return;

    function select(tab, focus = false) {
      tabs.forEach(item => {
        const active = item === tab;
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      panels.forEach(panel => { panel.hidden = panel.id !== tab.getAttribute('aria-controls'); });
      if (focus) tab.focus();
    }

    controls.addEventListener('click', event => {
      const tab = event.target.closest('[role="tab"]');
      if (tab && controls.contains(tab)) select(tab);
    });
    controls.addEventListener('keydown', event => {
      const index = tabs.indexOf(event.target);
      if (index < 0) return;
      let next;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % tabs.length;
      else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index + tabs.length - 1) % tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else return;
      event.preventDefault();
      select(tabs[next], true);
    });
    const narrow = window.matchMedia('(max-width: 620px)');
    const orient = () => controls.setAttribute('aria-orientation', narrow.matches ? 'vertical' : 'horizontal');
    orient();
    narrow.addEventListener('change', orient);
    select(tabs[0]);
    controls.hidden = false;
    root.classList.add('bc-enhanced');
  });
})();
