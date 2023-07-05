self.addEventListener('install', event => {
    event.waitUntil(
      caches.open('my-cache').then(cache => {
        return cache.addAll([
          '/',
          '/styles/global.css',
          '/styles/login.css',
          '/styles/home.css',
          '/styles/explorar.css',
          '/styles/index.css',
          '/styles/registrar.css',
          '/img/UnB-logo.png'
          
          // Adicione outros arquivos que você deseja armazenar em cache
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', event => {
    event.respondWith(
      caches.match(event.request).then(response => {
        return response || fetch(event.request);
      })
    );
  });