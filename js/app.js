document.documentElement.classList.add('js');
const toggle=document.querySelector('.menu-toggle'),nav=document.querySelector('.nav');
if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);toggle.textContent=open?'Close menu':'Menu';});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menu';toggle.focus();}});}
const search=document.querySelector('[data-search]');
if(search){search.addEventListener('input',()=>{const q=search.value.toLowerCase().trim();let count=0;document.querySelectorAll('[data-sport]').forEach(card=>{const match=card.dataset.sport.toLowerCase().includes(q);card.hidden=!match;if(match)count++;});document.querySelector('[data-count]').textContent=count+' sport'+(count===1?'':'s');document.querySelector('[data-empty]').hidden=count!==0;});}
// Do not promote a dated fundraiser after its drawing day begins.
function expireAnnouncements(){document.querySelectorAll('[data-expires]').forEach(el=>{if(Date.now()>=Date.parse(el.dataset.expires))el.remove();});}
expireAnnouncements();
setInterval(expireAnnouncements,60000);


// Progressive, accessible motion: no animation when reduced motion is requested.
const motionPreference=window.matchMedia('(prefers-reduced-motion: reduce)');
if(!motionPreference.matches&&'IntersectionObserver' in window){
  const revealTargets=document.querySelectorAll('.section-head,.action-card,.story-inner>div,.story-inner figure,.mission-inner,.winter-registration,.winter-options article,.registration-guide>*,.leadership-grid article,.sport-card,.resource-sections>article,.contact,.photo-grid figure,.calendar-callout');
  const observer=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  },{threshold:0.08,rootMargin:'0px 0px -25px 0px'});
  revealTargets.forEach((element,index)=>{
    // Off-screen targets animate on reveal; visible targets render normally.
    if(element.getBoundingClientRect().top>window.innerHeight-35){
      element.classList.add('reveal-on-scroll');
      element.style.setProperty('--reveal-delay',((index%3)*75)+'ms');
      observer.observe(element);
    }
  });
}
// Navigation closes after selecting a destination on smaller screens.
if(toggle&&nav){nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{
  nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menu';
}));}
