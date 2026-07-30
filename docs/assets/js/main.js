/* GammaOS Nano wiki - client behaviour: theme, search, scroll-spy */
(function(){
  // ---- theme ----
  var saved = localStorage.getItem('gn-theme');
  if(saved){ document.documentElement.setAttribute('data-theme', saved); }
  else if(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches){
    document.documentElement.setAttribute('data-theme','dark');
  }
  window.toggleTheme = function(){
    var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', cur);
    localStorage.setItem('gn-theme', cur);
  };

  // ---- search ----
  var input = document.getElementById('search-input');
  var box = document.getElementById('search-results');
  var index = null, results = [], active = -1;

  function load(cb){
    if(index){ cb(); return; }
    fetch('search-index.json').then(function(r){return r.json();}).then(function(d){ index = d; cb(); })
      .catch(function(){ index = []; cb(); });
  }
  function esc(s){ return String(s).replace(/[&<>]/g, function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}); }
  function hl(text, q){
    var i = text.toLowerCase().indexOf(q);
    if(i < 0){ return esc(text.slice(0,120)); }
    var start = Math.max(0, i - 30);
    var end = Math.min(text.length, i + q.length + 70);
    var out = (start > 0 ? '...' : '')
      + esc(text.slice(start, i))
      + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>'
      + esc(text.slice(i + q.length, end))
      + (end < text.length ? '...' : '');
    return out;
  }
  function score(item, q){
    var s = 0, t = item.title.toLowerCase(), d = (item.desc||'').toLowerCase(), b = item.text.toLowerCase();
    if(t === q){ s += 100; }
    if(t.indexOf(q) === 0){ s += 50; }
    if(t.indexOf(q) >= 0){ s += 30; }
    if(d.indexOf(q) >= 0){ s += 12; }
    if(b.indexOf(q) >= 0){ s += 8; }
    return s;
  }
  function render(q){
    if(!q){ box.hidden = true; box.innerHTML=''; return; }
    results = index.map(function(it){ return {it:it, s:score(it,q)}; })
      .filter(function(x){ return x.s>0; })
      .sort(function(a,b){ return b.s-a.s; })
      .slice(0,12);
    if(!results.length){ box.hidden=false; box.innerHTML='<div class="sr-empty">No matches for "'+esc(q)+'"</div>'; return; }
    box.hidden = false; active = -1;
    box.innerHTML = results.map(function(x,idx){
      var it = x.it, snip = hl(it.text, q);
      return '<a href="'+it.url+'" data-i="'+idx+'">'
        + '<span class="sr-group">'+esc(it.group)+'</span>'
        + '<span class="sr-title">'+esc(it.title)+'</span>'
        + '<span class="sr-snip">'+snip+'</span></a>';
    }).join('');
  }
  function move(dir){
    var links = box.querySelectorAll('a'); if(!links.length){ return; }
    active = (active + dir + links.length) % links.length;
    links.forEach(function(l,i){ l.classList.toggle('active', i===active); });
    links[active].scrollIntoView({block:'nearest'});
  }
  if(input){
    input.addEventListener('input', function(){ load(function(){ render(input.value.trim().toLowerCase()); }); });
    input.addEventListener('focus', function(){ if(input.value.trim()){ load(function(){ render(input.value.trim().toLowerCase()); }); } });
    input.addEventListener('keydown', function(e){
      if(e.key==='ArrowDown'){ e.preventDefault(); move(1); }
      else if(e.key==='ArrowUp'){ e.preventDefault(); move(-1); }
      else if(e.key==='Enter'){ var links=box.querySelectorAll('a'); if(links.length){ (links[active>=0?active:0]).click(); } }
      else if(e.key==='Escape'){ box.hidden=true; input.blur(); }
    });
    document.addEventListener('click', function(e){ if(!e.target.closest('.search')){ box.hidden=true; } });
    document.addEventListener('keydown', function(e){
      if(e.key==='/' && document.activeElement!==input && !/input|textarea/i.test(document.activeElement.tagName)){
        e.preventDefault(); input.focus();
      }
    });
  }

  // ---- scroll spy for TOC ----
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if(tocLinks.length){
    var targets = tocLinks.map(function(a){ return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); }).filter(Boolean);
    var spy = function(){
      var y = window.scrollY + 100, cur = null;
      targets.forEach(function(t){ if(t.offsetTop <= y){ cur = t; } });
      tocLinks.forEach(function(a){ a.classList.toggle('active', cur && a.getAttribute('href')==='#'+cur.id); });
    };
    window.addEventListener('scroll', spy, {passive:true}); spy();
  }

  document.querySelectorAll('.sidebar a').forEach(function(a){
    a.addEventListener('click', function(){ document.body.classList.remove('nav-open'); });
  });
})();
