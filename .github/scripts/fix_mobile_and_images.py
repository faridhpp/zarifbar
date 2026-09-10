from pathlib import Path

# 1) Hide brand text next to logo on mobile; show from md upward.
h = Path('src/components/Header.tsx')
s = h.read_text(encoding='utf-8-sig')
old = '''          <div>\n            <span className="text-sm md:text-xl lg:text-2xl font-black text-gray-900 tracking-tight block whitespace-nowrap">\n              اسپاب چی <span className="hidden md:inline-block text-purple-600 font-medium text-xs md:text-sm">{tagline || 'اتوبار مدرن'}</span>\n            </span>\n          </div>'''
new = '''          <div className="hidden md:block">\n            <span className="text-sm md:text-xl lg:text-2xl font-black text-gray-900 tracking-tight block whitespace-nowrap">\n              اسپاب چی <span className="hidden md:inline-block text-purple-600 font-medium text-xs md:text-sm">{tagline || 'اتوبار مدرن'}</span>\n            </span>\n          </div>'''
if old in s:
    s = s.replace(old, new)
h.write_text(s, encoding='utf-8')

# 2) Sanitize landing images loaded from persisted settings: never render Unsplash URLs.
p = Path('src/components/ServiceLanding.tsx')
s = p.read_text(encoding='utf-8-sig')
marker = "    const activeVideoUrl = loadedVideoUrl || data.videoUrl;"
code = '''    const sanitizeImageUrl = (url?: string) => {\n      if (!url) return '';\n      const value = String(url).trim();\n      if (/unsplash\\.com/i.test(value)) return '';\n      return value;\n    };\n    data.heroImage = sanitizeImageUrl(data.heroImage);\n    data.fullStoryImage = sanitizeImageUrl(data.fullStoryImage);\n    data.materials = data.materials.map((item) => ({ ...item, image: sanitizeImageUrl(item.image) }));\n'''
if code not in s:
    s = s.replace(marker, code + marker)
p.write_text(s, encoding='utf-8')
