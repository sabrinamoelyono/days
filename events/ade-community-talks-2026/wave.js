// Square-ended bars with irregular, audio-like heights (seeded, so every render is identical).
document.querySelectorAll('.wave').forEach(w => {
  let seed = 7;
  const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  for (let i = 0; i < 96; i++) {
    const x = i / 95;
    const body = .35 + .65 * Math.abs(Math.sin(x * 9.5 + .6));
    const h = Math.min(1, Math.max(.06, body * (.25 + rand() * .85)));
    const b = document.createElement('i');
    b.style.height = (6 + h * 64) + 'px'; b.style.opacity = (.35 + h * .55).toFixed(2);
    w.appendChild(b);
  }
});
