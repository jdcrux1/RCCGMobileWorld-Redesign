import os
import re

pages = [
    'sermons.html', 'contact.html', 'give.html', 'blog.html',
    'devotionals.html', 'testimonies.html', 'gallery.html',
    'privacy-policy.html', 'terms-of-service.html', 'blog-post.html'
]

with open('pages/about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# 1. Extract head links
head_links = '<link rel="stylesheet" href="../style.css">\n    <link rel="stylesheet" href="../pages-shared.css">'

# 2. Extract Overlays
overlays_match = re.search(r'(<!-- SEARCH OVERLAY -->.*?)(?=<!-- Navigation -->)', about_html, re.DOTALL)
overlays = overlays_match.group(1).strip() if overlays_match else ""

# 3. Extract Footer
footer_match = re.search(r'(<footer class="bg-\[#020617\].*?</footer>)', about_html, re.DOTALL)
footer = footer_match.group(1)

# 4. Extract Back to Top & Script
btt_match = re.search(r'(<!-- Back to Top -->.*?)</body>', about_html, re.DOTALL)
btt = btt_match.group(1).strip() if btt_match else ""

for page in pages:
    filepath = os.path.join('pages', page)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pre-step: extract any page-specific custom scripts we don't want to lose
    # explicitly for sermons.html and others
    custom_scripts = ""
    scripts_match = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
    for s in scripts_match:
        if 'playVideo' in s or 'selectGivingType' in s or 'openTestimonyModal' in s:
            # Reconstruct just the logic needed, skipping the duplicate nav/back-to-top stuff.
            lines = s.split('\n')
            clean_lines = []
            skip = False
            for line in lines:
                if '// Back to Top' in line or 'window.addEventListener(\'scroll\'' in line:
                    skip = True
                if skip and ('});' in line or '() =>' in line):
                    # this is flimsy but we'll try to just keep specific functions
                    pass
                
            # Better approach: regex out just what we want
            if 'playVideo' in s:
               match_vid = re.search(r'(function playVideo.*?})(.*?(function closeVideo.*?}))', s, re.DOTALL)
               if match_vid:
                   custom_scripts += "\n" + match_vid.group(1) + "\n" + match_vid.group(3) + "\n"
               # filter buttons for sermons
               match_filt = re.search(r'(document\.querySelectorAll\(\'.filter-btn\'\).*?}\);)', s, re.DOTALL)
               if match_filt:
                   custom_scripts += "\n" + match_filt.group(1) + "\n"

            if 'selectGivingType' in s:
                custom_scripts += s # Just keep whole script block for give.html, it's mostly give logic
            
            if 'openTestimonyModal' in s:
                 custom_scripts += s # testimonies logic
                 
    # 1. Replace <style> block
    if '<style>' in content:
        content = re.sub(r'<style>.*?</style>', head_links, content, flags=re.DOTALL)
    elif head_links not in content:
        content = content.replace('</head>', f'    {head_links}\n</head>')

    # 2. Add overlays after body
    # Remove existing overlays if any (to avoid duplicates)
    content = re.sub(r'<!-- SEARCH OVERLAY -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- LOGIN DRAWER -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- VIDEO MODAL -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    content = re.sub(r'(<body[^>]*>)', r'\1\n\n    ' + overlays, content, count=1)

    # 3. Update Page Hero
    hero_match = re.search(r'<section class="page-hero">.*?</section>', content, re.DOTALL)
    if hero_match:
        old_hero = hero_match.group(0)
        
        # Extract title
        title_m = re.search(r'<h1[^>]*>(.*?)</h1>', old_hero, re.DOTALL)
        title_text = title_m.group(1) if title_m else "Page Title"
        title_text = re.sub(r'<[^>]+>', '', title_text).strip()
        
        words = title_text.split()
        if len(words) > 1:
            keyword = words[-1]
            title_html = f'{" ".join(words[:-1])} <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-brand-accent">{keyword}</span>'
        else:
            title_html = f'<span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-brand-accent">{title_text}</span>'
            
        # Extract subtitle
        sub_m = re.search(r'<p class="page-hero-subtitle[^>]*>(.*?)</p>', old_hero, re.DOTALL)
        if not sub_m:
            sub_m = re.search(r'<p class="text-gray-400[^>]*>(.*?)</p>', old_hero, re.DOTALL)
        subtitle = sub_m.group(1).strip() if sub_m else ""
        
        # Extract Category/Label
        lbl_m = re.search(r'<p class="[^"]*section-label[^"]*">(.*?)</p>', old_hero, re.DOTALL)
        if not lbl_m:
            lbl_m = re.search(r'<p class="text-brand-accent[^"]*">(.*?)</p>', old_hero, re.DOTALL)
            
        label = lbl_m.group(1).strip() if lbl_m else "RCCG Platform"
        if not lbl_m and "page-hero-label" in old_hero:
           lbl_m2 = re.search(r'<span class="page-hero-label">(.*?)</span>', old_hero, re.DOTALL)
           if lbl_m2: label = lbl_m2.group(1).strip()

        new_hero = f'''<section class="page-hero">
        <div class="page-hero-content page-fade-in">
            <span class="page-hero-label">{label}</span>
            <h1 class="page-hero-title">{title_html}</h1>
            <p class="page-hero-subtitle">{subtitle}</p>
        </div>
    </section>'''
        content = content.replace(old_hero, new_hero)
    
    # 4 & 5. Replace Footer and Back to Top
    # Wipe everything from footer to EOF and replace
    if '<footer' in content:
        before_footer = content.split('<footer')[0]
        
        # Determine if we have specific custom scripts we saved
        extra_script_html = f"\n    <script>\n{custom_scripts}\n    </script>" if custom_scripts else ""
        if 'openTestimonyModal' in content and 'testimonies.html' in page:
             extra_script_html = "" # we already captured it, don't double inject if it's already there? Wait, the previous block wipes bottom.
             # Actually for testimonies, we should keep the modal html as well!
             # Where was testimony modal? Above script!
             testimony_modal_match = re.search(r'<!-- Testimony Submission Modal -->.*?(<script>.*?</script>)', content, re.DOTALL)
             if testimony_modal_match:
                 before_footer += "\n    " + testimony_modal_match.group(0).replace(testimony_modal_match.group(1), '') 
                 extra_script_html = testimony_modal_match.group(1)

        # For sermons, there's a local video modal ABOVE the footer. We should keep it.
        if 'sermons.html' in page and 'id="videoModal"' in content:
             vid_modal_match = re.search(r'<!-- Video Modal -->.*?</div>\s*</div>', content, re.DOTALL)
             if vid_modal_match:
                 before_footer += "\n    " + vid_modal_match.group(0) + "\n"

        content = before_footer + footer + '\n\n    ' + btt + extra_script_html + '\n</body>\n</html>\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Batch processing complete.")
