document.querySelectorAll('.wave').forEach(w => {
  for (let i = 0; i < 96; i++) {
    const x = i / 95;
    const h = Math.max(.08, Math.abs(Math.sin(x*21)*.55 + Math.sin(x*7.3+1)*.35 + Math.sin(x*53)*.18)) * Math.sin(Math.PI*x)**.6;
    const b = document.createElement('i');
    b.style.height = (8 + h*62) + 'px'; b.style.opacity = (.25 + h*.6).toFixed(2);
    w.appendChild(b);
  }
});
