<!DOCTYPE html>
<html>
<head>
    <title>Alışveriş Listem</title>
    <style>
        body {
            background-color: #d8d8d8;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            color: rgb(154, 94, 94);
        }
 
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
 
        h1, h2 {
            color: rgb(154, 94, 94);
        }
 
        hr {
            background-color: rgb(116, 158, 149);
            height: 8px;
            border: 0;
            margin: 20px 0;
        }
 
        .step {
            display: none;
        }
 
        .step.active {
            display: block;
        }
 
        form {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
 
<div class="container" id="shopping-cart">
    <!-- Alışveriş Sepeti Bölümü -->
    <div class="step active" id="step1">
        <h1>Alışveriş Sepeti</h1>
 
        <!-- Ürün Ekleme Formu -->
        <form id="item-form">
            <input type="text" id="newitem" placeholder="Ürün Adı" required>
            <input type="number" id="price" placeholder="Birim Fiyatı (TL)" required>
            <input type="number" id="quantity" placeholder="Adet" required>
            <button type="button" onclick="AddNewItem()">Ekle</button>
        </form>
 
        <hr>
 
        <!-- Ürün Listesi Tablosu -->
        <h2>Ürünler</h2>
        <table id="items">
            <tr>
                <th>Ürün Adı</th>
                <th>Birim Fiyatı (TL)</th>
                <th>Adet</th>
                <th>Sil</th>
            </tr>
        </table>
 
        <hr>
 
        <!-- Toplam Tutar -->
        <h2>Toplam</h2>
        <div id="total">Toplam Tutar: 0 TL</div>
 
        <!-- İleri Butonu -->
        <button onclick="nextStep(1)">İleri</button>
    </div>
 
    <!-- Kişisel Bilgiler Bölümü -->
    <div class="step" id="step2">
        <h1>Kişisel Bilgiler</h1>
        <form id="personal-info-form">
            <input type="text" id="name" placeholder="İsim" required><br>
            <input type="tel" id="phone" placeholder="Telefon" required><br>
            <input type="email" id="email" placeholder="E-posta" required><br>
            <!-- Geri ve İleri Butonları -->
            <button type="button" onclick="nextStep(-1)">Geri</button>
            <button type="button" onclick="nextStep(1)">İleri</button>
        </form>
    </div>
 
    <!-- Teslimat Adresi Bölümü -->
    <div class="step" id="step3">
        <h1>Teslimat Adresi</h1>
        <textarea id="address" rows="4" placeholder="Teslimat Adresi" required></textarea><br>
        <!-- Geri ve İleri Butonları -->
        <button type="button" onclick="nextStep(-1)">Geri</button>
        <button type="button" onclick="nextStep(1)">İleri</button>
    </div>
 
    <!-- Kredi Kartı ile Ödeme Bölümü -->
    <div class="step" id="step4">
        <h1>Kredi Kartı ile Ödeme</h1>
        <form id="credit-card-form">
            <input type="text" id="cardname" placeholder="Kart Üzerindeki İsim" required><br>
            <input type="text" id="cardnumber" placeholder="Kart Numarası" required><br>
            <input type="text" id="expdate" placeholder="Son Kullanma Tarihi (AA/YY)" required><br>
            <input type="text" id="cvv" placeholder="CVV/CVC Kodu" required><br>
            <!-- Geri ve İleri Butonları -->
            <button type="button" onclick="nextStep(-1)">Geri</button>
            <button type="button" onclick="completePurchase()">Alışverişi Tamamla</button>
        </form>
    </div>
</div>
 
<!-- Fatura Ekranı -->
<div class="container" id="invoice" style="display:none;">
    <h1>Fatura</h1>
    <div id="invoice-details">
        <!-- Fatura detayları burada gösterilecek -->
    </div>
</div>
 
<script>
    var currentStep = 1;
    var totalAmount = 0;
 
    // Yeni ürün ekleme fonksiyonu
    function AddNewItem() {
        var itemName = document.getElementById("newitem").value;
        var itemPrice = parseFloat(document.getElementById("price").value);
        var itemQuantity = parseInt(document.getElementById("quantity").value);
 
        var newRow = document.getElementById("items").insertRow();
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        var cell3 = newRow.insertCell(2);
        var cell4 = newRow.insertCell(3);
 
        cell1.innerHTML = itemName;
        cell2.innerHTML = itemPrice;
        cell3.innerHTML = itemQuantity;
        cell4.innerHTML = "<button onclick='removeItem(this)'>Sil</button>";
 
        totalAmount += itemPrice * itemQuantity;
        document.getElementById("total").innerText = "Toplam Tutar: " + totalAmount + " TL";
    }
 
    // Ürünü silme fonksiyonu
    function removeItem(btn) {
        var row = btn.parentNode.parentNode;
        var price = parseFloat(row.cells[1].innerHTML);
        var quantity = parseInt(row.cells[2].innerHTML);
        totalAmount -= price * quantity;
        document.getElementById("total").innerText = "Toplam Tutar: " + totalAmount + " TL";
        row.parentNode.removeChild(row);
    }
 
    // Adım ileri/geri fonksiyonu
    function nextStep(step) {
        if (step === -1) {
            currentStep--;
        } else {
            var inputs = document.querySelectorAll('#step' + currentStep + ' input[required]');
            var isValid = true;
            for (var i = 0; i < inputs.length; i++) {
                if (!inputs[i].value) {
                    isValid = false;
                    break;
                }
            }
            if (!isValid) {
                alert('Lütfen tüm gerekli alanları doldurun.');
                return;
            }
            currentStep++;
        }
       
        // Aktif adımı göster
        document.getElementById('step' + currentStep).classList.add('active');
        document.getElementById('step' + (currentStep - step)).classList.remove('active');
    }
 
    // Alışverişi tamamlama fonksiyonu
    function completePurchase() {
        var personalInfoForm = document.getElementById("personal-info-form");
        var address = document.getElementById("address").value;
        var creditCardForm = document.getElementById("credit-card-form");
        if (personalInfoForm.checkValidity() && address && creditCardForm.checkValidity()) {
            // Alışveriş tamamlama işlemi buraya gelecek
            document.getElementById("shopping-cart").style.display = "none";
            document.getElementById("invoice").style.display = "block";
 
            // Fatura detaylarını oluştur
            var invoiceDetails = document.getElementById("invoice-details");
            invoiceDetails.innerHTML = "<p><strong>Kişisel Bilgiler:</strong></p>" +
                "<p>İsim: " + document.getElementById("name").value + "</p>" +
                "<p>Telefon: " + document.getElementById("phone").value + "</p>" +
                "<p>E-posta: " + document.getElementById("email").value + "</p>" +
                "<p><strong>Teslimat Adresi:</strong></p>" +
                "<p>" + address + "</p>" +
                "<p><strong>Toplam Tutar:</strong> " + totalAmount + " TL</p>";
        } else {
            alert("Lütfen faturanızı görüntüleyebilmek için doğru bir E-posta girin ve tüm bilgilerinizin eksiksiz girildiğinden emin olun.");
        }
    }
</script>
</body>
</html>
