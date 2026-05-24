(function clock(){
  const el = document.getElementById('clock');
  if(!el) return;
  function tick(){
    const now = new Date();
    const utc = now.getTime() + now.getTimezoneOffset()*60000;
    const wita = new Date(utc + 8*3600000);
    const hh = String(wita.getHours()).padStart(2,'0');
    const mm = String(wita.getMinutes()).padStart(2,'0');
    el.textContent = `${hh}:${mm} WITA`;
  }
  tick();
  setInterval(tick, 30*1000);
})();

(function(){
  const el = document.getElementById('deploy-date');
  if(!el) return;
  el.textContent = new Date().toISOString().slice(0,10);
})();

(function reveal(){
  const els = document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){
    els.forEach(e=>e.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver((entries)=>{
    for(const e of entries){
      if(e.isIntersecting){
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    }
  }, {threshold:0.1, rootMargin:'0px 0px -6% 0px'});
  els.forEach(el=>io.observe(el));
})();
