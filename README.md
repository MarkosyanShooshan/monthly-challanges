# 📅 Monthly Challenges (Django Web Application)

[ 🇬🇧 English Version ](#english) | [ 🇦🇲 Հայերեն Տարբերակ ](#armenian)


<span id="english"></span>
## 🇬🇧 English

> A dynamic web application built with Python and the Django framework, designed to track and view monthly goals, habits, and challenges throughout the year.

### 📌 About the Project

**Monthly Challenges** is an interactive web platform demonstrating foundational Django concepts. The app presents an overview of all 12 months, where selecting any month reveals a tailored task or challenge planned for that specific period.

The project highlights key architectural features of Django, including dynamic URL routing with type converters, reverse URL resolution, template inheritance, custom error handling (404), and static asset management.

### ✨ Key Features

- **Dynamic URL Routing:** Dynamic route handling supporting both month names (e.g., `/challenges/january`) and numerical indices (e.g., `/challenges/1`).
- **Smart Redirection:** Automatically redirects numeric month routes to their corresponding canonical month names using Django's `reverse()` utility.
- **Django Template Engine (DTL):** Clean and maintainable layout using template inheritance (`base.html`), template blocks (`{% block %}`), and conditional rendering.
- **Custom 404 Error Handling:** User-friendly fallback pages for invalid or non-existent months.
- **Static Assets Integration:** Clean, responsive UI powered by custom CSS styling.

### 🛠 Tech Stack

- **Backend:** Python 3.x, Django
- **Frontend:** HTML5, CSS3, Django Template Language (DTL)
- **Database:** SQLite3

### 📂 Project Structure

monthly-challenges/
│

├── amisner/  # Django project configuration folder

│   ├── settings.py         # Project settings

│   ├── urls.py             # Root URL routing

│   └── wsgi.py / asgi.py

│

├── challenges/             # Core application

│   ├── views.py            # Business logic (month handlers, redirects)

│   ├── urls.py             # App-level routing

│   └── apps.py

│

├── templates/              # HTML templates (base.html, 404.html, challenges/)

├── static/                 # Static assets (CSS stylesheets)

├── manage.py               # Django management script







🚀 Installation & Setup
Follow these steps to run the project locally on your machine:
Clone the repository:
git clone https://github.com/MarkosyanShooshan/monthly-challanges.git
cd monthly-challanges
Create and activate a virtual environment:
Windows:
python -m venv venv
venv\Scripts\activate
macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install django
(or pip install -r requirements.txt if available)
Apply database migrations:
python manage.py migrate
Run the development server:
python manage.py runserver
View the application:
Open your browser and navigate to:
👉 http://127.0.0.1:8000/challenges/



🔮 Future Roadmap

Store challenges in a database using Django Models

Django Admin integration for adding and editing challenges dynamically

User authentication and personal challenge completion tracking

Progress dashboard with completion stats








<span id="armenian"></span>
🇦🇲 Հայերեն
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


