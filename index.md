<!-- CSS стили для красоты (можно вставлять прямо в MD) -->
<style>
  /* Стиль для круглой аватарки */
  .avatar-container {
    text-align: center;
    margin-bottom: 20px;
  }
  .avatar-img {
    width: 200px;       /* Размер круга */
    height: 200px;
    object-fit: cover;  /* Чтобы фото не сплющило, а красиво обрезало */
    border-radius: 50%; /* Делает круг */
    border: 4px solid #fff; /* Белая рамочка */
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
  }

  /* Стиль для контейнера с прокруткой */
  .scroll-box {
    max-height: 500px; /* Максимальная высота блока */
    overflow-y: auto;  /* Вертикальная прокрутка, если контент длиннее */
    border: 1px solid #444;
    padding: 10px;
    background-color: #f6f8fa; /* Светлый фон для контраста, если тема темная */
    color: #333;
    border-radius: 5px;
  }
  
  /* Убираем лишние отступы у iframe */
  iframe {
    border: none;
    width: 100%;
  }
</style>

<!-- БЛОК АВАТАРКИ -->
<div class="avatar-container">
  <!-- Замени assets/avatar.jpg на путь к твоему фото -->
  <img src="assets/avatar.jpg" class="avatar-img" alt="Мое фото">
</div>

# Привет! Я Тимур.
Здесь собраны мои проекты по анализу данных и разработке.

---

## 🚀 Проект 1: FinBest
**Анализ финансовых данных и Ad-Hoc отчетность.**

Этот проект посвящен глубокому анализу финансовых показателей. Включает в себя парсинг данных, обработку и визуализацию связей.

### 🕸 Интерактивный граф связей (Pyvis)
Ниже представлен интерактивный граф. Вы можете приближать, отдалять и перетаскивать узлы.

<!-- Вставка Pyvis HTML через iframe -->
<div style="height: 600px; border: 1px solid #ccc;">
    <iframe src="html_exports/pyvis_graph.html" height="100%"></iframe>
</div>

<br>

### 📊 Ad-Hoc Анализ и Ноутбук
Я провел исследовательский анализ данных. Ниже можно развернуть полный отчет из Jupyter Notebook.

<!-- СВОРАЧИВАЕМЫЙ БЛОК (ACCORDION) -->
<details>
  <summary style="cursor: pointer; font-size: 1.2em; font-weight: bold;">
    📂 Нажми, чтобы развернуть/свернуть полный анализ (Jupyter Notebook)
  </summary>
  
  <br>
  
  <!-- БЛОК С ПРОКРУТКОЙ -->
  <div class="scroll-box">
    <!-- Вставляем экспортированный HTML ноутбука -->
    <!-- height можно менять -->
    <iframe src="html_exports/ad_hoc_analysis.html" height="1000px"></iframe>
  </div>
  
  <p><i>*Ноутбук можно прокручивать внутри этого окна.</i></p>
</details>

<br>

**Ссылки:**
* [Репозиторий FinBest на GitHub](https://github.com/timurfays/FinBest)

---

## 🎓 Курсовые работы

Здесь представлены мои академические проекты. Полные тексты и данные доступны на Яндекс.Диске, а здесь — демонстрация результатов.

### Курсовая №1: Название темы
Описание того, что было сделано. Какие алгоритмы применялись.

<!-- Картинка или Гифка -->
![Демонстрация работы](assets/course_1.gif)

<details>
  <summary>📉 Показать дополнительные графики (свернуть/развернуть)</summary>
  <img src="assets/finbest_1.png" alt="График 1">
  <img src="assets/another_graph.png" alt="График 2">
</details>

📥 **[Скачать/Читать полную версию на Яндекс.Диске](ССЫЛКА_НА_ЯНДЕКС_ДИСК)**

---

### Курсовая №2: Название темы
Краткое описание второй курсовой.

![Результат работы](assets/course_2_image.png)

📥 **[Скачать/Читать полную версию на Яндекс.Диске](ССЫЛКА_НА_ЯНДЕКС_ДИСК)**

---

### Контакты
* Telegram: @...
* Email: ...
