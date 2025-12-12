---
layout: default
title: Тимур Файз | Портфолио
---

<!-- ==================== ДИЗАЙН (CSS) ==================== -->
<style>
  /* 1. Глобальные настройки */
  body {
    background-color: #f4f7f6; /* Чуть сероватый фон, не режет глаз */
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #333;
    line-height: 1.6;
    margin: 0;
    padding: 0;
  }
  
  /* Контейнер, чтобы текст не разъезжался на широких экранах */
  .main-content {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
  }

  /* 2. Заголовки */
  h1, h2, h3 {
    font-family: "Georgia", "Times New Roman", serif; /* Академический стиль */
    color: #2c3e50;
  }
  h1 { font-size: 2.5em; margin-bottom: 0.2em; border: none; }
  h2 { 
    margin-top: 40px; 
    border-bottom: 2px solid #3498db; /* Синяя линия под заголовком */
    display: inline-block;
    padding-bottom: 5px;
  }

  /* 3. Карточки (Белые блоки с тенью) */
  .card {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05); /* Легкая тень */
    padding: 30px;
    margin-bottom: 30px;
    transition: transform 0.2s;
  }
  .card:hover {
    transform: translateY(-2px); /* Чуть всплывает при наведении */
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
  }

  /* 4. Аватар и Шапка */
  .profile-header {
    text-align: center;
    margin-bottom: 50px;
  }
  .avatar {
    width: 220px;
    height: 220px;
    object-fit: cover;
    border-radius: 50%;
    border: 6px solid #fff;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
  }
  .tagline {
    font-size: 1.2em;
    color: #7f8c8d;
    font-style: italic;
  }

  /* 5. Галерея (Горизонтальный скролл) */
  .gallery-container {
    display: flex;
    overflow-x: auto;
    gap: 15px;
    padding-bottom: 15px;
    scrollbar-width: thin;
  }
  /* Красивый скроллбар */
  .gallery-container::-webkit-scrollbar { height: 8px; }
  .gallery-container::-webkit-scrollbar-thumb { background: #bdc3c7; border-radius: 4px; }
  
  .gallery-item {
    height: 220px; /* Фиксированная высота */
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: transform 0.2s;
  }
  .gallery-item:hover { transform: scale(1.02); }

  /* 6. Сворачиваемые блоки (Details) */
  details {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 10px 15px;
    margin: 15px 0;
  }
  summary {
    font-weight: bold;
    cursor: pointer;
    color: #2980b9;
    outline: none;
  }
  summary:hover { color: #1c5980; }
  
  /* Цитата внутри details */
  .doc-snippet {
    margin-top: 15px;
    padding-left: 15px;
    border-left: 4px solid #2980b9;
    color: #555;
    font-size: 0.9em;
  }

  /* 7. Iframe (для графиков и ноутбуков) */
  .frame-wrapper {
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    background: #fff;
  }

  /* Кнопка */
  .btn {
    display: inline-block;
    background-color: #2980b9;
    color: #fff !important;
    padding: 10px 20px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 10px;
  }
  .btn:hover { background-color: #3498db; }
</style>

<!-- ==================== КОНТЕНТ ==================== -->

<div class="main-content">

  <!-- ШАПКА -->
  <div class="profile-header">
    <img src="assets/avatar.jpg" class="avatar" alt="Тимур Файз">
    <h1>Тимур Файз</h1>
    <p class="tagline">Data Engineer | Researcher</p>
    <p>От алгоритмического фундамента МФТИ до Big Data архитектуры в СПбГУ.</p>
  </div>

  <!-- БЛОК: ИСТОРИЯ (О себе) -->
  <div class="card">
    <h2>🗺 Моя история</h2>
    <p>
      Это портфолио — история моего профессионального пути. Я начал в <b>МФТИ</b>, где вместо того, чтобы просто сдавать лабораторные, я усложнял себе задачи, визуализируя алгоритмы на C++. Там я понял важность архитектуры.
    </p>
    <p>
      В <b>СПбГУ</b> я применил этот инженерный подход к данным. Так родился проект <b>FinBest</b> — попытка создать не просто учебный скрипт, а полноценный промышленный конвейер (Pipeline), который учитывает реальные законы (ФЗ-152) и работает с Big Data.
    </p>
  </div>

  <!-- БЛОК: FINBEST -->
  <div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <h2>🚀 Проект: FinBest</h2>
      <span style="color:#7f8c8d; font-size:0.9em;">Stack: Airflow, Spark, dbt</span>
    </div>

    <p><b>Практическая реализация EtLT-конвейера и графового анализа.</b></p>
    
    <!-- 1. Выдержка из документа -->
    <details>
      <summary>📄 Описание задачи и Цель (Выдержка из курсовой)</summary>
      <div class="doc-snippet">
        <p><b>Актуальность:</b> Необходимость обработки транзакций с учетом ФЗ-152 (персональные данные) и ФЗ-115 (анти-отмывание) на российских облачных платформах.</p>
        <p><b>Решение:</b> Гибридная архитектура EtLT. Маскирование данных происходит ДО загрузки в облако, а тяжелая аналитика — внутри хранилища.</p>
      </div>
    </details>

    <!-- 2. Галерея -->
    <p><i>📸 Галерея (прокрутите вправо): архитектура, интерфейсы, дашборды.</i></p>
    <div class="gallery-container">
      <img src="assets/architecture_scheme.png" class="gallery-item" alt="Схема">
      <img src="assets/airflow_dag.png" class="gallery-item" alt="Airflow">
      <img src="assets/superset_dashboard.png" class="gallery-item" alt="Superset">
      <img src="assets/graph_viz.png" class="gallery-item" alt="Граф">
    </div>

    <br>

    <!-- 3. Интерактивный граф -->
    <h3>🕸 Интерактивный граф связей</h3>
    <p>Результат работы алгоритма кластеризации клиентов (GraphFrames). Граф живой — узлы можно двигать.</p>
    <div class="frame-wrapper" style="height: 500px;">
      <iframe src="html_exports/pyvis_graph.html" width="100%" height="100%" style="border:none;"></iframe>
    </div>

    <br>

    <!-- 4. Ноутбук -->
    <details>
      <summary>📓 Открыть полный код анализа (Jupyter Notebook)</summary>
      <br>
      <div class="frame-wrapper" style="height: 800px;">
        <iframe src="html_exports/ad_hoc_analysis.html" width="100%" height="100%" style="border:none;"></iframe>
      </div>
    </details>

    <br>
    <a href="ССЫЛКА_НА_ЯНДЕКС_ДИСК" class="btn">📥 Скачать полную документацию (PDF)</a>
  </div>

  <!-- БЛОК: МФТИ -->
  <div class="card">
    <h2>🏛 МФТИ: Визуализация алгоритмов</h2>
    <p>Мой первый серьезный проект. Визуализатор поиска пути на графах, написанный на C++ с использованием SFML.</p>

    <details>
      <summary>📄 Техническое описание</summary>
      <div class="doc-snippet">
        Реализация алгоритма Дейкстры с использованием паттернов проектирования. Позволяет визуализировать процесс обхода графа в реальном времени.
      </div>
    </details>

    <div class="gallery-container">
      <img src="assets/sfml_demo.gif" class="gallery-item" alt="Demo">
      <img src="assets/mipt_photo1.jpg" class="gallery-item" alt="MIPT">
      <img src="assets/cpp_code.png" class="gallery-item" alt="Code">
    </div>
  </div>

  <!-- ПОДВАЛ -->
  <div style="text-align:center; margin-top:50px; color:#7f8c8d;">
    <p>Готов к научному сотрудничеству и сложным инженерным задачам.</p>
    <p>
      <a href="https://t.me/твой_ник" style="color:#2980b9; text-decoration:none;">Telegram</a> • 
      <a href="mailto:твоя_почта" style="color:#2980b9; text-decoration:none;">Email</a>
    </p>
  </div>

</div>
