from pathlib import Path

p = Path('src/components/Header.tsx')
s = p.read_text(encoding='utf-8-sig')
old = '''          <div>\n            <span className="text-sm md:text-xl lg:text-2xl font-black text-gray-900 tracking-tight block whitespace-nowrap">\n              اسپاب چی <span className="hidden md:inline-block text-purple-600 font-medium text-xs md:text-sm">{tagline || 'اتوبار مدرن'}</span>\n            </span>\n          </div>'''
new = '''          <div className="hidden md:block">\n            <span className="text-sm md:text-xl lg:text-2xl font-black text-gray-900 tracking-tight block whitespace-nowrap">\n              اسپاب چی <span className="hidden md:inline-block text-purple-600 font-medium text-xs md:text-sm">{tagline || 'اتوبار مدرن'}</span>\n            </span>\n          </div>'''
if old not in s:
    raise SystemExit('Target header branding block not found')
p.write_text(s.replace(old, new, 1), encoding='utf-8')
