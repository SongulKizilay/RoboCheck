# RoboCheck

`RoboCheck`, belirtilen alt alan adları için `robots.txt` dosyalarını kontrol eden basit bir Python betiğidir.

## Kullanım

1. `robots.txt` dosyasını kontrol etmek istediğiniz alt alan adlarını içeren bir metin dosyası oluşturun. Her alt alan adını ayrı bir satırda belirtin. Örnek bir `subdomains.txt` dosyası şu şekilde olabilir:

https://link.dev.x.immutable.com https://support.immutable.com https://example.com


2. `RoboCheck` dosyasını indirin ve çalıştırın:

```bash
python3 RoboCheck.py
RoboCheck, alt alan adlarını tek tek kontrol edecek ve her biri için robots.txt dosyasını çıktı olarak verecektir.
Özellikler
curl komutunu kullanarak alt alan adlarının robots.txt dosyalarını kontrol eder.
Başarılı bir şekilde kontrol edilen alt alan adları için robots.txt içeriğini ve ayrıntıları çıktı olarak verir.
Başarısız olan alt alan adları için hata mesajını ve ayrıntıları çıktı olarak verir.
Örnek Çıktı
Subdomain: https://link.dev.x.immutable.com

# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:

--------------------------------------------------
Subdomain: https://support.immutable.com

User-agent: *
Disallow: /not-authorized
Disallow: /not-found
Disallow: /[helpCenterIdentifier]/
Crawl-delay: 1

--------------------------------------------------
Subdomain: https://example.com

Hata: curl: (6) Could not resolve host: example.com
Yukarıdaki örnekte, https://link.dev.x.immutable.com ve https://support.immutable.com alt alan adlarının robots.txt dosyaları başarılı bir şekilde kontrol edilmiştir. İkinci alt alan adı için robots.txt içeriği ve ayrıntıları çıktı olarak verilmiştir. https://example.com alt alan adı ise başarısız olmuş ve hata mesajı verilmiştir.

Bu şekilde RoboCheck betiği, belirtilen alt alan adlarının robots.txt dosyalarını kontrol etmek için kullanılabilir.

