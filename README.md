# 📅 Monthly Challenges (Ամսական Մարտահրավերներ)

> Դինամիկ վեբ-հավելված՝ կառուցված Python-ի և Django ֆրեյմվորքի հիման վրա, որը թույլ է տալիս դիտել յուրաքանչյուր ամսվա համար նախատեսված նպատակներն ու մարտահրավերները (challenges):

---

## 📌 Նախագծի մասին (About)

**Monthly Challenges** նախագիծը Django-ի հիմնարար հնարավորությունները ցուցադրող ինտերակտիվ վեբ-հարթակ է։ Այն ներկայացնում է տարվա բոլոր ամիսների ցանկը, որոնցից յուրաքանչյուրին սեղմելիս բացվում է տվյալ ամսվա համար սահմանված հատուկ առաջադրանքը կամ մարտահրավերը։

Հավելվածում իրականացված են Django-ի ճարտարապետության կարևոր սկզբունքները՝ դինամիկ երթուղավորում (routing), տվյալների վերահղում (redirection), շաբլոնների ժառանգում (template inheritance) և ստատիկ ֆայլերի (CSS/JS) ճիշտ ինտեգրում։

---

## ✨ Հիմնական հնարավորությունները (Features)

- **Դինամիկ URL Routing** — Ամիսների էջերի ավտոմատ գեներացում ինչպես ամսվա անունով (օր.՝ `/challenges/january`), այնպես էլ ամսվա հերթական թվով (օր.՝ `/challenges/1`):
- **Խելացի Վերահղում (Redirects)** — Ամսվա համարով մուտք գործելիս համակարգը `reverse()` մեթոդի օգնությամբ ավտոմատ վերահղում է համապատասխան անվանական էջին։
- **Շաբլոնների համակարգ (Django Template Engine)** — Մաքուր և մոդուլային կառուցվածք՝ բազային շաբլոնների (`base.html`), բլոկների (`{% block %}`) և պայմանական ցուցադրման կիրառմամբ։
- **Սխալների կառավարում (Custom 404)** — Գոյություն չունեցող ամիս մուտքագրելու դեպքում օգտատիրոջը ցուցադրվում է համապատասխան ծանուցում (404 Not Found):
- **Ժամանակակից Դիզայն (Static Assets)** — Ոճավորված CSS ֆայլեր և կոկիկ ինտերֆեյս։

---

## 🛠 Օգտագործված տեխնոլոգիաները (Tech Stack)

- **Backend:** Python 3.x, Django
- **Frontend:** HTML5, CSS3, Django Template Language (DTL)
- **Database:** SQLite3

---

## 📂 Նախագծի Կառուցվածքը (Project Structure)

monthly-challenges/

│

├── amisner/                # Django նախագծի հիմնական կոնֆիգուրացիոն պանակը

│   ├── settings.py         # Կարգավորումներ (Apps, Templates, Static)

│   ├── urls.py             # Գլխավոր URL կանոնները

│   └── wsgi.py / asgi.py

│

├── challenges/             # Հիմնական հավելվածը (App)

│   ├── views.py            # Լոգիկա (ամիսների մշակում, redirect-ներ)

│   ├── urls.py             # Հավելվածի երթուղիները

│   └── apps.py

│

├── templates/              # Ընդհանուր HTML շաբլոններ (ներառյալ base.html, 404.html)

├── static/                 # Ստատիկ ֆայլեր (CSS ոճեր, պատկերներ)

├── manage.py               # Django-ի ղեկավարման սկրիպտը

└── db.sqlite3              # Տվյալների բազա



🚀 Տեղադրում և Գործարկում (Installation & Setup)
Նախագիծը ձեր համակարգչում տեղային (locally) աշխատեցնելու համար հետևեք հետևյալ քայլերին.
1. Կլոնավորել ռեպոզիտորիան
git clone https://github.com/MarkosyanShooshan/monthly-challanges.git
cd monthly-challanges
2. Ստեղծել և ակտիվացնել վիրտուալ միջավայրը (Virtual Environment)
Windows:
python -m venv venv
venv\Scripts\activate
macOS / Linux:
python3 -m venv venv
source venv/bin/activate
3. Տեղադրել Django-ն
pip install django
4. Կատարել միգրացիաները (Migrations)
python manage.py migrate
5. Գործարկել սերվերը
python manage.py runserver
Բրաուզերում բացեք հետևյալ հասցեն՝
👉 http://127.0.0.1:8000/challenges/

🔮 Հետագա Բարելավումներ (Future Roadmap)

Մարտահրավերների պահպանում Django Models-ի միջոցով (բազայում)

Django Admin Panel-ի միջոցով մարտահրավերների ավելացում և խմբագրում

Օգտատերերի գրանցում և մուտք (User Authentication)

Մարտահրավերները կատարված նշելու հնարավորություն (Progress Tracker)

👤 Հեղինակ (Author)
Շուշան Մարկոսյան — https://github.com/MarkosyanShooshan
