// STICKY NAVBAR
window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    if (!nav) return;
    if (window.scrollY > 20) {
        nav.classList.add('shadow-lg');
        nav.classList.remove('bg-transparent');
        nav.classList.add('bg-brand-base/90');
    } else {
        nav.classList.remove('shadow-lg');
        nav.classList.remove('bg-brand-base/90');
        nav.classList.add('bg-transparent');
    }
});

// SEARCH TOGGLE
function toggleSearch() {
    const overlay = document.getElementById('searchOverlay');
    const input = document.getElementById('mainSearchInput');
    overlay.classList.toggle('open');
    if (overlay.classList.contains('open')) {
        setTimeout(() => input.focus(), 300); // Focuses the input automatically
        document.body.style.overflow = 'hidden'; // Prevents background scrolling
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

        if (drawer.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = 'auto';
        }
    }
}

// MOBILE MENU TOGGLE
function toggleMobileMenu() {
    try {
        const menu = document.getElementById('mobileMenu');
        if (menu) {
            menu.classList.toggle('active');
            document.body.style.overflow = menu.classList.contains('active') ? 'hidden' : 'auto';
            console.log('Mobile menu toggled, active:', menu.classList.contains('active'));
        } else {
            console.error('Mobile menu element not found');
        }
    } catch (e) {
        console.error('Error toggling mobile menu:', e);
    }
}

// LIVE STREAM MODAL
function openLiveStream(event) {
    if (event) event.preventDefault();
    const modal = document.getElementById('liveStreamModal');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// EMAIL SUBSCRIBE
function handleEmailSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const email = form.querySelector('input[type="email"]').value;
    alert('Thank you for subscribing! We will send updates to ' + email);
    form.reset();
}

function closeLiveStream() {
    const modal = document.getElementById('liveStreamModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';

    setTimeout(() => {
        const iframe = document.getElementById('liveVideo');
        if (iframe) {
            const currentSrc = iframe.src;
            iframe.src = currentSrc;
        }
    }, 300);
}

// INLINE SERMON VIDEO
function playSermonVideo() {
    const container = document.getElementById('sermonVideoContainer');
    if (container && !container.querySelector('iframe')) {
        container.innerHTML = `
            <iframe 
                src="https://www.youtube.com/embed/bH7KTcePBBw?autoplay=1" 
                class="absolute inset-0 w-full h-full" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>`;
    }
}

// Close everything when the Escape key is pressed
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        const searchOverlay = document.getElementById('searchOverlay');
        const loginDrawer = document.getElementById('loginDrawer');
        const loginOverlay = document.getElementById('loginOverlayBg');
        const streamModal = document.getElementById('liveStreamModal');
        const eventPanel = document.getElementById('eventPanel');

        if (searchOverlay && searchOverlay.classList.contains('open')) toggleSearch();

        if (loginDrawer && loginDrawer.classList.contains('active')) {
            loginDrawer.classList.remove('active');
            loginOverlay.classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        if (streamModal && streamModal.classList.contains('active')) {
            closeLiveStream();
        }

        if (eventPanel && eventPanel.classList.contains('active')) {
            closeEventDetails();
        }
    }
});

// PRELOADER LOGIC
document.addEventListener('DOMContentLoaded', () => {
    const preloader = document.getElementById('preloader');
    const loaderMask = document.getElementById('loaderMask');
    const loaderCounter = document.getElementById('loaderCounter');

    if (!preloader) return;

    document.body.classList.add('loading');

    let count = 0;
    const interval = setInterval(() => {
        if (count < 90) {
            count += Math.random() * 1.5 + 0.2; // Even smoother/slower increments
        } else if (count < 99) {
            count += 0.1;
        }

        updateLoader(count);

        if (count >= 100) {
            clearInterval(interval);
        }
    }, 60); // Slower interval (60ms instead of 40ms)

    window.addEventListener('load', () => {
        count = 100;
        updateLoader(100);
        preloader.classList.add('fully-loaded'); // Explicitly add here too
        setTimeout(finishLoading, 1200); // Give more time for the gold boom effect
    });

    function updateLoader(value) {
        const displayCount = Math.floor(value);
        loaderCounter.innerText = `${displayCount}%`;
        loaderMask.style.width = `${displayCount}%`;

        if (displayCount >= 100) {
            preloader.classList.add('fully-loaded');
        }
    }

    function finishLoading() {
        preloader.style.opacity = '0';
        preloader.style.visibility = 'hidden';
        document.body.classList.remove('loading');

        setTimeout(() => {
            if (preloader.parentNode) {
                preloader.parentNode.removeChild(preloader);
            }
        }, 1000);
    }
});

