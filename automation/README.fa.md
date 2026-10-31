# خودکارسازی اختیاری

[English](README.md)

با Python 3.11 یا بالاتر، از ریشهٔ مخزن وابستگی‌های `requirements-dev.txt` را نصب کنید؛ سپس `python automation/scripts/validate.py` و `python -m unittest discover -s automation/scripts -p 'test_*.py'` را اجرا کنید.

پس از نصب وابستگی، بررسی‌ها آفلاین‌اند و کلید API لازم ندارند. این آزمون‌ها ساختار و مستندات را بررسی می‌کنند؛ مدل را اجرا نمی‌کنند و اعتبار علمی را اثبات نمی‌کنند. متن تاریخی از قواعد جدید قالب‌بندی معاف است اما در صورت دسترسی به تاریخچه، بایت‌های آن با کامیت مبنا تطبیق داده می‌شود. [پروتکل ارزیابی](../evaluation/README.fa.md) و [مدیریت خروجی](examples/structured-output.md).
