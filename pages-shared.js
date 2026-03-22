// ===== PAGES SHARED JS =====

// STICKY NAVBAR
window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    if (window.scrollY > 20) {
        nav.classList.add('shadow-lg');
    } else {
        nav.classList.remove('shadow-lg');
    }
});

// SEARCH TOGGLE
function toggleSearch() {
    const overlay = document.getElementById('searchOverlay');
    const input = document.getElementById('mainSearchInput');
    overlay.classList.toggle('open');
    if (overlay.classList.contains('open')) {
        setTimeout(() => input.focus(), 300);
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
}

// LOGIN TOGGLE
function toggleLogin(event) {
    if (event) event.preventDefault();
    const drawer = document.getElementById('loginDrawer');
    const overlay = document.getElementById('loginOverlayBg');
    if (drawer && overlay) {
        drawer.classList.toggle('active');
        overlay.classList.toggle('active');
        document.body.style.overflow = drawer.classList.contains('active') ? 'hidden' : 'auto';
    }
}

// LIVE STREAM MODAL
function openLiveStream(event) {
    if (event) event.preventDefault();
    const modal = document.getElementById('liveStreamModal');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeLiveStream() {
    const modal = document.getElementById('liveStreamModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
    setTimeout(() => {
        const iframe = document.getElementById('liveVideo');
        if (iframe) { iframe.src = iframe.src; }
    }, 300);
}

// MOBILE MENU TOGGLE
function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    if (menu) {
        menu.classList.toggle('active');
        document.body.style.overflow = menu.classList.contains('active') ? 'hidden' : 'auto';
    }
}

// ESCAPE KEY HANDLER
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        const searchOverlay = document.getElementById('searchOverlay');
        const loginDrawer = document.getElementById('loginDrawer');
        const loginOverlay = document.getElementById('loginOverlayBg');
        const streamModal = document.getElementById('liveStreamModal');

        if (searchOverlay && searchOverlay.classList.contains('open')) toggleSearch();
        if (loginDrawer && loginDrawer.classList.contains('active')) {
            loginDrawer.classList.remove('active');
            loginOverlay.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
        if (streamModal && streamModal.classList.contains('active')) closeLiveStream();
    }
});

// ACCORDION
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.accordion-header').forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.closest('.accordion-item');
            const isActive = item.classList.contains('active');
            // Close all
            document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('active'));
            if (!isActive) item.classList.add('active');
        });
    });
});

// FILTER BAR
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;
            document.querySelectorAll('[data-category]').forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = '';
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(10px)';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                        card.style.transition = 'all 0.4s ease';
                    }, 50);
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});

// SCROLL REVEAL
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-section').forEach(el => observer.observe(el));
});

// BACK TO TOP
(function () {
    const btn = document.getElementById('backToTop');
    const ring = document.getElementById('scrollRing');
    if (!btn || !ring) return;

    const circumference = 2 * Math.PI * 20;

    const footer = document.querySelector('footer');
    if (footer) {
        const io = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    btn.classList.toggle('visible', entry.isIntersecting);
                });
            },
            { threshold: 0.05 }
        );
        io.observe(footer);
    }

    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = docHeight > 0 ? scrollTop / docHeight : 0;
        ring.style.strokeDashoffset = circumference * (1 - progress);
    }, { passive: true });
})();

// GIVING AMOUNT SELECTOR logic removed as it is handled specifically in give.html