// EVENT PANEL LOGIC
const eventData = {
    'youth-conference': {
        category: 'Youth Development',
        title: 'Youth Conference 2026',
        date: 'March 15, 2026',
        time: '9:00 AM - 4:00 PM',
        location: 'Main Auditorium, Redemption City',
        description: 'Empowering the next generation of leaders through spiritual growth, personal development sessions, and networking opportunities. Join thousands of young people as we explore "Kingdom Influence in a Digital Age".'
    },
    'easter-service': {
        category: 'Special Service',
        title: 'Easter Celebration Service',
        date: 'April 5, 2026',
        time: '8:00 AM & 10:00 AM',
        location: 'Church Campus, Lagos',
        description: 'Celebrate the resurrection of our Lord Jesus Christ. A special service filled with powerful worship, dance drama, and a life-changing message of hope and restoration. Bring your family and friends!'
    },
    'marriage-retreat': {
        category: 'Couples',
        title: 'Marriage Retreat',
        date: 'April 20-22, 2026',
        time: 'All Day Event',
        location: 'Redemption Resort Center',
        description: 'A weekend dedicated to strengthening marriages, fostering intimacy, and building godly homes. Enjoy practical workshops, romantic dinners, and renewed commitment in a serene environment.'
    }
};

function openEventDetails(eventKey) {
    const data = eventData[eventKey];
    if (!data) return;

    const panel = document.getElementById('eventPanel');
    const overlay = document.getElementById('eventOverlayBg');
    const content = document.getElementById('eventPanelContent');

    content.innerHTML = `
        <div class="event-detail-category">${data.category}</div>
        <h2 class="event-detail-title">${data.title}</h2>
        
        <div class="event-detail-meta">
            <div class="event-meta-item">
                <span class="event-meta-label">Date</span>
                <span class="event-meta-value">${data.date}</span>
            </div>
            <div class="event-meta-item">
                <span class="event-meta-label">Time</span>
                <span class="event-meta-value">${data.time}</span>
            </div>
            <div class="event-meta-item">
                <span class="event-meta-label">Location</span>
                <span class="event-meta-value">${data.location}</span>
            </div>
            <div class="event-meta-item">
                <span class="event-meta-label">Status</span>
                <span class="event-meta-value">Registration Open</span>
            </div>
        </div>

        <div class="event-detail-description">
            <p>${data.description}</p>
        </div>

        <div class="event-panel-footer">
            <button class="event-register-btn" onclick="alert('Registration feature coming soon!')">Register Now</button>
        </div>
    `;

    panel.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeEventDetails() {
    const panel = document.getElementById('eventPanel');
    const overlay = document.getElementById('eventOverlayBg');

    panel.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// BACK TO TOP — show only near footer, ring = scroll progress
(function () {
    const btn = document.getElementById('backToTop');
    const ring = document.getElementById('scrollRing');
    if (!btn || !ring) return;

    const circumference = 2 * Math.PI * 20; // r=20

    // Use IntersectionObserver on the footer to toggle visibility
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

    // Update progress ring on scroll
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = docHeight > 0 ? scrollTop / docHeight : 0;
        ring.style.strokeDashoffset = circumference * (1 - progress);
    }, { passive: true });
})();
