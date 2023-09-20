document.addEventListener('DOMContentLoaded', () => {
    const passInput = document.getElementById('password');
    const passInputConf = document.getElementById('pass_conf');
    const passShow = document.getElementById('show-pass');
    const form = document.getElementById('form');
    const errorMessage = document.querySelector('.messages-error');



    function showPassword() {
        if (passInput.type === 'password' || passInputConf.type === 'password') {
            passInput.type = 'text';
            passInputConf.type = 'text';
        } else {
            passInput.type = 'password';
            passInputConf.type = 'password';
        }
    }


    function passwordMatch(event) {
        event.preventDefault();

        if (passInput.value !== passInputConf.value) {
            let errorMsg = 'Passwords do not match';
            errorMessage.innerHTML = `<p> ${errorMsg} </p>`;
            errorMessage.style.display = 'block';
            passInputConf.style.border = "1px solid lightcoral";

            console.log('Passwords do not match');
        } else {
            errorMessage.style.display = 'none';
            passInputConf.style.border = "1px solid #ccc";
            form.submit();
        }
    }

    const passwordRules = {
        upper: /[A-Z]/,
        lower: /[a-z]/,
        digit: /\d/,
        minlength: /^.{8,12}$/,
        allowed: /^[-().&@?'#,/"+]$/,
        'max-consecutive': /(.)\1{2,}/
    };

    function validatePassword() {
        const password = passInput.value;
        const errors = [];

        for (const rule in passwordRules) {
            if (passwordRules.hasOwnProperty(rule)) {
                const regex = passwordRules[rule];
                if (!regex.test(password)) {
                    errors.push(rule);
                }
            }
        }

        if (errors.length > 0) {
            let errorMsg = '8-12 characters, use digits, @#~_-&, uppercase.';
            errorMessage.innerHTML = `<p> ${errorMsg} </p>`;
            errorMessage.style.display = 'block';
            passInput.style.border = "1px solid lightcoral";
        } else {
            errorMessage.style.display = 'none';
        }
    }




    passShow.addEventListener('click', showPassword);
    form.addEventListener('submit', passwordMatch);
    passInput.addEventListener('input', validatePassword);
});


