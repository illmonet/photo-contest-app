window.onload = function() {
  const effect = document.getElementById('flower-effect');
  if (!effect) return;

  for (let i = 0; i < 30; i++) {
    const petal = document.createElement('div');
    petal.className = 'petal';
    petal.style.left = Math.random() * 100 + 'vw';
    petal.style.animationDuration = (Math.random() * 3 + 2) + 's';
    effect.appendChild(petal);
  }
};
