(() => {
  'use strict';
  const navButton = document.querySelector('.nav-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  const setNavigation = (open, focus = false) => {
    navButton.setAttribute('aria-expanded', String(open));
    navButton.textContent = open ? 'Close' : 'Menu';
    mobileNav.hidden = !open;
    if (focus) (open ? mobileNav.querySelector('a') : navButton).focus();
  };
  navButton.addEventListener('click', () => setNavigation(mobileNav.hidden));
  mobileNav.addEventListener('click', e => { if (e.target.closest('a')) setNavigation(false); });
  document.addEventListener('keydown', e => {
    if (!mobileNav.hidden && e.key === 'Escape') setNavigation(false, true);
    if (!mobileNav.hidden && e.key === 'Tab') {
      const links = [...mobileNav.querySelectorAll('a')];
      if (e.shiftKey && document.activeElement === navButton) { e.preventDefault(); links.at(-1).focus(); }
      else if (!e.shiftKey && document.activeElement === links.at(-1)) { e.preventDefault(); navButton.focus(); }
    }
  });
  document.addEventListener('click', e => {
    if (!mobileNav.hidden && !e.target.closest('.site-header')) setNavigation(false);
  });
  matchMedia('(min-width: 768px)').addEventListener('change', e => { if (e.matches) setNavigation(false); });

  const menuSearch = document.querySelector('#menu-search');
  if (menuSearch) {
    const filters = [...document.querySelectorAll('[data-category]')];
    const groups = [...document.querySelectorAll('.menu-group')];
    const status = document.querySelector('#menu-status');
    const empty = document.querySelector('.empty-state');
    const glass = document.querySelector('#by-glass');
    const clear = document.querySelector('.clear-search');
    const labels = {seasonal:['Seasonal','Chef Pablo’s selections'], lunch:['Lunch','Tapas, paella & more'], dessert:['Dessert','Sweet things & after dinner'], drinks:['Cocktails & beer','From the bar'], wine:['Wine','By the glass & bottle'], spirits:['Spirits','For the last glass'], all:['Everything','The complete food & drinks menu']};
    const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    let category = 'seasonal';
    const apply = () => {
      const query = normalize(menuSearch.value.trim());
      let total = 0;
      groups.forEach(group => {
        let found = 0;
        const categoryMatches = category === 'all' || group.dataset.menuCategory === category;
        group.querySelectorAll('.dish').forEach(dish => {
          const text = group.querySelector('h3').textContent + ' ' + dish.textContent;
          const glassMatches = category !== 'wine' || !glass.checked || dish.dataset.glass === 'true';
          dish.hidden = !(categoryMatches && glassMatches && normalize(text).includes(query));
          if (!dish.hidden) found++;
        });
        group.hidden = found === 0;
        total += found;
      });
      filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.category === category)));
      document.querySelector('#category-title').textContent = labels[category][0];
      document.querySelector('#category-kicker').textContent = labels[category][1];
      document.querySelector('.glass-filter').hidden = category !== 'wine';
      status.textContent = total + (total === 1 ? ' selection' : ' selections') + (query ? ' matching “' + menuSearch.value.trim() + '”' : ' · Fall 2026');
      empty.hidden = total !== 0;
      clear.hidden = !query;
    };
    const fromHash = () => {
      const hash = location.hash.slice(1);
      if (labels[hash]) category = hash;
      apply();
    };
    filters.forEach(button => button.addEventListener('click', () => {
      category = button.dataset.category;
      history.replaceState(null, '', '#' + category);
      apply();
    }));
    let previousQuery = '';
    menuSearch.addEventListener('input', () => {
      if (!previousQuery && menuSearch.value.trim()) { category = 'all'; history.replaceState(null, '', '#all'); }
      previousQuery = menuSearch.value.trim();
      apply();
    });
    glass.addEventListener('change', apply);
    clear.addEventListener('click', () => {menuSearch.value=''; previousQuery=''; apply(); menuSearch.focus();});
    document.querySelector('.reset-menu').addEventListener('click', () => {
      category = 'all'; menuSearch.value = ''; previousQuery=''; glass.checked = false; history.replaceState(null, '', '#all'); apply(); menuSearch.focus();
    });
    document.querySelector('.mobile-menu-index')?.addEventListener('click', event => {
      event.preventDefault();
      document.querySelector('#menu-controls').scrollIntoView({behavior:'instant',block:'start'});
      document.querySelector('[data-category="' + category + '"]').focus({preventScroll:true});
    });
    document.querySelector('.print-menu').addEventListener('click', () => window.print());
    addEventListener('hashchange', fromHash);
    fromHash();
  }

  const lightbox = document.querySelector('.lightbox');
  if (lightbox) {
    const triggers = [...document.querySelectorAll('.gallery-open')];
    const image = lightbox.querySelector('img');
    let index = 0;
    let opener;
    const show = next => {
      index = (next + triggers.length) % triggers.length;
      const source = triggers[index].querySelector('img');
      image.src = source.src;
      image.alt = source.alt;
      lightbox.querySelector('.gallery-count').textContent = `${index + 1} / ${triggers.length}`;
      lightbox.querySelector('.gallery-caption').textContent = source.alt;
    };
    triggers.forEach((button, i) => button.addEventListener('click', event => {
      event.preventDefault(); opener = button; show(i); lightbox.showModal(); document.body.style.overflow = 'hidden';
    }));
    lightbox.querySelector('.close-lightbox').addEventListener('click', () => lightbox.close());
    lightbox.querySelector('.prev-photo').addEventListener('click', () => show(index - 1));
    lightbox.querySelector('.next-photo').addEventListener('click', () => show(index + 1));
    lightbox.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft') {e.preventDefault(); show(index - 1);}
      if (e.key === 'ArrowRight') {e.preventDefault(); show(index + 1);}
    });
    lightbox.addEventListener('click', e => {
      if (e.target !== lightbox) return;
      const r = lightbox.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) lightbox.close();
    });
    lightbox.addEventListener('close', () => { document.body.style.overflow = ''; opener?.focus(); });
  }
})();
