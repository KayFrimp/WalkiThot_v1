// Function to show/hide the sidebar
function showSidebar() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.style.display = (sidebar.style.display === 'none' || sidebar.style.display === '') ? 'flex' : 'none';
}

// Function to toggle the mobile menu
function toggleMenu() {
    var nav = document.querySelector('header nav ul');
    nav.classList.toggle('show');
}

// Initialize the Slick carousel
$('.post-wrapper').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    nextArrow: $('.next'),
    prevArrow: $('.prev'), // Fixed the duplicated 'nextArrow' to 'prevArrow'
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
    ]
});

/* login page */
function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Perform AJAX request to the server for login validation
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            alert('Login successful!');
            // You can redirect the user or perform other actions after successful login
        } else {
            alert('Login failed. Please check your username and password.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
/* signup page */
function validateForm() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;

    // Perform any additional client-side validation if needed

    // Perform AJAX request to the server for signup
    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password, confirmPassword }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            alert('Signup successful!');
            // You can redirect the user or perform other actions after successful signup
        } else {
            alert('Signup failed. Please check your information.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
