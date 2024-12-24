<body>
    <div class="container">
        <h1>Duygu Tespiti API'si</h1>
        <p>Bu proje, FastAPI, TensorFlow ve OpenCV kullanarak duygu tespiti yapan bir API sağlar. Yüz görüntüsünden duygu tespiti yapmak için eğitilmiş bir model kullanır. Tespit edilen duygular aşağıdaki kategorilerden birine sınıflandırılır:</p>
        <ul>
            <li>Sinirli</li>
            <li>Tiksinti</li>
            <li>Korku</li>
            <li>Mutlu</li>
            <li>Notr</li>
            <li>Üzgün</li>
            <li>Şaşkın</li>
        </ul>
        <h2>API'ye Erişim</h2>
        <p>API şu anda aşağıdaki adreste çalışmaktadır:</p>
        <p><a href="https://emotion.baristok.com.tr" target="_blank">https://emotion.baristok.com.tr</a></p>
        <h2>Özellikler</h2>
        <ul>
            <li>Yüklenen gri tonlamalı bir görüntüden duygu tespiti yapar.</li>
            <li>Haar Cascade algoritması ile yüz tespiti gerçekleştirir.</li>
            <li>TensorFlow modeliyle duygu sınıflandırması yapar.</li>
            <li>Basit ve kullanımı kolay bir API uç noktası sunar.</li>
        </ul>
        <h2>Gereksinimler</h2>
        <p>Aşağıdaki araç ve kütüphanelerin kurulu olduğundan emin olun:</p>
        <ul>
            <li>FastAPI</li>
            <li>TensorFlow</li>
            <li>OpenCV</li>
            <li>NumPy</li>
            <li>PIL (Pillow)</li>
        </ul>
        <h2>Nasıl Çalıştırılır?</h2>
        <ol>
            <li><b>Sunucuyu başlatın:</b>
                <pre><code>uvicorn api:app --host 0.0.0.0 --port 8000</code></pre>
                <p>Sunucu şu adreste çalışacaktır: <code>http://127.0.0.1:8000</code></p>
                <p>Cloud server üzerinde API şu anda başarıyla çalışmaktadır:</p>
                <p><a href="https://emotion.baristok.com.tr" target="_blank">https://emotion.baristok.com.tr</a></p>
            </li>
        </ol>
    </div>
</body>
</html>
