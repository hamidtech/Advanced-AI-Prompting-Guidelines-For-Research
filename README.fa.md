# راهنمای پیشرفتهٔ پرامپت‌نویسی برای پژوهش

از قالب پرامپت تا گردش‌کار پژوهشی مبتنی بر شواهد — **نسخهٔ ۲.۰**.

[English](README.md) · [مجوز MIT](LICENSE) · [مشارکت](CONTRIBUTING.md)

از کاری شروع کنید که می‌خواهید انجام دهید. برای شروع نیازی به برنامه‌نویسی، JSON، حساب API یا عامل خودمختار ندارید. پیشنهاد مدل موضوعی برای بررسی است؛ دلیل تازگی علمی نیست.

## لایهٔ اول: شروع پژوهش

| نیاز شما | نقطهٔ شروع |
|---|---|
| هنوز نمی‌دانم به چه چیزی علاقه دارم | [کشف علاقه](catalog/prompts/interest-discovery.fa.md) |
| موضوع پایان‌نامه می‌خواهم | [ایده‌پردازی پایان‌نامه](catalog/prompts/thesis-brainstormer.fa.md) |
| زاویه‌ای برای مقاله می‌خواهم | [کاوش زاویهٔ مقاله](catalog/prompts/article-angle-explorer.fa.md) |
| ایدهٔ کتاب دارم | [کاوش ایدهٔ کتاب](catalog/prompts/book-concept-explorer.fa.md) |
| عنوانم نیاز به اصلاح دارد | [اصلاح عنوان](catalog/prompts/title-refiner.fa.md) |

قالب را باز کنید، مواردی را که می‌دانید جایگزین کنید و برای بقیه «نامشخص» بنویسید. متن کامل پرامپت را به ابزار مناسب بدهید. فرض‌ها و حد شواهد را بخواهید و ادعاهای واقعی را پیش از استفاده با منبع اصلی بررسی کنید.

## لایهٔ دوم: گردش‌کار قابل دفاع

- [از علاقه تا عنوان](catalog/workflows/topic-to-title.fa.md)
- [اعتبارسنجی موضوع](catalog/workflows/topic-validation.fa.md)
- [بررسی شکاف پژوهشی](catalog/workflows/gap-verification.fa.md)
- [از مقاله تا شواهد](catalog/workflows/paper-to-evidence.fa.md)

[قرارداد پرامپت](docs/foundations/prompt-contract.fa.md)، [تعامل با مدل](docs/foundations/modern-interaction.fa.md)، [راهنماهای رشته‌ای](docs/disciplines/) و [درستکاری پژوهشی](docs/integrity/) را ببینید. قابلیت ابزارها با تاریخ بررسی در [راهنمای ابزارها](docs/tools/) آمده است.

## لایهٔ سوم: ساختار، خودکارسازی و ارزیابی

[شِماها](catalog/schemas/)، [مثال‌های ساختگی آموزشی](examples/README.fa.md)، [خودکارسازی اختیاری](automation/README.fa.md) و [پروتکل ارزیابی](evaluation/README.fa.md) برای کاربران فنی‌اند. سی سناریوی دوزبانه آماده شده است؛ مقایسهٔ تجربی مدل‌ها **در انتظار اجرا** است و ادعای بهبود اندازه‌گیری‌شده نداریم.

## ده پرامپت

| شناسه | الگوی فارسی | English |
|---|---|---|
| RP-01 | [ایده‌پردازی متمرکز پایان‌نامه](catalog/prompts/thesis-brainstormer.fa.md) | [Focused Thesis Brainstormer](catalog/prompts/thesis-brainstormer.md) |
| RP-02 | [کاوش زاویه‌های مقاله](catalog/prompts/article-angle-explorer.fa.md) | [Article Angle Explorer](catalog/prompts/article-angle-explorer.md) |
| RP-03 | [کاوش ایدهٔ کتاب](catalog/prompts/book-concept-explorer.fa.md) | [Book Concept Explorer](catalog/prompts/book-concept-explorer.md) |
| RP-04 | [عنوان‌سازی میان‌رشته‌ای](catalog/prompts/cross-disciplinary-title.fa.md) | [Cross-Disciplinary Research Title Maker](catalog/prompts/cross-disciplinary-title.md) |
| RP-05 | [تولید فرضیهٔ شکاف پژوهشی](catalog/prompts/gap-hypothesis.fa.md) | [Research Gap Hypothesis Generator](catalog/prompts/gap-hypothesis.md) |
| RP-06 | [کشف علاقهٔ پژوهشی](catalog/prompts/interest-discovery.fa.md) | [Research Interest Discovery](catalog/prompts/interest-discovery.md) |
| RP-07 | [نقد موضوع پژوهش](catalog/prompts/topic-critic.fa.md) | [Research Topic Critic](catalog/prompts/topic-critic.md) |
| RP-08 | [اصلاح عنوان پژوهش](catalog/prompts/title-refiner.fa.md) | [Research Title Refiner](catalog/prompts/title-refiner.md) |
| RP-09 | [ترکیب پیشینه بر پایهٔ شواهد](catalog/prompts/literature-synthesizer.fa.md) | [Evidence-Grounded Literature Synthesizer](catalog/prompts/literature-synthesizer.md) |
| RP-10 | [ارزیابی امکان اجرای پژوهش](catalog/prompts/feasibility-assessor.fa.md) | [Research Feasibility Assessor](catalog/prompts/feasibility-assessor.md) |

## مهاجرت و نگهداری

پنج فایل اصلی بدون تغییر بایت‌ها در [آرشیو تاریخی](legacy/2024-gpt-4o/) حفظ شده‌اند. نشانی فایل‌های ریشه برقرار است؛ برای عنوان‌بخش‌های قدیمی ممکن است به آرشیو نیاز داشته باشید. [راهنمای مدرن](ModernResearchPrompting.md) که قبلاً وجود نداشت اکنون ایجاد شده است. [ممیزی و مهاجرت](docs/audit-and-migration.md)، [تغییرات](CHANGELOG.md)، [اعتبارسنجی](automation/README.fa.md) و [گزارش تحویل](docs/delivery-report.md).

قابلیت محصولات تصویری از زمان بررسی‌اند، نه تضمین دسترسی یا قیمت. پوشش منابع، کیفیت فارسی، سیاست انتشار و اجازهٔ استفاده از داده باید در هر پروژه بررسی شوند. مسئولیت نهایی کار با پژوهشگر است.
