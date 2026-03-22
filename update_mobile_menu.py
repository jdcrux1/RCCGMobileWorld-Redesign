import os

pages_dir = 'pages'
for filename in os.listdir(pages_dir):
    if not filename.endswith('.html'): continue
    
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Ministries is already in the mobile-menu-links
    if '<a href="ministries.html" class="mobile-menu-link">' in content:
        print(f"Skipping {filename} (Already has Ministries)")
        continue
    
    event_block = '''            <a href="events.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                Events
            </a>'''
            
    ministries_block = '''            <a href="events.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                Events
            </a>
            <a href="ministries.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                Ministries
            </a>'''
            
    # Some files might have different formatting, let's use a simpler replace
    event_svg = 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z'
    ministries_svg = 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z'
    
    if event_svg in content:
        # Find the end of the events a tag
        idx_event = content.find(event_svg)
        end_a = content.find('</a>', idx_event) + 4
        
        insert_block = f'''
            <a href="ministries.html" class="mobile-menu-link">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="{ministries_svg}"/></svg>
                Ministries
            </a>'''
            
        content = content[:end_a] + insert_block + content[end_a:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated mobile menu in {filename}")
    else:
        print(f"Could not find events SVG in {filename}")
