#!/usr/bin/env python3
"""Add mobile menu HTML and fix hamburger onclick to all subpages in pages/ folder."""
import os

PAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages')

MOBILE_MENU_HTML = '''
    <!-- FULL-SCREEN MOBILE MENU -->
    <div class="mobile-menu" id="mobileMenu">
        <div class="mobile-menu-header">
            <a href="../index.html" class="flex items-center">
                <img src="../rccg-for-web.png" alt="RCCG Logo" class="h-10 w-auto">
            </a>
            <button class="mobile-menu-close" onclick="toggleMobileMenu()" aria-label="Close menu">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
        </div>
        <div class="mobile-menu-links">
            <a href="../index.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                Home
            </a>
            <a href="about.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                About
            </a>
            <a href="sermons.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                Sermons
            </a>
            <a href="events.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                Events
            </a>
            <a href="contact.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                Contact
            </a>
            <a href="#" onclick="toggleLogin(event); toggleMobileMenu();" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                Login
            </a>
        </div>
        <div class="mobile-menu-ctas">
            <a href="#" onclick="openLiveStream(event); toggleMobileMenu();" class="btn-outline text-white">
                <svg class="w-5 h-5 text-red-500" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/></svg>
                Watch Live
            </a>
            <a href="give.html" class="btn-primary text-white">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                Give
            </a>
        </div>
    </div>
'''

pages = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith('.html')])
count = 0
for page in pages:
    filepath = os.path.join(PAGES_DIR, page)
    with open(filepath, 'r') as f:
        content = f.read()
    
    modified = False
    
    if 'id="mobileMenu"' in content:
        print(f'SKIP {page} (already has mobileMenu)')
        continue
    
    if '</nav>' in content:
        idx = content.index('</nav>') + len('</nav>')
        content = content[:idx] + MOBILE_MENU_HTML + content[idx:]
        modified = True
        print(f'ADD mobile menu to {page}')
    
    if 'toggleMobileMenu' not in content and 'M4 6h16M4 12h16M4 18h16' in content:
        content = content.replace(
            '<button class="text-gray-300 hover:text-white p-2">',
            '<button onclick="toggleMobileMenu()" aria-label="Open menu" class="text-gray-300 hover:text-white p-2">'
        )
        modified = True
        print(f'FIX hamburger in {page}')
    
    if modified:
        with open(filepath, 'w') as f:
            f.write(content)
        count += 1

print(f'Done! Modified {count} files.')
