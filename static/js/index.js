document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const backspaceIcon = document.getElementById('backspace-search');
    const notificationBody = document.getElementById('notification-content');
    const notificationBtn = document.getElementById('notification-icon');
    const menu = document.querySelector('.menu');
    const asideBoxes = document.querySelectorAll('.aside-link');

    let notificationVisible = false;

    function toggleBackspaceIcon() {
        if (searchInput.value.trim() !== '') {
            backspaceIcon.style.display = 'inline-block';
        } else {
            backspaceIcon.style.display = 'none';
        }
    }

    function clearInputValue() {
        searchInput.value = '';
        toggleBackspaceIcon();
    }

    function showNotification() {
        notificationVisible = !notificationVisible;
        if (notificationVisible) {
            notificationBody.style.display = 'block';
        } else {
            notificationBody.style.display = 'none';
        }
    }

    function closeNotification(event) {
        if (notificationVisible && event.target !== notificationBtn) {
            notificationBody.style.display = 'none';
            notificationVisible = false;
        }
    }

    function toggleCollapsedAsideMenu() {
        if (asideBoxes.style === 'block') {
            asideBoxes.style === 'none'
        } else {
            asideBoxes.style === 'block'
        }
    }

    function toggleCollapsedAsideMenu() {
        asideBoxes.forEach(box => {
            const asideLink = box.querySelector('.aside-link');
            if (box.classList.contains('active')) {
                box.classList.remove('active');
                asideLink.style.display = 'none';
            } else {
                box.classList.add('active');
                asideLink.style.display = 'block';
            }
        });
    }

    menu.addEventListener('click', toggleCollapsedAsideMenu);


    toggleBackspaceIcon();
    menu.addEventListener('click', toggleCollapsedAsideMenu);
    searchInput.addEventListener('input', toggleBackspaceIcon);
    backspaceIcon.addEventListener('click', clearInputValue);
    notificationBtn.addEventListener('click', showNotification);
    document.addEventListener('click', closeNotification);

});







document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            tabButtons.forEach((btn) => btn.classList.remove('active'));

            if (tabContents[index]) {
                tabContents.forEach((content) => content.classList.remove('active'));

                button.classList.add('active');
                tabContents[index].classList.add('active');
            }
        });
    });
});


