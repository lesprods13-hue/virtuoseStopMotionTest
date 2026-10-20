/* Stop Motion Virtuose — fonctionne hors ligne.
   Réseau d'abord (pour toujours avoir la dernière version), cache si pas de connexion. */
const CACHE='smv-v1.9';
const CORE=['./','index.html','manifest.json','icons/icon-192.png','icons/icon-512.png','icons/apple-touch-icon.png',
 ...['plage','pirate','ocean','nuit','espace','jungle','chateau','montagne','farwest','volcan','theatre','manoir'].flatMap(k=>[`decors/${k}.webp`,`decors/mini/${k}.webp`,`decors/p/${k}.webp`,`decors/p/mini/${k}.webp`])];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).catch(()=>{}));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);
 const same=u.origin===location.origin,font=/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname);if(!same&&!font)return;
 e.respondWith(fetch(r).then(res=>{if(res&&(res.ok||res.type==='opaque')){const copy=res.clone();caches.open(CACHE).then(c=>c.put(r,copy)).catch(()=>{})}return res})
  .catch(()=>caches.match(r,{ignoreSearch:true}).then(m=>m||(r.mode==='navigate'?caches.match('index.html'):Response.error()))))});
