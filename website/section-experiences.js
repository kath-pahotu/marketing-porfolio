/* Each section owns its controls; no global navigation or autoplay. */
(() => {
  document.querySelectorAll('[data-mx-explorer]').forEach(root => {
    const controls = root.querySelector('[data-mx-controls]');
    if (!controls) return;
    const tabs = [...controls.querySelectorAll('[role="tab"]')];
    const panels = [...root.querySelectorAll('[data-mx-panel]')];
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
      const current = tabs.indexOf(event.target);
      if (current < 0) return;
      let next;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (current + 1) % tabs.length;
      else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (current + tabs.length - 1) % tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else return;
      event.preventDefault();
      select(tabs[next], true);
    });

    // Match the orientation to the responsive question chooser layout.
    if (controls.classList.contains('mx-controls--analysis')) {
      const wide = window.matchMedia('(min-width: 761px)');
      const orient = () => controls.setAttribute('aria-orientation', wide.matches ? 'vertical' : 'horizontal');
      orient();
      wide.addEventListener('change', orient);
    }
    select(tabs[0]);
    controls.hidden = false;
    root.classList.add('mx-enhanced');
  });
})();
