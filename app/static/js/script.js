// -- Functions --

// Go home
function goHome() {
    window.location.replace('http://127.0.0.1:5000');
}

// -- Shortcuts

function logout(e) {
    if (e.shiftKey && e.ctrlKey && e.altKey && e.key === 'L') {
        window.location.replace('https://dry-spire-09763.herokuapp.com/logout');
        // window.location.replace('http://127.0.0.1:5000/logout');
    }
}

// -- Shortcuts handler

document.addEventListener('keyup', logout, false);