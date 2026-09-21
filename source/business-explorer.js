/* Business context controls are isolated from the site's navigation and workflow. */
(() => {
  const root = document.querySelector('.business-explorer');
  if (!root) return;
  const tabs = [...root.querySelectorAll('[role="tab"]')];
  const views = [...root.querySelectorAll('[data-bx-view]')];
  const status = root.querySelector('.bx-announcement');
  const selected = { ecosystem: 'saas', spotlight: 'saas', journey: 'audience' };

  function selectDetail(group, key, announce = false) {
    const controls = root.querySelector(`[data-bx-controls="${group}"]`);
    const button = controls.querySelector(`[data-bx-choice="${key}"]`);
    if (!button) return;
    selected[group] = key;
    controls.querySelectorAll('button').forEach(item => {
      item.setAttribute('aria-pressed', String(item === button));
    });
    root.querySelectorAll(`[data-bx-detail="${group}"]`).forEach(panel => {
      panel.hidden = panel.dataset.bxKey !== key;
    });
    if (announce) status.textContent = `${button.querySelector('strong').textContent} selected. Related context and case studies are shown below.`;
  }

  function selectView(tab, focus = false) {
    tabs.forEach(item => {
      const active = item === tab;
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
    });
    views.forEach(panel => { panel.hidden = panel.id !== tab.getAttribute('aria-controls'); });
    if (focus) tab.focus();
  }

  Object.entries(selected).forEach(([group, key]) => selectDetail(group, key));
  selectView(tabs[0]);
  root.classList.add('is-enhanced');
  root.querySelectorAll('.bx-tabs, [data-bx-controls]').forEach(group => { group.hidden = false; });

  root.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button || !root.contains(button)) return;
    if (button.getAttribute('role') === 'tab') {
      selectView(button);
      status.textContent = `${button.textContent} view selected.`;
    } else if (button.dataset.bxChoice) {
      const group = button.closest('[data-bx-controls]').dataset.bxControls;
      selectDetail(group, button.dataset.bxChoice, true);
      // Both domain views describe the same selection; the journey retains its stage.
      if (group === 'ecosystem' || group === 'spotlight') {
        selectDetail(group === 'ecosystem' ? 'spotlight' : 'ecosystem', button.dataset.bxChoice);
      }
    }
  });

  root.querySelector('.bx-tabs').addEventListener('keydown', event => {
    const index = tabs.indexOf(event.target);
    if (index < 0) return;
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
    else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = tabs.length - 1;
    else return;
    event.preventDefault();
    selectView(tabs[next], true);
  });
})();
