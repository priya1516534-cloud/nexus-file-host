function loginAdmin() {
    const pass = document.getElementById('admin-pass').value;
    fetch('/api/admin/files', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({password: pass})
    })
    .then(res => res.json())
    .then(data => {
        if(data.success) {
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('file-list-section').style.display = 'block';
            const body = document.getElementById('files-body');
            body.innerHTML = data.files.map(f => 
                `<tr><td>${f.name}</td><td>${f.type}</td><td><a href="${f.link}" target="_blank">View</a></td></tr>`
            ).join('');
        } else {
            alert("Galt Password!");
        }
    });
                           }
