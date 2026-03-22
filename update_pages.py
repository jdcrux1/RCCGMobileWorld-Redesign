import os
import re

def update_pages():
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Extract nav
    nav_match = re.search(r'<nav[^>]*>.*?</nav>', index_content, re.DOTALL)
    if not nav_match:
        print("Could not find <nav> in index.html")
        return
    nav_block = nav_match.group(0)
    
    # Extract footer
    footer_match = re.search(r'<footer[^>]*>.*?</footer>', index_content, re.DOTALL)
    if not footer_match:
        print("Could not find <footer> in index.html")
        return
    footer_block = footer_match.group(0)
    
    # Extract tailwind config
    tailwind_match = re.search(r'<script>\s*tailwind\.config = \{.*?</script>', index_content, re.DOTALL)
    if not tailwind_match:
        print("Could not find tailwind config in index.html")
        return
    tailwind_block = tailwind_match.group(0)

    # Prepare nav and footer blocks for pages/ directory
    pages_nav = nav_block.replace('href="pages/', 'href="')
    pages_nav = pages_nav.replace('href="index.html"', 'href="../index.html"')
    pages_nav = pages_nav.replace('src="logo.png"', 'src="../logo.png"')
    
    pages_footer = footer_block.replace('href="pages/', 'href="')
    pages_footer = pages_footer.replace('href="index.html"', 'href="../index.html"')
    pages_footer = pages_footer.replace('src="logo.png"', 'src="../logo.png"')
    
    pages_dir = 'pages'
    for filename in os.listdir(pages_dir):
        if not filename.endswith('.html'): continue
        
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Replace nav
        content = re.sub(r'<nav class="fixed[^>]*>.*?</nav>', pages_nav, content, flags=re.DOTALL)
        
        # Replace footer
        content = re.sub(r'<footer[^>]*>.*?</footer>', pages_footer, content, flags=re.DOTALL)
        
        # Replace tailwind config
        content = re.sub(r'<script>\s*tailwind\.config = \{.*?</script>', tailwind_block, content, flags=re.DOTALL)
        
        # Replace green theme to blue
        content = content.replace('brand-green', 'brand-accent')
        content = content.replace('brand-greendark', 'brand-accent') # just in case
        content = content.replace('bg-[#16a34a]', 'bg-blue-600')
        content = content.replace('bg-[#22c55e]', 'bg-brand-accent')
        
        # In specific files like sermons.html, the green CSS is defined in <style> block,
        # where it has `#22c55e` and `#4ade80`. I'll replace those directly for consistency.
        content = content.replace('#22c55e', '#3b82f6') # brand-accent
        content = content.replace('#4ade80', '#60a5fa') # blue hover
        content = content.replace('rgba(34, 197, 94', 'rgba(59, 130, 246') # rgba equivalent
        
        # Fix index3.html links
        content = content.replace('href="../index3.html"', 'href="../index.html"')
        
        # Fix active state in Navigation for specific pages if needed
        # (index.html has none active by default except maybe in some subpages wait, index has none with border-b)
        # We can add active state based on filename
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"No changes in {filename}")

if __name__ == "__main__":
    update_pages()
