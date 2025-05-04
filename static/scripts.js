document.getElementById('password')?.addEventListener('input', e => {
    const val = e.target.value;
    let score = 0;
    if (val.length >= 8) score++;
    if (/[A-Z]/.test(val)) score++;
    if (/[a-z]/.test(val)) score++;
    if (/\d/.test(val)) score++;
    if (/[^A-Za-z0-9]/.test(val)) score++;
    const percent = (score / 5) * 100;
    document.getElementById('strength-bar').style.width = percent + '%';
    const texts = ['Bardzo słabe', 'Słabe', 'Średnie', 'Dobre', 'Silne'];
    const index = score > 0 ? score - 1 : 0;
    document.getElementById('strength-text').textContent = texts[index];
  });
  
  const keyInput = document.getElementById('key-input');
  keyInput?.addEventListener('input', e => {
    const val = e.target.value;
    let score = 0;
    if (val.length >= 4) score++;
    if (val.length >= 8) score++;
    if (/[A-Z]/.test(val)) score++;
    if (/[a-z]/.test(val)) score++;
    const percent = (score / 4) * 100;
    document.getElementById('key-strength-bar').style.width = percent + '%';
    const textsKey = ['Bardzo słaby', 'Słaby', 'Średni', 'Dobry'];
    const idx = score > 0 ? Math.min(score - 1, textsKey.length - 1) : 0;
    document.getElementById('key-strength-text').textContent = textsKey[idx];
  });
  
  const vigForm = document.getElementById('vigenere-form');
  vigForm?.addEventListener('submit', e => {
    const key = vigForm.key.value;
    if (!/^[A-Za-z]+$/.test(key)) {
      alert('Klucz może zawierać tylko litery.');
      e.preventDefault();
    }
  });
  