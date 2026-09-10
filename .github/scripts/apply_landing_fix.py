from pathlib import Path
import re

p = Path('src/components/ServiceLanding.tsx')
s = p.read_text(encoding='utf-8-sig')

# Remove online-estimator buttons from the four dedicated service landing pages.
s = re.sub(r'''\n\s*<button\s+\n\s*onClick=\{onOpenEstimator\}\s*\n\s*className="bg-transparent border border-white/30[\s\S]*?</button>''', '', s)
s = re.sub(r'''\n\s*<button\s+\n\s*onClick=\{onOpenEstimator\}\s*\n\s*className="bg-transparent border border-white/40[\s\S]*?</button>''', '', s)

# Rename yellow CTA.
s = s.replace('تلفن رزرو: {data.heroPhone}', 'تلفن تماس: {data.heroPhone}')

# Transport copy should cover both moving and van/Nissan services.
s = s.replace('fullStoryTitle: "وانت بار تلفنی و نیسان بار اسپاب چی",', 'fullStoryTitle: "اسباب‌کشی، وانت بار و نیسان بار اسپاب چی",')
old_transport = 'حمل بار سبک و نیمه‌سنگین نیازمند چابکی و دقت عمل بالاست. اگر نیاز به حمل یک یا چند قلم بار دارید، با پرداخت نیمی از هزینه کامیون‌های اسباب‌کشی می‌توانید از سرویس وانت و نیسان تلفنی ما برخوردار شوید. خودروهای ما همراه با رانندگانی ماهر و پتوهای مخمل مخصوص ضربه‌گیر، بار شما را به کمال ایمنی جابجا می‌نمایند. وقت‌شناسی بالا و حضور کمتر از ربع ساعت از ویژگی‌های بارز اتوبار اسپاب چی است.'
new_transport = 'اسپاب چی خدمات اسباب‌کشی و حمل اثاثیه منزل را در کنار سرویس وانت بار و نیسان بار برای بارهای سبک و نیمه‌سنگین ارائه می‌دهد. متناسب با حجم بار و نوع جابه‌جایی، خودروی مناسب و نیروی موردنیاز هماهنگ می‌شود تا اثاثیه و بار با دقت و نظم جابه‌جا شوند. برای هماهنگی اسباب‌کشی، حمل اثاثیه، وانت یا نیسان می‌توانید مستقیماً با اسپاب چی تماس بگیرید.'
s = s.replace(old_transport, new_transport)

# Remove unsupported insurance claims.
s = s.replace('جهت آسایش خاطر بدون تزلزل شما عزیزان، بیش از ۹۹ درصد از خدمات حمل و ترابری سبک ما به صورت کاملاً رایگان تحت بیمه کالا ثبت می‌گردند.', 'در تمام مراحل حمل، تلاش تیم اسپاب چی بر جابه‌جایی منظم و با دقت اثاثیه و بار و انتخاب خودروی متناسب با نوع بار است.')
s = s.replace('99درصد از مشتریان ما ،به صورت رایگان بیمه شده اند.', 'بسته‌بندی و جابه‌جایی با تمرکز بر دقت، نظم و کاهش احتمال آسیب به وسایل انجام می‌شود.')
s = s.replace('کلیه اموال و اثاثیه منزل شما بر اساس قرارداد رسمی شرکت تحت پوشش بیمه دولتی کامل قرار می‌گیرند.', 'شرایط نگهداری و جزئیات خدمات انبار پیش از تحویل وسایل با مشتری هماهنگ و شفاف‌سازی می‌شود.')

# Replace old brand references.
s = s.replace('شرکت ظریف بار', 'شرکت اسپاب چی').replace('اتوبار ظریف بار', 'اتوبار اسپاب چی').replace('ظریف بار', 'اسپاب چی')

# Persisted admin settings may still contain old copy, so enforce corrected display values.
marker = "    const activeVideoUrl = loadedVideoUrl || data.videoUrl;"
guard = '''    if (slug === 'transport') {
      data.fullStoryTitle = "اسباب‌کشی، وانت بار و نیسان بار اسپاب چی";
      data.fullStoryDesc = "اسپاب چی خدمات اسباب‌کشی و حمل اثاثیه منزل را در کنار سرویس وانت بار و نیسان بار برای بارهای سبک و نیمه‌سنگین ارائه می‌دهد. متناسب با حجم بار و نوع جابه‌جایی، خودروی مناسب و نیروی موردنیاز هماهنگ می‌شود تا اثاثیه و بار با دقت و نظم جابه‌جا شوند. برای هماهنگی اسباب‌کشی، حمل اثاثیه، وانت یا نیسان می‌توانید مستقیماً با اسپاب چی تماس بگیرید.";
      data.topics = data.topics.map((topic, index) => index === 2
        ? { ...topic, title: "حمل با دقت و مسئولیت‌پذیری", desc: "در تمام مراحل حمل، تلاش تیم اسپاب چی بر جابه‌جایی منظم و با دقت اثاثیه و بار و انتخاب خودروی متناسب با نوع بار است." }
        : { ...topic, title: topic.title?.replace(/ظریف بار/g, 'اسپاب چی'), desc: topic.desc?.replace(/ظریف بار/g, 'اسپاب چی') });
    }
    if (slug === 'storage') {
      data.pillars = data.pillars.map((pillar, index) => index === 2
        ? { ...pillar, title: "شرایط شفاف نگهداری", desc: "شرایط نگهداری و جزئیات خدمات انبار پیش از تحویل وسایل با مشتری هماهنگ و شفاف‌سازی می‌شود." }
        : pillar);
      data.topics = data.topics.map((topic) => ({ ...topic, title: topic.title?.replace(/ظریف بار/g, 'اسپاب چی'), desc: topic.desc?.replace(/ظریف بار/g, 'اسپاب چی') }));
    }
    if (slug === 'packing') {
      data.materials = data.materials.map((item, index) => index === 3
        ? { ...item, title: "بسته‌بندی و حمل با دقت", desc: "بسته‌بندی و جابه‌جایی با تمرکز بر دقت، نظم و کاهش احتمال آسیب به وسایل انجام می‌شود.", badge: "دقت در جابه‌جایی" }
        : item);
    }
'''
if guard not in s:
    s = s.replace(marker, guard + marker)

p.write_text(s, encoding='utf-8')
