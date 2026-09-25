/* Local enhancement; plotted values are available in the Markdown tables and JSON ledger. */
'use strict';
document.querySelectorAll('main table').forEach(table => {
  const wrap = document.createElement('div');
  wrap.className = 'analysis-table-scroll';
  wrap.tabIndex = 0;
  wrap.setAttribute('role', 'region');
  wrap.setAttribute('aria-label', 'Data table; scroll horizontally for all columns');
  table.before(wrap); wrap.append(table);
});
document.querySelectorAll('.analysis-figure').forEach(figure => {
  const tooltip = figure.querySelector('.map-tooltip');
  const show = marker => { tooltip.textContent = marker.dataset.tooltip; tooltip.hidden = false; };
  const hide = () => { tooltip.hidden = true; };
  figure.querySelectorAll('[data-tooltip]').forEach(marker => {
    marker.addEventListener('pointerenter', () => show(marker));
    marker.addEventListener('pointerleave', hide);
    marker.addEventListener('focus', () => show(marker));
    marker.addEventListener('blur', hide);
    marker.addEventListener('click', () => show(marker));
    marker.addEventListener('keydown', event => { if (event.key === 'Escape') hide(); });
  });
});
