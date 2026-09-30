// ==========================================================================
// PISSY VIBES — Interactive JavaScript
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    // 1. Animated Stats Counter
    const statElements = document.querySelectorAll('.stat-number');
    
    if (statElements.length > 0) {
        const animateCount = (el) => {
            const target = parseInt(el.getAttribute('data-target') || el.innerText.replace(/[^0-9]/g, ''), 10);
            if (isNaN(target)) return;
            
            let count = 0;
            const duration = 1800; // 1.8s
            const intervalTime = 20;
            const step = Math.ceil(target / (duration / intervalTime));
            
            const timer = setInterval(() => {
                count += step;
                if (count >= target) {
                    count = target;
                    clearInterval(timer);
                }
                el.innerText = count.toLocaleString('fr-FR');
            }, intervalTime);
        };

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCount(entry.target);
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        statElements.forEach(el => observer.observe(el));
    }

    // 2. Auto-close mobile navbar on click outside / link click
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle)');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    if (navbarCollapse && typeof bootstrap !== 'undefined') {
        const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse) || new bootstrap.Collapse(navbarCollapse, { toggle: false });
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    bsCollapse.hide();
                }
            });
        });
    }

    // 3. Photo Lightbox trigger
    const photoTriggers = document.querySelectorAll('[data-pv-lightbox]');
    const lightboxModal = document.getElementById('pvLightboxModal');
    const lightboxImg = document.getElementById('pvLightboxImg');
    const lightboxCaption = document.getElementById('pvLightboxCaption');

    if (photoTriggers.length > 0 && lightboxModal && lightboxImg) {
        photoTriggers.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const src = btn.getAttribute('data-img-src');
                const caption = btn.getAttribute('data-caption') || '';
                lightboxImg.src = src;
                if (lightboxCaption) {
                    lightboxCaption.innerText = caption;
                }
                const modal = new bootstrap.Modal(lightboxModal);
                modal.show();
            });
        });
    }
});
