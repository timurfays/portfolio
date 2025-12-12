---
layout: default
title: Тимур Файз | Портфолио
---

<!-- ==================== СТИЛИ (CSS) ==================== -->
<style>
  /* Общие настройки */
  body {
    background-color: #f4f6f8;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #2c3e50;
    line-height: 1.6;
    margin: 0; padding: 0;
  }
  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
  }

  /* Типографика */
  h1 { font-size: 2.2em; margin-bottom: 0.2em; color: #1a202c; }
  h2 { border-bottom: 2px solid #3182ce; padding-bottom: 5px; display: inline-block; margin-top: 0; }
  h3 { margin-bottom: 10px; color: #2d3748; }
  
  /* Карточки */
  .card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
    padding: 30px;
    margin-bottom: 30px;
  }

  /* Шапка профиля */
  .profile-header { text-align: center; margin-bottom: 40px; }
  .avatar {
    width: 180px; height: 180px; object-fit: cover;
    border-radius: 50%; border: 5px solid #fff;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  }
  .bio-text { font-size: 1.1em; color: #4a5568; max-width: 700px; margin: 10px auto; }

  /* Навыки (Badges) */
  .tech-badge {
    display: inline-block;
    background-color: #ebf8ff; color: #2b6cb0;
    border: 1px solid #bee3f8;
    padding: 4px 10px; border-radius: 15px;
    font-size: 0.85em; font-weight: 600;
    margin: 0 5px 5px 0;
  }
  .tech-badge.core { background-color: #e6fffa; color: #234e52; border-color: #b2f5ea; } /* Зеленые для базы */

  /* Галерея (Скролл) */
  .gallery-scroll {
    display: flex; overflow-x: auto; gap: 15px; padding: 10px 0;
    scrollbar-width: thin;
  }
  .gallery-item {
    height: 200px; border-radius: 6px; border: 1px solid #cbd5e0;
    flex-shrink: 0;
  }

  /* Сворачиваемые блоки */
  details {
    background: #f7fafc; border: 1px solid #edf2f7;
    border-radius: 8px; padding: 12px; margin: 15px 0;
  }
  summary { font-weight: 600; color: #3182ce; cursor: pointer; }
  .doc-content {
    margin-top: 10px; padding-left: 15px;
    border-left: 3px solid #3182ce; font-size: 0.95em; color: #4a5568;
  }

  /* Iframe контейнер */
  .iframe-box {
    border: 1px solid #e2e8f0; border-radius: 8px;
    overflow: hidden; background: white; margin-top: 15px;
  }

  /* Кнопки */
  .btn {
    display: inline-block; padding: 8px 16px;
    border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9em;
    transition: background 0.2s;
  }
  .btn-primary { background: #3182ce; color: white !important; }
  .btn-primary:hover { background: #2b6cb0; }
  .btn-outline { border: 1px solid #3182ce; color: #3182ce !important; }
  .btn-outline:hover { background: #ebf8ff; }

  /* Таймлайн образования */
  .edu-item {
    position: relative; padding-left: 20px; margin-bottom: 20px;
    border-left: 2px solid #cbd5e0;
  }
  .edu-item::before {
    content: ""; position: absolute; left: -6px; top: 5px;
    width: 10px; height: 10px; border-radius: 50%; background: #3182ce;
  }
</style>

<div class="container">

  <!-- 1. ШАПКА -->
  <div class="profile-header">
    <img src="assets/avatar.jpg" class="avatar" alt="Тимур Файз">
    <h1>Тимур Файз</h1>
    <p style="color: #718096; font-weight: 500;">Data Engineer | Researcher</p>
    <p class="bio-text">
      Инженер-исследователь с фокусом на архитектуре данных и алгоритмах. 
      Мой путь — это сочетание фундаментальной школы МФТИ и прикладного Data Engineering в СПбГУ.
    </p>
  </div>

  <!-- 2. ТЕХНИЧЕСКИЙ СТЕК -->
  <div class="card">
    <h3>🛠 Технический Арсенал</h3>
    <div style="margin-bottom: 15px;">
      <span class="tech-badge core">C++ (STL)</span>
      <span class="tech-badge core">Python</span>
      <span class="tech-badge core">SQL (PostgreSQL)</span>
      <span class="tech-badge core">Algorithms & Data Structures</span>
    </div>
    <div>
      <span class="tech-badge">Apache Airflow</span>
      <span class="tech-badge">Apache Spark</span>
      <span class="tech-badge">dbt</span>
      <span class="tech-badge">Docker</span>
      <span class="tech-badge">Git (CI/CD)</span>
      <span class="tech-badge">Bash / Shell Scripting</span>
      <span class="tech-badge">Design Patterns (GoF)</span>
      <span class="tech-badge">SFML (Graphics)</span>
    </div>
  </div>

  <!-- 3. ОБРАЗОВАНИЕ (Единая история) -->
  <div class="card">
    <h2>🎓 Академический путь</h2>
    <p style="margin-bottom: 25px;">
      Прошел углубленную программу подготовки в двух ведущих технических вузах страны. 
      Имею подтвержденную базу (транскрипты) по ключевым инженерным дисциплинам.
    </p>

    <!-- МФТИ -->
    <div class="edu-item">
      <h3 style="margin: 0;">МФТИ (Московский физико-технический институт)</h3>
      <span style="font-size: 0.9em; color: #718096;">Фундаментальная информатика | <b>[Укажи кол-во семестров] семестров</b></span>
      <p style="margin-top: 5px; font-size: 0.95em;">
        <b>Ключевые дисциплины:</b> Алгоритмы и структуры данных, Архитектура ЭВМ, Углубленный C++, Линейная алгебра, Аналитическая геометрия.
        <br><i>Акцент на низкоуровневом понимании работы вычислительных систем и паттернах проектирования.</i>
      </p>
    </div>

    <!-- СПбГУ -->
    <div class="edu-item">
      <h3 style="margin: 0;">Санкт-Петербургский Государственный Университет (СПбГУ)</h3>
      <span style="font-size: 0.9em; color: #718096;">Прикладная математика, программирование и ИИ | Перевод / Продолжение обучения</span>
      <p style="margin-top: 5px; font-size: 0.95em;">
        <b>Специализация:</b> Анализ больших данных (Big Data), Построение ETL-пайплайнов, Распределенные системы.
        <br><i>Практическая реализация сложных инженерных проектов (см. FinBest).</i>
      </p>
    </div>

    <div style="margin-top: 25px;">
      <a href="ССЫЛКА_НА_ПАПКУ_СО_СПРАВКАМИ" class="btn btn-outline">
        📂 Посмотреть академические справки (Transcripts)
      </a>
    </div>
  </div>

  <!-- 4. ПРОЕКТ 1: FINBEST (Data Engineering) -->
  <div class="card">
    <div style="display:flex; justify-content:space-between; flex-wrap:wrap; align-items:center;">
      <h2 style="margin-top:0;">🚀 Проект: FinBest</h2>
      <span style="font-size:0.9em; color:#718096;">EtLT Pipeline • Airflow • Spark</span>
    </div>
    
    <p>
      <b>Практическая реализация EtLT-конвейера и графового анализа.</b><br>
      Система для обработки финансовых транзакций, решающая проблему соблюдения ФЗ-152 (маскирование данных) и ФЗ-115 (поиск мошеннических схем) в облачной среде.
    </p>

    <!-- Выдержка из Документа -->
    <details>
      <summary>📄 Цель и Архитектура (из Пояснительной записки)</summary>
      <div class="doc-content">
        <p><b>Проблема:</b> Необходимость безопасной обработки чувствительных данных в публичных облаках РФ.</p>
        <p><b>Решение:</b> Гибридная архитектура. "Легкая" трансформация (маскирование PII) происходит до загрузки, "Тяжелая" аналитика (Spark) — внутри контура.</p>
        <p><b>Стек:</b> Airflow (оркестрация), Pandas (Extract), Spark (Heavy Transform), dbt (Modeling), Superset (BI).</p>
      </div>
    </details>

    <!-- Галерея -->
    <p><i>📸 Галерея реализации (прокрутка вправо):</i></p>
    <div class="gallery-scroll">
      <img src="assets/architecture_scheme.png" class="gallery-item" alt="Architecture">
      <img src="assets/airflow_dag.png" class="gallery-item" alt="Airflow DAG">
      <img src="assets/superset_dashboard.png" class="gallery-item" alt="Superset">
      <img src="assets/graph_viz.png" class="gallery-item" alt="Graph Viz">
    </div>

    <!-- Интерактив -->
    <h3>🕸 Анализ связей (Interactive Graph)</h3>
    <p>Результат работы алгоритма кластеризации (GraphFrames). Граф интерактивен.</p>
    <div class="iframe-box" style="height: 500px;">
      <iframe src="html_exports/pyvis_graph.html" width="100%" height="100%" style="border:none;"></iframe>
    </div>

    <!-- Ноутбук -->
    <details>
      <summary>📓 Показать полный код (Jupyter Notebook)</summary>
      <div class="iframe-box" style="height: 600px;">
        <iframe src="html_exports/ad_hoc_analysis.html" width="100%" height="100%" style="border:none;"></iframe>
      </div>
    </details>

    <div style="margin-top:20px;">
      <a href="https://github.com/timurfays/FinBest" class="btn btn-primary">GitHub Repo</a>
      <a href="ССЫЛКА_НА_КУРСОВУЮ_PDF" class="btn btn-outline" style="margin-left:10px;">Скачать документацию (PDF)</a>
    </div>
  </div>

  <!-- 5. ПРОЕКТ 2: МФТИ (Software Engineering) -->
  <div class="card">
    <div style="display:flex; justify-content:space-between; flex-wrap:wrap; align-items:center;">
      <h2 style="margin-top:0;">🏛 МФТИ: Визуализация алгоритмов</h2>
      <span style="font-size:0.9em; color:#718096;">C++ • SFML • Design Patterns</span>
    </div>

    <p>
      <b>Интерактивная визуализация алгоритма Дейкстры.</b><br>
      Проект демонстрирует глубокое понимание ООП и паттернов проектирования. Вместо стандартного консольного вывода, создана графическая среда для наблюдения за работой алгоритма в реальном времени.
    </p>

    <details>
      <summary>⚙️ Технические детали и Паттерны</summary>
      <div class="doc-content">
        <p><b>Архитектура:</b> Использованы порождающие и поведенческие паттерны для гибкой настройки графа.</p>
        <p><b>Визуализация:</b> Библиотека SFML использована для рендеринга узлов и анимации процесса поиска пути.</p>
        <p><b>Оптимизация:</b> Эффективная работа с памятью и указателями (C++).</p>
      </div>
    </details>

    <div class="gallery-scroll">
      <img src="assets/sfml_demo.gif" class="gallery-item" alt="SFML Demo">
      <img src="assets/cpp_code.png" class="gallery-item" alt="Code Snippet">
      <img src="assets/mipt_photo1.jpg" class="gallery-item" alt="MIPT Campus">
    </div>
  </div>

  <!-- ПОДВАЛ -->
  <div style="text-align:center; color:#a0aec0; margin-top:50px; font-size:0.9em;">
    <p>Готов к решению сложных инженерных задач.</p>
    <a href="mailto:твоя_почта" style="color:#3182ce; text-decoration:none;">Email</a> • 
    <a href="https://t.me/твой_ник" style="color:#3182ce; text-decoration:none;">Telegram</a>
  </div>

</div>
